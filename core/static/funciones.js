

function validarNombre(input){
        var dato = document.querySelector(input);
        if(dato.value.length >= 3 && dato.value.length <= 20){
            dato.classList.remove("error");
            
        }else{
            dato.classList.add("error");
            
        }
}   

function validarContraseña(input){
    var dato = document.querySelector(input);
    if(dato.value.length >= 3 && dato.value.length <= 20){
        dato.classList.remove("error");
        
    }else{
        dato.classList.add("error");
        
    }
}   
      
