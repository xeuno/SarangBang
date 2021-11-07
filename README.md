<h3 align="center"><b>항해99 1주차 4팀, 사랑방(SarangBang)</b></h3>

<h4 align="center">📆 2021.11.01 ~ 2021.11.06</h4>

---

<br>
<h3 align="center"><b>🛠 Tech Stack 🛠</b></h3>
<p align="center">
<img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
<img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white">
<img src="https://img.shields.io/badge/html-E34F26?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
<img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black">
<img src="https://img.shields.io/badge/aws-232F3E?style=for-the-badge&logo=aws&logoColor=white">
</br>
<img src="https://img.shields.io/badge/Python-F80000?style=for-the-badge&logo=Python&logoColor=white">
<img src="https://img.shields.io/badge/Flask-4FC08D?style=for-the-badge&logo=Flask&logoColor=white">
<img src="https://img.shields.io/badge/Jinja-7952B3?style=for-the-badge&logo=Jinja&logoColor=white">
<img src="https://img.shields.io/badge/MongoDB-61DAFB?style=for-the-badge&logo=MongoDB&logoColor=white">

<br><br>
<h3 align="center"><b>🎬 Getting Started 🎬</b></h3>
<pre>
<code>
~$ cd sarangbang
~$ sudo chmod 755 initail_ec2.sh
~$ ./initial_ec2.sh
~$ pip install flask
~$ pip install mongo
~$ python3 app.py
</code>
</pre>

<br>
<h3 align="center"><b>📂 Project Directory Structure 📁</b></h3>
<pre>
<code>
/static
  └──/css
     ├── /login.css
     ├── /main.css
     ├── /header.css
     ├── /footer.css
     ├── /reset.css
     ├── /join_membership
     ├── /postview.css
     ├── /writing.css
     └── /postlist.css
  └──/img
     ├── /logo.png
     └── /banner.png
  └──/js
     ├── /join_membership.js
     ├── /layout_postlist.js
     ├── /layout_postview.js
     ├── /layout_writing.js
     └── /login.js
/templates
  └──/layout_section
     ├── /header.html
     └── /footer.html
  ├── /layout.html
  ├── /join_membership.html
  ├── /layout_postlist.html
  ├── /layout_postview.html
  ├── /layout_writing.html
  └── /login.html

├── /README.md
├── /app.py
</code>
</pre>

---

<h3 align="center"><b>📢 Main function 📢</b></h3>
<br>
<h4 align="center"><b>📰 Login Page 📰</b></h4>

<table width="100%">
    <tr>
        <td width="60%"><img src="https://user-images.githubusercontent.com/57797592/140597056-2d5732ee-1d16-4d5e-963c-53534021a238.PNG" /></td>
        <td width="40%">JWT 방식을 사용하여 로그인 기능을 구현하였습니다.</td>
    </tr>
</table>

---

<br>
<h4 align="center"><b>📰 Join Membership Page 📰</b></h4>

<table width="100%">
    <tr>
        <td width="60%"><img src="https://user-images.githubusercontent.com/57797592/140597087-27822dce-c3f2-4326-8dd0-b11d09d2c24f.PNG" /></td>
        <td width="40%">회원가입을 할 수 있는 페이지 입니다.</td>
    </tr>
</table>

---

<br>
<h4 align="center"><b>📰 Post Section Page 📰</b></h4>

<table width="100%">
    <tr>
        <td width="60%"><img src="https://user-images.githubusercontent.com/57797592/140597095-ac455453-77c1-41db-a4a0-b6ad829fc549.PNG" /></td>
        <td width="40%">- 작성된 글 목록을 볼 수 있습니다! 글 목록은 Jinja 서버 사이드 렌더링으로 구현하여 빠른 페이지 로딩이 가능합니다. <br>- 포스트를 클릭하면 상세페이지로 이동할 수 있습니다. <br>- 헤더 부분의 로그아웃 버튼을 누르면 로그아웃이 가능합니다. <br>- 헤더 부분의 글쓰기 버튼을 누르면 글쓰기 페이지로 이동합니다. <br>- 검색란에 카페의 이름을 검색하면 해당하는 카페의 포스트를 볼 수 있습니다.</td>
    </tr>
