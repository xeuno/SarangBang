from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client.cafes

#mainpage 이동
@app.route('/')
def home():
    return render_template('main.html')


#이미지 가져오기
@app.route('/api/imgdown', methods=['GET'])
def image_download():
    data = list(db.cafelist.find({}, {'_id': False}))
    return jsonify({'all_data': data})

#로그아웃
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('/login.html'))

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)