from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)
from datetime import datetime, timedelta
from pymongo import MongoClient
import jwt, json

# 우분투에서 사용하는 DB
# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.cafes
SECRET_KEY = "SARANGBANG" #토큰 발급 SECRET_KEY

# 메인 화면 - 토큰 기한이 남아있으면 바로 글 목록 페이지로 이동
@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.userdb.find_one({'id': payload['id']})
        if user_info is not None:
            # 글 목록들을 DB에서 가져와 글 목록 페이지로 넘겨주기
            postdata = list(db.cafelist.find({}, {'_id': False}))

        return render_template("layout_postlist.html", postdata=postdata)  # 포스트들이 담긴 리스트를 넘겨준다!

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

# 로그인 화면으로 이동
@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)

# 회원 가입 화면으로 이동
@app.route('/joinMembership')
def joinMembership():
    return render_template('join_membership.html')


# 글쓰기 화면으로 페이지 이동 시 토큰 검사를 통해 유효성을 검사한다
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


# 회원가입 하기
@app.route('/signup', methods=['POST'])
def signUp():
    user_id = request.form['user_id']
    user_password = request.form['user_password']

    doc = {
        'id': user_id,
        'pw': user_password
    }
    db.userdb.insert_one(doc)
    return jsonify({'msg': '회원가입이 완료되었습니다.'})


# 아이디 중복 확인
@app.route('/check_dup', methods=['POST'])
def check_dup():
    check_id = request.form['check_id']
    if db.userdb.find_one({'id': check_id}) is None:
        return jsonify({'msg': "사용 가능한 아이디 입니다."})
    else:
        return jsonify({'exists': "이미 존재하는 아이디 입니다."})


# 로그인 성공할때 토큰 생성
@app.route('/api/login', methods=['POST'])
def sign_in():
    id_receive = request.form['username_give']
    pw_receive = request.form['password_give']
    result = db.userdb.find_one({'id': id_receive, 'pw': pw_receive})

    if result is not None:
        payload = {
            'id': id_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        # 우분투에서 사용하는 return
        # return jsonify({'result': 'success', 'token': token.decode('utf-8')})
        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


# 글 저장하기 호출 시 마찬 가지로 토큰 검사 후 글을 저장할 수 있다.
@app.route('/api/writing', methods=['POST'])
def save_writing():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.userdb.find_one({'id': payload['id']})
        writer_name = user_info['id']  # 토큰에서 ID 정보 가져오기

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
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))

    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 올바르지 않습니다."))

# 상세 글 보기
@app.route('/<writer_name>/<cafe_name>')
def show_clicked_post(writer_name, cafe_name):
    token_receive = request.cookies.get('mytoken')
    print(token_receive)

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.userdb.find_one({'id': payload['id']})
        user_id = user_info['id']

        data = db.cafelist.find_one({'writer_name': writer_name, 'cafe_name': cafe_name}, {'_id': False})
        writer_id = data['writer_name']
        cafe_name = data['cafe_name']
        cafe_address = data['cafe_address']
        cafe_img = data['cafe_img']
        cafe_coment = data['cafe_coment']
        user_mentlist = data['user_mentlist']

        return render_template("layout_postview.html",
                               writer_id=writer_id,
                               cafe_name=cafe_name,
                               cafe_address=cafe_address,
                               cafe_img=cafe_img,
                               cafe_coment=cafe_coment,
                               user_mentlist=user_mentlist,
                               current_user=user_id)

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))

    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 올바르지 않습니다."))


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


# 댓글 쓸때 현재 유저가 누군지 알려주는 역할
@app.route('/api/getid', methods=['GET'])
def getID():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.userdb.find_one({'id': payload['id']})
        user_id = user_info['id']

        return jsonify({'user_id': user_id})

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))

    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 올바르지 않습니다."))


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
