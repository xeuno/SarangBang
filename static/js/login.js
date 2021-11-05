//로그인 페이지에서 배너에 로그아웃, 글쓰기 버튼 숨기기
window.addEventListener('load', function () {
    let login_page = '/login';
    let now_href = location.pathname;
    let hide_gnb = document.querySelector('.gnb_list');
    let logo_center = document.querySelector('.nav');
    if (now_href === login_page) {
        hide_gnb.style.display = 'none';
        logo_center.style.justifyContent = 'center';
    }
});

//토큰정보 얻어오기
function login_JWT() {
    let id_input = document.querySelector('#user_id').value;
    let pw_input = document.querySelector('#user_pw').value;

    if (id_input === "") {
        alert('아이디를 입력해 주세요')
    } else if (pw_input === "") {
        alert('비밀번호를 입력해 주세요')
    }

    $.ajax({
        type: "POST",
        url: "/api/login",
        data: {
            username_give: id_input,
            password_give: pw_input
        },
        success: function (response) {
            if (response['result'] === 'success') {
                $.cookie("mytoken", response['token']);
                window.location.replace("/")
            } else {
                alert(response['msg'])
            }

        }
    });

}

//로그아웃 시, 쿠키삭제, 로그인 페이지로 이동
function logout() {
    $.removeCookie('mytoken');
    window.location.href = '/login';
}

//회원가입 페이지로 이동
function join_membership() {
    window.location.href = '/joinMembership';
}

//로그인 버튼 엔터 이벤트 감지하면 로그인 되게!
let go_writing = document.querySelector('.go_main');
go_writing.addEventListener('keydown', function (e) {
    if (e.keyCode === 13) {
        e.preventDefault();
        login_JWT();
    }
});