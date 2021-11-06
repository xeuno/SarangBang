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
        <b>header.html에 로그아웃, 글쓰기 메뉴를 포함하여 렌더링 해서 로그인, 회원가입 페이지에서도 로그아웃, 글쓰기 메뉴가 보이는 문제</b>
    </summary>
<br>    해결: 페이지 로드 시 href 값 비교를 통해 로그인, 회원가입 페이지라면 해당 태그를 display:none으로 설정해 안보이게 함.

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
