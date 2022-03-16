var nome_completo = "Martina Keunecke Beck"
var idade = 28
var endereco = "ali do lado, tres"
var cep = 00000-000
var telefone = 99999-0000
var email = "email@gmail.com"
var academica = "Tecnólogo em Fotografia"
var profissao = "Balconista - Adolfo Keunecke & Cia LTDA"

var titulo = document.createElement("h1")
titulo.textContent=nome_completo
document.body.append(titulo)
criar_linha()

criar_h2("Informação de Contato")
criar_paragrafo(telefone)
criar_paragrafo(email)
criar_paragrafo(endereco)

criar_linha()

criar_h2("Formação Academica")
criar_paragrafo(academica)

criar_linha()

criar_h2("Experiência Profissional")
criar_paragrafo(profissao)

function criar_linha(){
    var linha=document.createElement("hr")
    document.body.append(linha)
}

function criar_paragrafo(conteudo){
    var txt_paragrafo = document.createElement("p")
    txt_paragrafo.textContent=conteudo
    document.body.append(txt_paragrafo)
}

function criar_h2(texto){
    var txt_h2 = document.createElement("h2")
    txt_h2.textContent=texto
    document.body.append(txt_h2)
}



