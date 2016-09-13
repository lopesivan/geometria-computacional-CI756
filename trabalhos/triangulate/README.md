# Introdução
O algoritmo **triangulate.py** executa a triangulação de polígonos.

# Observações


# Execução
>./triangulate.py

# Entrada de dados
O algoritmo recebe de entrada um número **n** de vértices, em seguida
as coordenadas **x** e **y** dos **n** vértices separados com espaço.
As coordenadas devem ser em sentido anti-horário.
## Exemplo
4<br />
1 20<br />
1 4<br />
15 4<br />
15 20<br />

# Saída de dados
A saída contém a entrada de dados, mais o número de triangulos que o 
polígono dado pelos vértices da entrada possui, mais os vértices de 
cada triangulo, seguido das faces contrárias de cada vértice, onde
0 é a face externa.

## Exemplo
4<br />
1 20<br />
1 4<br />
15 4<br />
15 20<br />
2<br />
1 2 4 2 0 0<br />
4 2 3 0 0 1<br />

# Bugs conhecidos
1. Caso a entrada seja dada no sentido horário, no caso da entrada de exemplo 
  seria: <br /> 
  4 <br />
  1 4 <br />
  1 20 <br />
  15 20 <br />
  15 4 <br />
  Então o algoritmo se torna imprevisível.
2. Foi testado com algumas instâncias, em alguns casos teve problema por causa 
  do número de vértices, o algoritmo que divide o polígono em sub-polígonos
  acusa erro porque faço referencia a um vértice que só existe se houver 
  3 vértices anteriores, assim, somente acima de 4 vértices que executa a
  função.

