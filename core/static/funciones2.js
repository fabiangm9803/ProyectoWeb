function validarNombre(input){
    var dato = document.querySelector(input);
    if(dato.value.length >= 3 && dato.value.length <= 15){
        dato.classList.remove("error");
    }else{
        dato.classList.add("error");
    }
}

function validarContraseña(input){
    var dato = document.querySelector(input);
    if(dato.value.length >= 8 && dato.value.length <=12){
        dato.classList.remove("error");
    }else{
        dato.classList.add("error");
    }
}

function validarCorreo(input){
    var dato = document.querySelector(input);
    if(dato.value.length >= 10 && dato.value.length <=30){
        dato.classList.remove("error");
    }else{
        dato.classList.add("error");
    }
}


