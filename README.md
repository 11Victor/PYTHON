# Engenharia da Computação
<img src="https://www.python.org/static/img/python-logo.png">
<p>Universidade Anhembi Morumbi</p>
<p>Disciplina: Técnicas de Programação</p>
<p>Professor: André Santana</p>
<p>Aluno: Victor Valencio</p>

<br>
<p></p>

## Atividade N1
<p>Situação Problema<br>
Muitos jogos de RPG são baseados em explorar dungeons, ou seja, explorar cavernas, calabouços, florestas e todo tipo de lugar desconhecido.
Hoje você será o líder de uma guilda de heróis!</p>
<p>As regras para a travessia do labirinto são bastante simples. Toda a guilda começará na sala 1 e a partir dela pode-se escolher 2 opções diferentes:<br>
⦁	1 – Caminho vermelho (ou direita);<br>
⦁	2 – Caminho preto (ou esquerda);<br>
Você precisará criar a lógica para fazer com que por meio de interações com o usuário seja possível avançar pelos caminhos do labirinto. Considere que “o mapa” oculto é idêntico a este:</p>
<div align="center">
<img src="https://i.imgur.com/a0vzbLD.png">
</div>

<p>Note que o caminho preto da sala 8 leva à um local desconhecido, isso porque esta dungeon é controlada por criaturas místicas que dominam o tempo-espaço e criaram um portal! Toda vez que os personagens escolherem o caminho preto estando na sala 8 é preciso sortear o seu destino.</p>
<p>Podendo ser qualquer sala entre 1, 2, 3, 4 ou 5.
O seu programa deve fazer com que a guilda inicie na sala 1 e possa escolher entre o caminho vermelho e preto na estrutura indicada anteriormente. Ele deverá funcionar todo em console, não é preciso criar nenhum tipo de gráfico.
</p>
<p>Algumas regras que precisam ser implementadas:<br>
⦁	Os heróis vencem ao chegar na Sala 9;<br>
⦁	A sala 6 tem realmente uma única possibilidade;<br>
⦁	Os heróis perdem se levarem 7 ou mais interações para chegarem na sala 9;<br>
⦁	Cada vez que os heróis escolhem um caminho é considerado 1 interação.<br>
⦁	Você precisa utilizar um laço de repetição, podendo ser o comando “while”;<br>
⦁	Dentro do laço de repetição você poderá incluir somente UM BLOCO de comando “if” (com direito a um elif e um else, mas sem outros ifs internos) e NENHUM comando “switch-case” (os demais comandos não possuem limitação);<br>
⦁	Não pode usar nenhum if disfarçado de while.<br>
⦁	Fora do laço de repetição você poderá utilizar quantos comandos precisar.
</p>
<p></p>


