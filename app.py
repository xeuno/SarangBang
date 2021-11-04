from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client.cafes

# 메인 화면
@app.route('/')
def homework():
    return render_template('layout_postlist.html')

# 글쓰기 화면
@app.route('/writing')
def layout_writing():
    return render_template('layout_writing.html')

# 상세 페이지 화면
@app.route('/postview')
def layout_postview():
    return render_template('layout_postview.html')

# 글 저장하기 호출 시
@app.route('/api/writing', methods=['POST'])
def save_writing():
    # 클라이언트로 부터 정보 넘겨받기
    writer_name = request.form['writer_name']
    cafe_name = request.form['cafe_name']
    cafe_address = request.form['cafe_address']
    cafe_coment = request.form['cafe_coment']
    cafe_img = request.form['cafe_img']
    user_ment = []

    doc = {
        'writer_name': writer_name,
        'cafe_name': cafe_name,
        'cafe_address': cafe_address,
        'cafe_coment': cafe_coment,
        'cafe_img': cafe_img,
        'user_ment': user_ment
    }

    db.cafelist.insert_one(doc)

    return jsonify({'msg': '저장되었습니다.'})  # 저장 완료됨을 알림

# 글 목록 불러오기 호출 시
@app.route('/api/postlist', methods=['GET'])
def cafelists_down():
    data = list(db.cafelist.find({}, {'_id': False}))
    return jsonify({'downlists': data})

# 상세 글 정보 불러오기 호출 시
@app.route('/api/postdown', methods=['POST'])
def post_down():
    writier_name = request.form['writer_name']
    cafe_name = request.form['cafe_name']

    data = db.cafelist.find_one({'writer_name': writier_name, 'cafe_name': cafe_name[4:]}, {'_id': False})
    return jsonify({'downlists': data})


# 댓글 저장기능 호출 시
@app.route('/api/userment', methods=['POST'])
def save_userment():
    writer_name = request.form['writer_name']
    cafe_name = request.form['cafe_name']
    user_ment_info = json.loads(request.form['ment'])

    data = db.cafelist.find_one({'writer_name': writer_name[9:], 'cafe_name': cafe_name[8:]}, {'_id': False})

    new_mentlists = data['user_ment']
    new_mentlists.append(user_ment_info)

    db.cafelist.update_one({'writer_name': writer_name[9:], 'cafe_name': cafe_name[8:]},
                           {'$set': {'user_ment': new_mentlists}})

    return jsonify({'msg': '댓글이 저장되었습니다.'})


# 댓글 삭제기능 호출 시
@app.route('/api/delment', methods=['POST'])
def delete_userment():
    writer_name = request.form['writer_name']
    cafe_name = request.form['cafe_name']
    user_ment_info = json.loads(request.form['ment'])

    data = db.cafelist.find_one({'writer_name': writer_name[9:], 'cafe_name': cafe_name[8:]}, {'_id': False})

    new_mentlists = data['user_ment']
    del_index = new_mentlists.index(user_ment_info)
    del new_mentlists[del_index]

    db.cafelist.update_one({'writer_name': writer_name[9:], 'cafe_name': cafe_name[8:]},
                           {'$set': {'user_ment': new_mentlists}})

    return jsonify({'msg': '댓글이 저장되었습니다.'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)