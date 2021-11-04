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

function login_JWT() {
    let id_input = document.querySelector('#user_id').value;
    let pw_input = document.querySelector('#user_pw').value;
    if (id_input === "") {
        alert('아이디를 입력해 주세요')
    }
    if (pw_input === "") {
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
                $.cookie('mytoken', response['token']);
                window.location.replace("/")
            } else {
                alert(response['msg'])
            }
        }
    });
}

function logout() {
    $.removeCookie('mytoken');
    window.location.href = '/login'
}