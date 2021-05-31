checkEnter = (e) => {
    if(e.keyCode == 13)
    {
        e.preventDefault();
    }
}   

removeIt = (e) => {
    e.target.parentElement.style.display = "none";
}

document.addEventListener("DOMContentLoaded", () => {
    const x = document.querySelector("#Main__content__create__input");
    x.onkeypress = checkEnter;
    
    const y = document.querySelector("#Message__remove");
    y.onclick = removeIt;
});