checkEnter = (e) => {
    if(e.keyCode == 13)
    {
        e.preventDefault();
    }
}   

document.addEventListener("DOMContentLoaded", () => {
    var x = document.querySelector("#Main__content__create__input");
    x.onkeypress = checkEnter;
});