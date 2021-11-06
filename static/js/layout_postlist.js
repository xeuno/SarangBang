//검색 기능
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

//검색 버튼에 엔터 이벤트 감지!
let search_enter = document.querySelector('.searchBtn');
search_enter.addEventListener('keydown', function (e) {
    if (e.keyCode === 13) {
        e.preventDefault();
        post_filter();
    }
});