</table>

---

<br>
<h4 align="center"><b>📰 Post Writing Page 📰</b></h4>
<table width="100%">
    <tr>
        <td width="60%"><img src="https://user-images.githubusercontent.com/57797592/140597459-bb706ace-85ed-49a0-8016-70dc9bf70e4f.PNG" /></td>
        <td width="40%">- 파일 선택 버튼을 누르면 내 컴퓨터에 있는 이미지 파일을 로드할 수 있습니다. <br>- 카페 이름, 주소, 코멘트를 작성할 수 있습니다. <br>- 저장하기 버튼 클릭 시, DB에 글이 저장됩니다. 모든 입력란이 채워지지 않으면 글을 저장할 수 없습니다.</td>
    </tr>
    <tr>
        <td width="60%"><img src="https://user-images.githubusercontent.com/57797592/140597444-bc379eae-a5f2-4f84-bc9f-1b916e753074.PNG" /></td>
        <td width="40%">다 작성한 후 페이지의 모습입니다.</td>
    </tr>
</table>

---

<br>
<h4 align="center"><b>📰 Post Detail Page 📰</b></h4>

<table width="100%">
    <tr>
        <td width="60%"><img src="https://user-images.githubusercontent.com/57797592/140597172-9e8f76d9-95ed-49c8-8978-c7a29e1edc97.PNG" /></td>
        <td width="40%">-클릭한 포스트의 정보들을 볼 수 있습니다. <br> - 댓글 작성 기능이 있어 댓글을 달 수 있고, 로그인한 ID로 작성했던 댓글들은 삭제할 수 있습니다. JWT 토큰을 이용해 사용자 검증을 하여 본인이 작성한 댓글에만 삭제 버튼이 보이도록 구현하였습니다.</td>
    </tr>
</table>

---

<h4 align="center"><b>👨🏻‍🤝‍👨🏻 Members 👨🏻‍🤝‍👨🏻</b></h4>
<br>
<table>
    <tr>
        <td align="center">
        <a href="https://diddl.tistory.com/"><img src="https://img.shields.io/badge/양성은-000AFF?style=뱃지모양&logo=로고&logoColor=white"/></a>
        </td>
        <td align="center">
        <a href="https://velog.io/@hamkke"><img src="https://img.shields.io/badge/이서현-2DDC88?style=뱃지모양&logo=로고&logoColor=black"/></a>
        </td>
        <td align="center">
        <a href="https://luce-sicut-stella.tistory.com/"><img src="https://img.shields.io/badge/송민지-D77EE9?style=뱃지모양&logo=로고&logoColor=white"/></a>
        </td>
        <td align="center">
        <a href="https://github.com/WooMinGy"><img src="https://img.shields.io/badge/우민기-FAFF00?style=뱃지모양&logo=로고&logoColor=black"/></a> 
        </td>
    </tr>
    <tr>
        <th width="25%" align="center">:spider_web: BACK-END
        </th>
        <th width="25%" align="center">:spider_web: FRONT-END
        </th>
        <th width="25%" align="center">:spider_web: BACK-END 
        </th>
        <th width="25%" align="center">:spider_web: FRONT-END
        </th>
    </tr>
    <tr>
        <td align="center">끝없이 인내하고 끝없이 노력하고 끝없이 겸손하자.
        </td>
        <td align="center">큰 나무는 작은 묘목으로 시작되고, 큰 사람은 작은 가르침으로 시작된다. 감사도 작은 것부터 시작해야 한다.
        </td>
        <td align="center">과거로 거슬러 올라가지 말고 미래를 바라지도 말라
        </td>
        <td align="center">사람은 어려움 속에서 성장한다.
        </td>
    </tr>
</table>

---

<h4 align="center"><b>✏ Trouble Shooting ✏</b></h4>
<br>
<details>
    <summary>
        <b>js File에서 Element를 제대로 불러오지 못하는 문제</b>
    </summary>
    <br>해결 : head에 있던 script를 body 맨 아래 부분으로 위치를 옮김.
