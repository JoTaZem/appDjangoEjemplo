
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