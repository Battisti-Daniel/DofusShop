function redirect(url) {
    window.location.href = url;
}

function icons() {
        const icons = document.querySelectorAll('.icon');

        icons.forEach(icon => {
            icon.addEventListener('click', () => {
                if(icon.classList.contains("selected")){
                    icon.classList.remove("selected")
                    search = document.getElementById("inputSearch")
                    search.setAttribute("value","")
                }else {
                    icons.forEach(otherIcon => {
                        otherIcon.classList.remove('selected');
                    });
                    icon.classList.add('selected');
                }
            });

        });

}

function searchBy(){
    const icons = document.querySelectorAll(".icon")
    icons.forEach(selected =>{
        if(selected.classList.contains("selected")){
            search = document.getElementById("inputSearch")
            search.setAttribute("value",selected.id)
        }
    })
}



icons();
