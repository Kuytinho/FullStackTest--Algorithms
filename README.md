# Desafio de Algoritmos e Estrutura de Dados

Este é um desafio de implementação de algoritmos e estruturas de dados, focado em um problema específico: circular partículas em um ciclotron.

## Descrição do Problema

O objetivo é implementar uma função chamada `cyclotron` que recebe dois parâmetros: a partícula (e, p ou n) e o tamanho da matriz. A função deve retornar uma matriz que representa o estado do ciclotron após a aceleração da partícula especificada.

As partículas podem ser aceleradas de maneiras diferentes, conforme definido nos requisitos do desafio. A função deve lidar com casos de matrizes de diferentes tamanhos (4x4, 5x5, etc.) e produzir o resultado esperado para cada caso.

## Instruções de Uso

1. Clone este repositório em sua máquina.

2. Certifique-se de ter o Python instalado.

3. Navegue até o diretório raiz do projeto.

4. Execute o arquivo de teste `test_cyclotron.py` para verificar se a função `cyclotron` está funcionando corretamente. Use o seguinte comando:

´python3 -m unittest test_cyclotron.py´


A saída do teste mostrará se a função está produzindo os resultados esperados.

5. Você também pode executar o exemplo de uso da função `cyclotron` no arquivo `main.py`. Use o seguinte comando:

python3 cyclotron.py


Isso executará o exemplo e mostrará a saída no terminal.

## Detalhes da Implementação

A função `cyclotron` foi implementada no arquivo `cyclotron.py`. Ela segue uma abordagem baseada em condicionais para lidar com as diferentes partículas e seus padrões de aceleração. A função utiliza uma matriz para representar o estado do ciclotron, preenchendo as células conforme as especificações do desafio.

## Autor

Lucas Carvalho de Medeiros

---

Este é um desafio proposto por [Lexart Labs](https://www.lexartlabs.com) para avaliar habilidades em algoritmos e estruturas de dados.

