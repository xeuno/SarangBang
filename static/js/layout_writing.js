function imgToBase64ByFileReader(url) {
    let reader = new FileReader();
    reader.onloadend = function () {
        console.log(reader.result)
        resolve(reader.result);
        console.log(reader.result)
        document.getElementById('img-id').setAttribute('src', reader.result);
    }
}

function loadFile(input) {
    let file = input.files[0]; //선택된 파일 가져오기

    let newImage = document.createElement("img"); //새 이미지 추가
    newImage.src = URL.createObjectURL(file); //이미지 source 가져오기
    newImage.id = "img-id"
    newImage.style.width = "100%";
    newImage.style.height = "100%";
    newImage.style.objectFit = "cover";

    //이미지를 image-show div에 추가
    let container = document.getElementById('image-show');
    container.appendChild(newImage);

    //이미지를 서버에 저장하기 위해 base64 형태로 변환
    imgToBase64ByFileReader(document.getElementById('img-id').getAttribute("src"));
}

function checkwrite() { // 글 저장을 위한 예외처리
    if ($('#img-id').attr("src") == "") {
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
                cafe_name: $('#cafeName').val(),
                cafe_address: $('#cafeAddress').val(),
                cafe_coment: $('#cafeComent').val(),
                cafe_img: $('#img-id').attr("src")
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

// 서버에서 받아온 이미지를 띄우는 함수
function download_img() {
    $.ajax({
        type: "GET",
        url: "/api/imgdown",
        data: {},
        success: function (response) { // 성공하면
            let dwnImg = response['downimg'];
            for (let i = 0; i < dwnImg.length; i++) {
                // 새 이미지 만들기
                let newImage = document.createElement("img");
                newImage.src = dwnImg[i]['cafe_img'];

                // div에 새 이미지 추가
                let container = document.getElementById('addimg');
                container.appendChild(newImage);
            }
        }
    })
}
