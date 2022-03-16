
var usuarios = new Array
var token = 'a6f906ca1462ee35051d80e4f987172770c914e1dc10d9e32cd16e73dcb325ce'

$("#enviar").click(
    function(){
        let url = this.name
        $.ajax({
            url: url,
            type: 'get',
            success: function (retorno) {
                console.log(retorno.meta.pagination.pages)

                let paginas = retorno.meta.pagination.pages

                retorno.data.forEach(element => {
                    $("#lista").append($("<li></li>").text(element.name+","+element.email))                   
                });

                for(i = 2;i <= paginas;i++){
                    $.ajax({
                        url:url+"?page="+i,
                        type:"get",
                        success: function(retorno){
                            retorno.data.forEach(element => {
                                $("#lista").append($("<li></li>").text(element.name + ","+ element.email))
                            })
                        }
                    })
                }
                
            },
            error: function (erro) {
                console.error(erro)
            } 
        })
    }
)

$("#mandar").click(
    function () {

        let nome = $("#nome").val()
        let email = $("#email").val()
        let objeto = {
            name: nome,
            email: email,
            gender: "Male",
            status: "Active"
        }
        $.ajax(
            {
                url: this.name,
                type: "post",
                headers: {
                    'Accept': "application/json",
                    'Content-type': 'application/json',
                    'Authorization':'Bearer '+token
                },
                data:JSON.stringify(objeto),
                success:function(retorno){
                    alert("funcionou")
                },
                error: function(erro){ 
                    alert("errou")
                }
            }
        )

    }
)
