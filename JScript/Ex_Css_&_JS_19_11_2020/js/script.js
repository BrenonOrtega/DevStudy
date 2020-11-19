function chamaAlerta(event){
    alert("teste");
    return false;
}

function setupBtn(){
    var button = document.getElementById("button1");
    button.onclick=chamaAlerta;
}