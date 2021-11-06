let id_check_result = null;

//배너에 있는 글쓰기, 로그아웃 버튼을 안보이게 하는 부분
window.addEventListener('load', function () {
    let sign_page = '/joinMembership';
    let now_href = location.pathname;
    let hide_gnb = document.querySelector('.gnb_list');
    let logo_center = document.querySelector('.nav');
    if (now_href === sign_page) {
        hide_gnb.style.display = 'none';
        logo_center.style.justifyContent = 'center';
    }
});

//비밀번호 형식이 맞는지 검사하는 함수
function check_pw() {
    var pw = document.getElementById('pw').value;

    if (pw.length < 8 || pw.length > 16) {
        alert('비밀번호는 8글자 이상, 16글자 이하만 이용 가능합니다.');
        document.getElementById('pw').value = '';
    }
    if (document.getElementById('pw').value != '' && document.getElementById('pw2').value != '') {
        if (document.getElementById('pw').value == document.getElementById('pw2').value) {
            document.getElementById('check').innerText = '비밀번호가 일치합니다.' //옆에 메세지를 띄우기 위해 inner를 썼다.
            document.getElementById('check').style.color = 'blue';
            document.getElementById('check').style.fontSize = '10px';

        } else {
            document.getElementById('check').innerText = '비밀번호가 일치하지 않습니다.';
            document.getElementById('check').style.color = 'red';
            document.getElementById('check').style.fontSize = '10px';
        }
    }
    var chk_num = pw.search(/[0-9]/g);
    var chk_eng = pw.search(/[a-zA-Z]/ig);
    if (chk_num < 0 || chk_eng < 0) {
        document.getElementById('check').innerText = '비밀번호는 숫자와 영문자를 혼용하여야 합니다.';
        document.getElementById('check').style.color = 'red';
        document.getElementById('check').style.fontSize = '10px';
        return false;
    }
}

function check_id_format(result) {
    var regExp = /^(?=.*[a-zA-Z])[-a-zA-Z0-9_.]{4,10}$/;
    return regExp.test(result);
}

//아이디 중복확인 검사하는 함수, 중복확인 버튼 클릭 시 호출.
function check_id() {
    const inputID = $('#id').val();

    if (inputID == "") {
        document.getElementById('idCheck').innerHTML = '아이디를 입력해주세요.'
        document.getElementById('icCheck').style.color = 'red';
        document.getElementById('idCheck').style.fontSize = '5px';
    } else if (!check_id_format(inputID)) {
        document.getElementById('idCheck').innerHTML = '아이디의 형식을 확인해주세요. 영문과 숫자, 일부 특수문자(._-) 사용 가능. 4-10자 길이'
        document.getElementById('icCheck').style.color = 'red';
        document.getElementById('idCheck').style.fontSize = '5px';
    } else {
        $.ajax({
            type: "POST",
            url: "/check_dup",
            data: {
                check_id: inputID
            },
            success: function (response) {
                if (response["msg"]) {
                    document.getElementById('idCheck').innerHTML = response["msg"]
                    document.getElementById('idCheck').style.color = 'blue'
                    document.getElementById('idCheck').style.fontSize = '5px';
                    id_check_result = inputID; // 검사를 한 ID 값을 저장해 둠
                    inputID.focus();
                } else {
                    document.getElementById('idCheck').innerHTML = response["exists"]
                    document.getElementById('idCheck').style.color = 'red'
                    document.getElementById('idCheck').style.fontSize = '5px';
                    inputID.focus();
                }
            }
        });

    }
}

//회원가입 버튼을 눌렀을 때 호출하는 함수.
function signup() {
    let user_id = $('#id').val();
    let user_password = $('#pw').val();
    let pw_check_result = document.getElementById('check').innerText;
    console.log(pw_check_result);

    if (user_id !== id_check_result) {
        alert("아이디 중복확인을 해주세요!");
    } else if (pw_check_result !== '비밀번호가 일치합니다.') {
        alert('비밀번호를 다시 확인해 주세요.');
    } else {
        $.ajax({
            type: "POST",
            url: "/signup",
            data: {
                user_id: user_id,
                user_password: user_password
            },
            success: function (response) {
                alert(response['msg']);
                window.location.replace('/');
            }
        });
    }
}