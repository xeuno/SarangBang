//1.입력받으면 입력값 초기화
//2. 입력값 댓글로들어가기
//3. 댓글 삭제, 수정기능
//4. 타임스템프기능
const rootDiv = document.getElementById("userment-list");
const mainCommentCount = document.querySelector('#count');
let user_id = "";

$(document).ready(function () {
    user_id = getCurrentUserID(); //현재 접속해있는 유저의 아이디 값 가져오기
});

function getCurrentUserID() {
    $.ajax({
        type: "GET",
        url: "/api/getid",
        data: {},
        success: function (response) {
            if (response['user_id'] !== null) {
                user_id = response['user_id'];
            } else {
                alert(response['msg']);
            }
        }
    });
}

//타임스템프 만들기
function generateTime() {
    let date = new Date();
    const dateString = date.toISOString();
    const dateToString = dateString.substring(0, 10) + " " + dateString.substring(11, 19);
    return dateToString
}

function deleteComments(event) {
    const list = event.parentNode.parentNode;

    rootDiv.removeChild(list);
    //메인댓글 카운트 줄이기.
    if (mainCommentCount.innerText <= '0') {
        mainCommentCount.innerText = 0;
    } else {
        mainCommentCount.innerText = parseInt(mainCommentCount.innerText) - 1;
    }

    delUserMent(list); //DB에서 댓글 지우기
}

function saveUserMent() {
    let writer_name = document.getElementById('writer-show').innerText; // 글 작성자 아이디
    let cafe_name = document.getElementById('name-show').innerText;
    let user_ment_dict = {}

    user_ment_dict['user_name'] = user_id; // 현재 댓글 작성자 아이디..헷갈림 주의
    user_ment_dict['ment'] = document.getElementsByClassName('inputValue')[0].innerText;
    user_ment_dict['date'] = document.getElementsByClassName('time')[0].innerText;

    $.ajax({
        type: "POST",
        url: "/api/userment",
        data: {
            writer_name: writer_name,
            cafe_name: cafe_name,
            ment: JSON.stringify(user_ment_dict)
        },
        success: function (response) {
        }
    })
}

function delUserMent(obj) {
    let writer_name = document.getElementById('writer-show').innerText;
    let cafe_name = document.getElementById('name-show').innerText;
    let user_ment_dict = {}

    console.log(obj);
    user_ment_dict['user_name'] = user_id;
    user_ment_dict['ment'] = obj.getElementsByClassName('inputValue')[0].innerText;
    user_ment_dict['date'] = obj.getElementsByClassName('time')[0].innerText;

    $.ajax({
        type: "POST",
        url: "/api/delment",
        data: {
            writer_name: writer_name,
            cafe_name: cafe_name,
            ment: JSON.stringify(user_ment_dict)
        },
        success: function (response) {
        }
    })
}

//댓글보여주기
function showComment(comment) {
    const userName = document.createElement('div');
    const inputValue = document.createElement('span');
    const showTime = document.createElement('div');
    const countSpan = document.createElement('span')
    const commentList = document.createElement('div');  //이놈이 스코프 밖으로 나가는 순간 하나지우면 다 지워지고 입력하면 리스트 다불러옴.

    //삭제버튼 만들기
    const delBtn = document.createElement('button');
    delBtn.className = "deleteComment";
    delBtn.innerText = "삭제";

    commentList.className = "eachComment";
    userName.className = "name";
    inputValue.className = "inputValue";
    showTime.className = "time";

    //유저네임가져오기
    userName.innerText = user_id;//사용자 이름 표시
    userName.appendChild(delBtn);

    //입력값 넘기기
    inputValue.innerText = comment;

    //타임스템프찍기
    showTime.innerText = generateTime();
    countSpan.innerText = 0;

    //댓글뿌려주기
    commentList.appendChild(userName);
    commentList.appendChild(inputValue);
    commentList.appendChild(showTime);
    rootDiv.prepend(commentList);

    delBtn.addEventListener("click", ()=>{deleteComments(delBtn)});

    saveUserMent();
}

//버튼만들기+입력값 전달
function pressBtn() {
    const currentVal = document.getElementById("userment-input");

    if (!currentVal.value.length) {
        alert("댓글을 입력해주세요!!");
    } else {
        showComment(currentVal.value);
        mainCommentCount.innerText = parseInt(mainCommentCount.innerText) + 1;
        currentVal.value = null;
    }
}
