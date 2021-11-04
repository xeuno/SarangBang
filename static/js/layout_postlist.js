$(document).ready(function () {
    download_post();
});

function post_filter() {
    let search_keyword = document.getElementById("search").value.toLowerCase(); //소문자로 검색어 받아오기
    let postList = document.getElementsByClassName("card-box");

    for (let i = 0; i < postList.length; i++) {
        let postName = postList[i].getElementsByClassName('cafe-title');
        if (postName[0].innerText.toLowerCase().indexOf(search_keyword) != -1) {
            postList[i].style.display = "flex"
        } else {
            postList[i].style.display = "none"
        }
    }
}

function getCookie(name) {
  var value = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
  return value? value[2] : null;
}

function send_postData(obj) {
    let writerName = obj.getElementsByTagName("small")[0].innerText.split(" ")[1];
    let postName = obj.getElementsByTagName("h2")[0].innerText;

    sessionStorage.setItem(postName, writerName);
    location.href = "postview?" + "postname=" + postName;
}

// 서버에서 받아온 이미지를 띄우는 함수
function download_post() {
    $.ajax({
        type: "GET",
        url: "/api/postlist",
        data: {},
        success: function (response) { // 성공하면
            let datas = response['downlists'];
            for (let i = 0; i < datas.length; i++) {
                let writer_name = datas[i]['writer_name'];
                let cafe_name = datas[i]['cafe_name'];
                let cafe_address = datas[i]['cafe_address'];
                let cafe_coment = datas[i]['cafe_coment'];
                let cafe_img = datas[i]['cafe_img'];

                let tmp_html = `<div class="card-box" style="width: 600px" onclick="send_postData(this)">
                                        <div class="card">
                                            <img class="card-image" src=${cafe_img}>
                                            <div class="text" style="margin: 10px">
                                                <small>작성자: ${writer_name}</small>
                                                <h2 class="cafe-title">이름: ${cafe_name}</h2>
                                                <h3>${cafe_coment}</h3>
                                                <small>주소: ${cafe_address}</small>
                                            </div>
                                        </div>
                                    </div>`;

                // div에 새 이미지 추가
                $('#card-list').append(tmp_html);
            }
        }
    })
}