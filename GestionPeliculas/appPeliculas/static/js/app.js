


/**Function eliminarPelicula(id) description...
 * funcion que verifica si desea eliminar una película segun id escogido
 *
 * @param {*} id - El identificador de la película a eliminar.
 */ 
function eliminarPelicula(id){
    Swal.fire
    ({
        title: "Esta seguro de eliminar la película?",
        showDenyButton: true,
        confirmButtonText: "SI",
        denyButtonText: "NO" 
    }).then((result)=>{
        if(result.isConfirmed){
            location.href = "/eliminarPelicula/" + id;
        }
    });
}

function mostrarImagen(evento){
    alert("sadasd")
    // Obtener el archivo de la entrada de archivo
   const imagenPelicula = document.querySelector("#imagenPelicula");
   const files = evento.target.files;
   const archivo = files[0];
   const url = URL.createObjectURL(archivo);
    // Establecer la URL de la imagen en el elemento de imagen
    let filename = archivo.name;
    let extension = filename.split('.').pop();
    extension = extension.toLowerCase();
    if(extension !== "jpg" && extension !== "jpeg" && extension !== "png"){
        fileFoto.value = "";
        Swal.fire("seleccionar","la imagen debe ser jpg, jpeg o png","error");
    } else {
        imagenPelicula.setAttribute("src", url);
    }
}