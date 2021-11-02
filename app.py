from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.cafes

## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('layout.html')

@app.route('/writing')
def layout_writing():
    return render_template('layout_writing.html')

# 저장하기(POST) API
@app.route('/writing', methods=['POST'])
def save_order():
    # 클라이언트로 부터 정보 넘겨받기
    cafe_name = request.form['cafe_name']
    cafe_address = request.form['cafe_address']
    cafe_coment = request.form['cafe_coment']
    cafe_img = request.form['cafe_img']

    doc = {
        'cafe_name': cafe_name,
        'cafe_address': cafe_address,
        'cafe_coment': cafe_coment,
        'cafe_img': cafe_img
    }
    db.cafelist.insert_one(doc)

    return jsonify({'msg': '저장되었습니다.'})  # 저장 완료됨을 알림

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)