</details>

<details>
    <summary>
        <b>button의 onclick 함수가 동작하지 않는 문제</b>
    </summary>
  <br><b>해결 : button tag에 type지정을 해준다.</b>
    
```html
    <!-- File : "../templates/join_membership.html" -->
    <button id="joinBox" onclick="signup()" type="button">가입하기</button>
```

</details>

<details>
    <summary>
        <b>header.html에 로그아웃, 글쓰기 메뉴를 포함하여 렌더링 해서 로그인, 회원가입 페이지에서도 로그아웃, 글쓰기 메뉴가 보이는 문제</b>
    </summary>
<br><b>해결 : 페이지 로드 시 href 값 비교를 통해 로그인, 회원가입 페이지라면 해당 태그를 display:none으로 설정해 안보이게 함.</b>

```html
    <!-- File: "../templates/layout_section/header.html" -->
    <ul class="gnb_list">
        <li><a href="" onclick="logout()">로그아웃</a></li>
        <li><a href="/writing">글 쓰기</a></li>
    </ul>

```

```javascript
    //해결 File: "../static/js/login.js"
    window.addEventListener('load', function () {
        let login_page = '/login'; //로그인 페이지 경로 -> 로그아웃 페이지에서 적용할 시, '/joinMembership'으로 설정하면 됨
        let now_href = location.pathname; //현재 페이지 경로
        let hide_gnb = document.querySelector('.gnb_list');
        let logo_center = document.querySelector('.nav');
        if (now_href === login_page) { //만약 현재 경로가 로그인 페이지 경로라면
            hide_gnb.style.display = 'none'; //안보이게 설정하기
            logo_center.style.justifyContent = 'center';
        }
    });
```

</details>
	
<details>
    <summary>
        <b>로그인 시 받아오는 JWT 토큰을 쿠키에 저장할 때 경로를 지정하여, 지정한 경로 외의 페이지에서는 쿠키를 가져올 수 없는 문제</b>
    </summary>
<br><b>해결 : Path설정을 제거해주어 모든 경로에서 쿠키를 가져올 수 있도록 구성함.</b>

```javascript
    //문제 코드 File : "../static/js/login.js의 login_JWT() 내부"
    success: function (response) {
        if (response['result'] === 'success') {
            $.cookie("mytoken", response['token'], {path: '/'});
            window.location.replace("/")
        } else {
            alert(response['msg'])
        }
    }
```

```javascript
   //수정하여 해결한 코드     
   success: function (response) {
            if (response['result'] === 'success') {
                $.cookie("mytoken", response['token']);
                window.location.replace("/")
            } else {
                alert(response['msg'])
            }
        }
```

</details>

<details>
    <summary>
        <b>input을 이용해 내 컴퓨터에 있는 파일 업로드 시 이미지 경로가 fakePath로 나오는 문제</b>
    </summary>
    사용자가 로드한 이미지를 DB에 저장하기 위해 이미지 경로를 python API 서버 쪽으로 넘겨 서버 측에서 파일을 바이너리 형태로 변환하여 저장하려 했으나 fakepath로 인해 파일 경로를 알 수 없었다

```html
    <!-- File : "../templates/layout_writing.html" -->
    <form class="cafeImg-form" method="post" enctype="multipart/form-data"> <!-- 이미지 파일 데이터에 알맞는 enctype 설정 -->
        <div class="image-show" id="image-show"> <!-- 이미지 띄울 공간 --> </div>
        <input type="file" accept="image/*" onchange="loadFile(this)"> <!-- 이미지 로드함수 호출 -->
    </form>
```
    
File : "../static/js/layout_writing.js"
    
```javascript
    function loadFile(input) {
        let file = input.files[0]; //선택된 파일 가져오기
    
        let newImage = document.createElement("img"); //새 이미지 추가
        newImage.src = URL.createObjectURL(file); //이미지 source 가져오기 -> fakePath
        newImage.id = "cafe-image"
        newImage.style.width = "100%";
        newImage.style.height = "100%";
        newImage.style.objectFit = "cover";
    
        //이미지를 image-show div에 추가
        let container = document.getElementById('image-show');
        container.appendChild(newImage);
    }
```

