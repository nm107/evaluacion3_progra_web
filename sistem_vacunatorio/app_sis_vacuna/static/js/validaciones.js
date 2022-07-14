function validacion_formulario_ingreso_persona() {
    console.log( "validacion_formulario_ingreso_persona")
    var rut = document.formulario_form.txt_rut.value
    var nombre = document.formulario_form.txt_nombre.value
    var ap_paterno = document.formulario_form.txt_appaterno.value
    var ap_materno = document.formulario_form.txt_apmaterno.value
    var edad = document.formulario_form.txt_edad.value

    if (rut.length > 9 && rut.length < 10 || rut.indexOf('-') < 0) {
        alert('el rut ingresado no es valido')
        console.log(rut + "rut")
        console.log(txt_rut + "txtrut")

        document.formulario_form.txt_rut.focus()
        return false
    }if (nombre.length == 0) {
    alert('Ingrese un nombre')
    document.formulario_form.txt_nombre.focus()
    return false
}if(ap_paterno.length == 0){
    alert('Ingrese su apellido paterno')
    document.formulario_form.txt_appaterno.focus()
    return false
}if(ap_materno.length == 0){
    alert('Ingrese su apellido materno')
    document.formulario_form.txt_apmaterno.focus()
    return false
}if(edad < 0 || edad > 100){
    alert('Ingrese una edad correcta')
    document.formulario_form.txt_edad.focus()
    return false
}else {
    alert('Persona Ingresada correctamente' +
    ' rut: ' + rut /*+ ' nombre: ' + nombre + ' telefono: ' + telefono*/)
document.formulario_form.submit() 
alert("Ingreso correcto")
}
}

/*function limpiar() {
    document.getElementById("txt_rut").value = "";
    document.getElementById("txt_nombre").value = "";
    document.getElementById("txt_telefono").value = "";
    document.getElementById("inputState").value = "";
    document.getElementById("floatingTextarea2").value = "";


}*/