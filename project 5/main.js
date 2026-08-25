function changeinnertext(element){
    if(element.innerText=='Login'){
        element.innerText='Logout';
    }
    else{
        element.innerText='Login';
    }
}

function showAlart(){
    alert('This button was clicked')
}

function remove(element){
    element.remove();
}
var x=3;
function addlikes(){
    let like=document.querySelector('#like');
    x++;
    like.innerText=x;
}