<br><b>해결 : javascript에서 이미지를 Base64 형태로 인코딩하여 해당 값을 넘기도록 구현</b>

```javascript
    function loadFile(input) {
        let file = input.files[0]; //선택된 파일 가져오기
    
        let newImage = document.createElement("img"); //새 이미지 추가
        newImage.src = URL.createObjectURL(file); //이미지 source 가져오기
        newImage.id = "cafe-image"
        newImage.style.width = "100%";
        newImage.style.height = "100%";
        newImage.style.objectFit = "cover";
    
        //이미지를 image-show div에 추가
        let container = document.getElementById('image-show');
        container.appendChild(newImage);
    
        //이미지를 서버에 저장하기 위해 base64 형태로 변환
        imgToBase64ByFileReader(document.getElementById('cafe-image').getAttribute("src"));
    }
```            
    
```javascript
    function imgToBase64ByFileReader(url) {
        return new Promise((resolve, reject) => {
            let xhr = new XMLHttpRequest();
            xhr.onload = () => {
                let reader = new FileReader();
                reader.onloadend = function () {
                    resolve(reader.result);
                    document.getElementById('cafe-image').setAttribute('src', reader.result);
                }
                reader.readAsDataURL(xhr.response); //Base64형식으로 인코딩
            }
            xhr.open('GET', url);
            xhr.responseType = 'blob';
            xhr.send();
        });
    }
```
    
</details>

<details>
    <summary>
        <b>AJAX로 배열을 전송할 때 에러 발생하는 문제</b>
    </summary>
<br><b>해결 : javascript에서 이미지를 Base64 형태로 인코딩하여 해당 값을 넘기도록 구현</b>
<br>배열은 객체에 해당하므로 json방식으로 직렬화해서 보낸 후 받는 쪽에서는 역직렬화를 통해 데이터를 얻을 수 있다.
<ul>
    <li><b>serialization 직렬화</b></li>
    : 객체를 쉽게 옮길 수 있는 형태로 변환하는 과정.
    <: 직렬화된 객체는 HTTP를 사용해 클라이언트-서버 간 옮길 수 있다.
    <li><b>deserialization 역직렬화</b></li>
    : 직렬화와 반대되는 기능, 직렬화된 객체를 재구성한다.
</ul>

```javascript
    // File : "../static/js/layout_postview.js"
    function delUserMent(obj) {
        let writer_name = document.getElementById('writer-show').innerText;
        let cafe_name = document.getElementById('name-show').innerText;
        let user_ment_dict = {} //댓글 정보를 담을 딕셔너리

        user_ment_dict['user_name'] = user_id;
        user_ment_dict['ment'] = obj.getElementsByClassName('inputValue')[0].innerText;
        user_ment_dict['date'] = obj.getElementsByClassName('time')[0].innerText;

        $.ajax({
            type: "POST",
            url: "/api/delment",
            data: {
                writer_name: writer_name,
                cafe_name: cafe_name,
                ment: JSON.stringify(user_ment_dict) // JSON으로 직렬화
            },
            success: function (response) {}
        })
    }
```

```python
    # File : ../app.py
    @app.route('/api/delment', methods=['POST'])
    def delete_userment():
        writer_name = request.form['writer_name']
        cafe_name = request.form['cafe_name']
        user_ment_info = json.loads(request.form['ment']) # JSON 역직렬화
    
        data = db.cafelist.find_one({'writer_name': writer_name[9:], 'cafe_name': cafe_name[8:]}, {'_id': False})
    
        new_mentlists = data['user_mentlist']
        del_index = new_mentlists.index(user_ment_info)
        del new_mentlists[del_index]
    
        db.cafelist.update_one({'writer_name': writer_name[9:], 'cafe_name': cafe_name[8:]},
                               {'$set': {'user_mentlist': new_mentlists}})
    
        return jsonify({'msg': '댓글이 저장되었습니다.'})
```    
    
