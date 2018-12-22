Guia como usar/Descricao das classes:
@ parser.py - este arquivo esta desacoplado das demais classes;
- Sua função é transformar as instâncias para o padrão que o leitor suporta.
- Caso estejam várias instancias em um único arquivo elas são desmembradas, caso tenha apenas uma irá apenas remover os dados desnecessários como número de linhas/colunas ou strings.
## Para usar execute:
python parser.py diretorio_das_instancias

ex: python parser.py VLSI

@ app.py - Esta classe inicializa o programa, aqui é possivel definir os parâmetros do AG, como TAM_POP, MAX_GEN, TX_ELITE, TX_CROSS, TX_MUT, BLX_alpha. 
Para usar adicione o arquivo no diretorio "instancias" e execute

python app.py nome_do_arquivo

ex: python app.py W3.txt

@ BRKGA.py - Nesta classe está implementada a estrutura do AG, como funções de cruzamento, mutação, seleção roleta, avaliação aptidao, evolução da pop etc.
@ Dados.py - Nesta classe está implementado o leitor de arquivos
@ Decoder.py - Nesta classe está implementado o decoder de chaves aleatorias para o espaço do problema, os mecanismos de transposiçao de colunas, preprocessamento dos dados(preencher com 1) e avaliaçao da matriz proposta.
@ localsearch.py - Nesta classe estão implementadas algumas heuristicas de buscalocal, no momento estou utilizando a 2-opt, poderia rodar duas buscas locais, porém deixa um pouco pesado e não melhora tanto em relação as soluções encontradas
