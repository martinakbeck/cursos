var contador = 0

function calcular(){
    let formula = document.getElementById("formula").value
    if (formula ==""){
        alert("Não há fórmula para calcular")
        return
    }
    let resultado = eval(formula)
    document.getElementById("formula").value = resultado

    inserir_na_tabela(formula, resultado)


}

function reduzir_um_caractere(){
    let formula = document.getElementById("formula").value
    formula = formula.slice(0,-1)
    document.getElementById("formula").value = formula
}

function injetar_texto(botao){
    let simbolo = botao.value
    let formula = document.getElementById("formula").value
    document.getElementById("formula").value += simbolo

}

function inserir_na_tabela(str_formula, num_resultado){
    let linha = document.createElement("tr")
    let coluna_execucao = document.createElement("td")
    contador = contador + 1
    coluna_execucao.textContent = contador
    linha.append(coluna_execucao)

    let coluna_formula = document.createElement("td")
    coluna_formula.textContent = str_formula
    linha.append(coluna_formula)

    let coluna_resultado = document.createElement("td")
    coluna_resultado.textContent = num_resultado
    linha.append(coluna_resultado)

    let conteudo = document.getElementById("historico")
    conteudo.append(linha)

    
}