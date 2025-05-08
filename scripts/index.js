window.onload = function () {

    const catCol = document.getElementsByClassName("cat");
    const cats = Array.from(catCol);
    const dirs = document.getElementsByClassName("directory");
    const catList = document.querySelector(".cat-list");

    function clickScroll(eventObj) {
        let clicked = eventObj.target;
        let i = cats.indexOf(clicked);
        dirs[i].scrollIntoView(true);
    }

    catList.addEventListener("click", clickScroll);

    const toTop = document.querySelector(".to-top");

    toTop.addEventListener("click", function () {
        window.scrollTo(0, 0);
    });
}