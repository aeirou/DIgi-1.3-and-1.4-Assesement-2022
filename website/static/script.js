const nav = document.getElementById('nav')

window.addEventListener('scroll', function(){
    if(window.scrollY > 700){
        nav.classList.add('active')
    }else{
        nav.classList.remove('active')
    }
});

setTimeout(function() {
    Alert.getOrCreateInstance(document.querySelector(".flashes")).close();
  }, 3000)