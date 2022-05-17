var imgLamp = document.getElementById('lamp');

function turnOnYellow(){
    var checkbox = document.getElementById('mylamp')
    if (checkbox.checked == true){
        imgLamp.setAttribute('src','img/lamp-on.png');
    }
    else
    {
        imgLamp.setAttribute('src','img/lamp.png');
    }
}

function turnOnBlue(){
    var checkbox = document.getElementById('mylamp1')
    if (checkbox.checked == true){
        imgLamp.setAttribute('src','img/lamp-on_blue.png');
    }
    else
    {
        imgLamp.setAttribute('src','img/lamp.png');
    }
}


