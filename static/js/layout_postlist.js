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

function send_postData(obj) {
    let writerName = obj.getElementsByTagName("small")[0].innerText.split(" ")[1];
    let postName = obj.getElementsByTagName("h2")[0].innerText;

    // sessionStorage.setItem(postName, writerName);
    // location.href = "postview?" + "postname=" + postName;
    showPost(postName, writerName);
}

function showPost(postName, writerName) {
    $.ajax({
        type: "POST",
        url: "/api/postdown",
        data: {
            writer_name: writerName,
            cafe_name: postName
        },
        success: function (response) {
            // const postName = response['downlists']['cafe_name'];
            // const postAddress = response['downlists']['cafe_address'];
            // const postComment = response['downlists']['cafe_coment'];
            // const postImage = response['downlists']['cafe_img'];
            // const ments = response['downlists']['user_mentlist'];
            //
            // document.getElementById('writer-show').append(writer_name);
            // document.getElementById('name-show').append(postName);
            // document.getElementById('address-show').append(postAddress);
            // document.getElementById('text-show').append(postComment);
            // document.getElementById("image-show").setAttribute("src", postImage);
            // showDBMents(ments);
            console.log(response);
        }
    });
}

let search_enter = document.querySelector('.searchBtn');
search_enter.addEventListener('keydown', function (e) {
    if (e.keyCode === 13) {
        e.preventDefault();
        post_filter();
    }
});