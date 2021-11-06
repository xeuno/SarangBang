<h3 align="center"><b>항해99 1주차 4팀, 사랑방(SarangBang)</b></h3>

<h4 align="center">📆 2021.11.01 ~ 2021.11.06</h4>

---

<h3 align="center"><b>🛠 Tech Stack 🛠</b></h3>
</br>
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

<h3 align="center"><b>🎬 Getting Started 🎬</b></h3>
<pre>
<code>
~$ cd sarangbang
~$ pip install flask
~$ pip install mongo
~$ python3 app.py
</code>
</pre>

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
<h4 align="center"><b>📰 Login Page 📰</b></h4>

| Page Image | 설명 |
| ---------- | ---- |
| <img src="https://user-images.githubusercontent.com/57797592/140596100-f8e10ff7-e71e-4a21-acf0-1748f051e16f.png" width="700" /> | JWT 방식을 사용하여 로그인 기능을 구현하였습니다. |

---

<h4 align="center"><b>📰 Join Membership Page 📰</b></h4>

| Page Image | 설명 |
| ---------- | ---- |
| <img src="https://user-images.githubusercontent.com/57797592/140595222-87d5ae9b-fae4-4bb9-ba5d-36dd51098608.png" width="700" /> | 회원가입을 할 수 있는 페이지 입니다. |

---

<h4 align="center"><b>📰 Post Section Page 📰</b></h4>

| Page Image | 설명 |
| ---------- | ---- |
| <img src="https://user-images.githubusercontent.com/57797592/140595207-ad2c46ac-9250-409a-87b8-8016fbc4e0e4.png" width="700" /> | - 작성된 글 목록을 볼 수 있습니다! 글 목록은 Jinja 서버 사이드 렌더링으로 구현하여 빠른 페이지 로딩이 가능합니다. <br>- 포스트를 클릭하면 상세페이지로 이동할 수 있습니다. <br>- 헤더 부분의 로그아웃 버튼을 누르면 로그아웃이 가능합니다. <br>- 헤더 부분의 글쓰기 버튼을 누르면 글쓰기 페이지로 이동합니다. |

---

<h4 align="center"><b>📰 Post Writing Page 📰</b></h4>

| Page Image | 설명 |
| ---------- | ---- |
| <img src="https://user-images.githubusercontent.com/57797592/140595258-edc138c6-ea47-42fd-8d29-4e4f42ffcded.png" width="700" /> | - 파일 선택 버튼을 누르면 내 컴퓨터에 있는 이미지 파일을 로드할 수 있습니다. <br>- 카페 이름, 주소, 코멘트를 작성할 수 있습니다. <br>- 저장하기 버튼 클릭 시, DB에 글이 저장됩니다. 모든 입력란이 채워지지 않으면 글을 저장할 수 없습니다. |
| <img src="https://user-images.githubusercontent.com/57797592/140595293-fa8ab171-a978-40b9-9870-ff6ffaf16f8c.png" width="700" /> | 다 작성한 후 페이지의 모습입니다. |

---

<h4 align="center"><b>📰 Post Detail Page 📰</b></h4>

| Page Image | 설명 |
| ---------- | ---- |
| <img src="https://user-images.githubusercontent.com/57797592/140595299-67f2788c-4f39-4c55-89bf-a4a541ee19c1.png" width="700" /> | -클릭한 포스트의 정보들을 볼 수 있습니다. <br> - 댓글 작성 기능이 있어 댓글을 달 수 있고, 로그인한 ID로 작성했던 댓글들은 삭제할 수 있습니다. JWT 토큰을 이용해 사용자 검증을 하여 본인이 작성한 댓글에만 삭제 버튼이 보이도록 구현하였습니다. |

---

<h4 align="center"><b>👨🏻‍🤝‍👨🏻 Members 👨🏻‍🤝‍👨🏻</b></h4>
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

<h4 align="center"><b>✏ Review ✏</b></h4>
