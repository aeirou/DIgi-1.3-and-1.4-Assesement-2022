const nav = document.getElementById('nav')

window.addEventListener('scroll', function(){
    if(window.scrollY > 10){
        nav.classList.add('active')
    }else{
        nav.classList.remove('active')
    }
});