</details>

<details>
    <summary>
        <b>AWS ec2 서버에서 app.py 실행 시, JWT token 전달 시 object of type bytes is not json serializable 에러 발생 문제</b>
    </summary>
<br><b>해결 : token.decode('utf-8')을 통해 byte 타입으로 반환된 토큰을 str 형식으로 변환해주기</b>
<br>같은 코드인데 로컬 호스트에서 실행하는 것과 AWS 서버에서 실행하는 결과가 다른지..-> 구글링해보니 jwt 버전차이라고 한다!!
    
```python
    # File : ../app.py
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
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
            return jsonify({'result': 'success', 'token': token})
        else:
            return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})
```

</details>

<details>
    <summary>
        <b>AJAX POST 요청에서 render_template로 페이지 이동이 안되는 문제 (해결했으나 다른 문제 발생으로 현재는 다른방법으로 구현했음)</b>
    </summary>
<br><b>응답 받는 부분에 document.write(response)로 해결</b>
<br>AJAX로 POST 요청을 보낼 때 요청은 자바스크립트에서 오는 것이고 플라스크의 응답 데이터는 자바 스크립트에 저장된다고 한다. 브라우저 자체에는 직접 보내거나 받는게 없으므로 페이지를 다시 렌더링하지 않는다. 따라서 받는 쪽에서 페이지를 새로 써줌으로써 해결.

```javascript
    function showPost(data) {
        let writer_name = sessionStorage.getItem(data);

        $.ajax({
            type: "POST",
            url: "/api/postdown",
            data: {
                writer_name: writer_name,
                cafe_name: data
            },
            success: function (response) {
                document.write(response); //페이지 쓰기
                showDBMents(ments);
            }
        });
    }
```

</details>

<details>
    <summary>
        <b>AJAX POST 요청에서 render_template로 페이지 이동이 안되는 문제 해결 - 2_jinja2를 이용한 경로 변경 및 api 호출</b>
    </summary>
  <br><b>해결 : html에서 파이썬 서버쪽으로 서버에서 전달받은 작성자, 글 제목을 경로로 지정하여 호출</b>
<br>AJAX로 POST 요청을 보낼 때 요청은 자바스크립트에서 오는 것이고 플라스크의 응답 데이터는 자바 스크립트에 저장된다고 한다.
<br>브라우저 자체에는 직접 보내거나 받는게 없으므로 페이지를 다시 렌더링하지 않는다. 따라서 받는 쪽에서 페이지를 새로 써줌으로써 해결.
포스트 하나(card-box클래스를 가진 div)를 선택했을 때 서버에서 받은 작성자, 글 제목를 경로로 다시 api 호출
    
```html
    <!-- File : "../templates/layout_postlist.html" -->
    <!-- 글 목록 나타낼 공간 서버 사이드 렌더링 적용 -->
    <div class="card-list" id="card-list">
        {% for one_post in postdata %}
            <div class="card-box" onclick="location.href='/{{ one_post.writer_name }}/{{ one_post.cafe_name }}'">
                <div class="card">
                    <img class="card-image" src={{ one_post.cafe_img }}>
                    <div class="text" style="margin: 10px">
                        <small>작성자: {{ one_post.writer_name }}</small>
                        <h2 class="cafe-title">이름: {{ one_post.cafe_name }}</h2>
                        <h3 class="cafe-coment">{{ one_post.cafe_coment }}</h3>
                        <small>주소: {{ one_post.cafe_address }}</small>
                    </div>
                </div>
            </div>
        {% endfor %}
    </div>
```

<br>서버 측에서는 해당경로를 변수로 받을 수 있게 구현, 받은 정보에 해당하는 포스트 내용을 다시 rendering해주도록 구현하였다.    
    
```python
    # app.py
    @app.route('/<writer_name>/<cafe_name>') #html에서 전달해주는 값을 받을 변수..변수를 경로로 지정해놓음으로써 포스트마다 실행될 수 있게 구현
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
```    
    
</details>
