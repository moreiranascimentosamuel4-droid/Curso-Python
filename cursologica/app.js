let titulo = document.querySelector('h1');
titulo.innerHTML = 'Jogo do número secreto';

let escolha = document.querySelector('p');
escolha.innerHTML = 'Escolha um numero entre 1 e 100';

let botao = document.querySelector('#btn');
botao.addEventListener('click', verificarNumero);

let numero = document.querySelector('#numero');

// criar número secreto       
let numero_secreto = Math.floor(Math.random( )* 100 ) +1;
let tentativas = 0;
function verificarNumero() {
    let numeroUsuario = Number(input.value);
    tentativas++;

    if (!numeroUsuario) {
        texto.innerHTML = 'Digite um número válido!';
        return;
    }
}

while (tentativas <= 3){
if (numero_secreto == numero){
let acertou = document.querySelector('#resultado');
acertou.innerHTML = 'Você acertou, meus parabéns!!!'
}else{
let errou = document.querySelector('#resultado')
errou.innerHTML = 'Você errou tente novamente'
tentativas ++;
}
}