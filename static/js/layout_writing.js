function imgToBase64ByFileReader(url) {
    return new Promise((resolve, reject) => {
        let xhr = new XMLHttpRequest();
        xhr.onload = () => {
            let reader = new FileReader();
            reader.onloadend = function () {
                resolve(reader.result);
                document.getElementById('cafe-image').setAttribute('src', reader.result);
            }
            reader.readAsDataURL(xhr.response);
        }
        xhr.open('GET', url);
        xhr.responseType = 'blob';
        xhr.send();
    });
}

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

function checkwrite() { // 글 저장을 위한 예외처리
    if ($('#cafe-image').attr("src") == "") {
        return false;
    } else if ($('#cafeName').val() == "") {
        return false;
    } else if ($('#cafeAddress').val() == "") {
        return false;
    } else if ($('#cafeComent').val() == "") {
        return false;
    } else {
        return true;
    }
}

function writing() {
    if (checkwrite()) {
        $.ajax({
            type: "POST",
            url: "/api/writing",
            data: {
                writer_name: "yse09@kakao.com",
                cafe_name: $('#cafeName').val(),
                cafe_address: $('#cafeAddress').val(),
                cafe_coment: $('#cafeComent').val(),
                cafe_img: $('#cafe-image').attr("src")
            },
            success: function (response) {
                alert(response["msg"]);
                window.location.replace('/'); //메인 페이지로 리다이렉트
            }
        })
    } else {
        alert("사진, 이름, 주소, 코멘트를 빠짐없이 작성해 주세요."); //예외 사항을 사용자에게 알림
    }
}
