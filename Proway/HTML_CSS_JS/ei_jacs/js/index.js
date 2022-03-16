

$(".get").click(
    function (){
        $.ajax({
            url: this.value,
            type: "get",
            success: function (retorno) {
                console.log(retorno)
                console.warn(JSON.stringify(retorno))
            },
            error: function (erro) {
                console.error(erro)
            } 
        })
    }
)

$("#eco_get").click(
    function(){
        $.ajax({
            url:this.value,
            type:"get",
            success: function(retorno){
                console.log(retorno.args)
                console.warn(JSON.stringify(retorno.args))
            },
            error:function(erro){
                console.error(erro)
            }

        })
    }

)

$("#delay").click(
    function(){
        $.ajax(
            {
            url:this.name + $("#segundos").val(),
            type:"get",
            success: function(retorno){
                alert("Olhar console ")
                console.log(retorno)
            },
            error:function(erro){
                console.error(erro)
            }

        })

    }
)

$("#enviar").click(

    function(){
        let nome = $("#nome").val()
        let email = $("#email").val()

        let objeto = {
            apelido: nome,
            melhor_email: email
        }

        $.ajax({
            url: this.name,
            type: 'post',
            headers: {
                'Accept': "application/json",
                'Content-type': 'application/json',
            },
            data: JSON.stringify(objeto),
            success: function (retorno) {
                console.log(retorno.json)
            },
            error: function (erro) {
                console.error(erro)
            } 
        })
    }
)
       