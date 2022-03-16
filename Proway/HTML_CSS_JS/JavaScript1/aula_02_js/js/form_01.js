function validar_form(){
    console.clear()
    //captura de dados pelo ID
    let nome= document.getElementById("nome_visitante").value
    let idade= Number(document.getElementById("idade_visitante").value)
    let email= document.getElementById("email_visitante").value
    let sugestao= document.getElementById("sugestao").value
    let valido= true

    //validações
    
    if(nome.length < 3){
        console.error("O nome "+nome+" informado é muito curto, o tamanho mínimo é três caracteres")
        valido= false
    }

    if(nome.length > 30){
        console.warn("O nome "+nome+" informado é muito grande, tamanho máximo é de 30 caracteres")
        valido= false
    }
    
    if (idade < 18){
        console.error("Menor de idade não queremos aqui!")
        valido = false
    }

    if (! email.includes("@gmail")){
        console.error("Só aceitamos domínio Gmail!")
        valido= false
    }
    if(email.includes("@gmail")){
        console.log("O e-mail é do Gmail")
    }

    if(valido){
        enviar()
    }else{
        alert("Não foi possível enviar os dados, verifique no log e tente novamente")
    }

}

function enviar(){
    alert("Ok, tudo certo para enviar")
}
