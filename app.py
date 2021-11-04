from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)
from datetime import datetime, timedelta
from pymongo import MongoClient
import json, jwt

# 우분투에서 사용하는 DB
# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.cafes
SECRET_KEY = "SARANGBANG"

# 메인 화면 - 토큰 기한이 남아있으면 바로 글 목록 페이지로 이동
@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.userdb.find_one({'id': payload['id']})

        return render_template('layout_postlist.html', user_info=user_info)

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

    return render_template('login.html')


# 로그인 화면
@app.route('/login')
def login():
    return render_template('login.html')


# 글 상세 화면
@app.route('/postview')
def layout_postview():
    token_receive = request.cookies.get('mytoken')

    try:
        jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        return render_template('layout_postview.html')

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))

    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="페이지 정보가 존재하지 않습니다."))


# 글쓰기 화면
@app.route('/writing')
def layout_writing():
    token_receive = request.cookies.get('mytoken')

    try:
        jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        return render_template('layout_writing.html')

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))

    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


@app.route('/api/getid', methods=['GET'])
def getID():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.userdb.find_one({'id': payload['id']})
        user_id = user_info['id']

        return jsonify({'user_id': user_id})

    except jwt.ExpiredSignatureError:
        return jsonify({'msg': "로그인 시간이 만료되었습니다."})

    except jwt.exceptions.DecodeError:
        return jsonify({'msg': "로그인 정보가 존재하지 않습니다."})

    return jsonify({'msg': '알 수 없는 예외사항 발생.'})


# 로그인 성공할때 토큰 생성
@app.route('/api/login', methods=['POST'])
def sign_in():
    id_receive = request.form['username_give']
    pw_receive = request.form['password_give']
    result = db.userdb.find_one({'id': id_receive, 'pw': pw_receive})
    payload = {
        'id': id_receive,
        'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    if result is not None:
        # 우분투에서 사용하는 return
        # return jsonify({'result': 'success', 'token': token.decode('utf-8')})
        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


# 글 저장하기 호출 시
@app.route('/api/writing', methods=['POST'])
def save_writing():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.userdb.find_one({'id': payload['id']})
        writer_name = user_info['id']  # 토큰에서 정보 가져오기

        # 클라이언트로 부터 정보 넘겨받기
        cafe_name = request.form['cafe_name']
        cafe_address = request.form['cafe_address']
        cafe_coment = request.form['cafe_coment']
        cafe_img = request.form['cafe_img']
        user_mentlist = []

        doc = {
            'writer_name': writer_name,
            'cafe_name': cafe_name,
            'cafe_address': cafe_address,
            'cafe_coment': cafe_coment,
            'cafe_img': cafe_img,
            'user_mentlist': user_mentlist
        }

        client.cafes.cafelist.insert_one(doc)

        return jsonify({'msg': '저장되었습니다.'})  # 저장 완료됨을 알림

    except jwt.ExpiredSignatureError:
        return jsonify({'msg': "로그인 시간이 만료되었습니다."})

    except jwt.exceptions.DecodeError:
        return jsonify({'msg': "로그인 정보가 존재하지 않습니다."})


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

    new_mentlists = data['user_mentlist']
    new_mentlists.append(user_ment_info)

    db.cafelist.update_one({'writer_name': writer_name[9:], 'cafe_name': cafe_name[8:]},
                           {'$set': {'user_mentlist': new_mentlists}})

    return jsonify({'msg': '댓글이 저장되었습니다.'})


# 댓글 삭제기능 호출 시
@app.route('/api/delment', methods=['POST'])
def delete_userment():
    writer_name = request.form['writer_name']
    cafe_name = request.form['cafe_name']
    user_ment_info = json.loads(request.form['ment'])

    data = db.cafelist.find_one({'writer_name': writer_name[9:], 'cafe_name': cafe_name[8:]}, {'_id': False})

    new_mentlists = data['user_mentlist']
    del_index = new_mentlists.index(user_ment_info)
    del new_mentlists[del_index]

    db.cafelist.update_one({'writer_name': writer_name[9:], 'cafe_name': cafe_name[8:]},
                           {'$set': {'user_mentlist': new_mentlists}})

    return jsonify({'msg': '댓글이 저장되었습니다.'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
