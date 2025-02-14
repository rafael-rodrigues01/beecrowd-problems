Desafio 1222

quinta-feira, 30 de janeiro de 2025
17:06

Machado quer ser escritor. Ele escreveu muitos contos, resenhas de livros, relatos de viagens que fez e um pouco de romance. Agora Machado quer participar de um concurso de contos, que tem regras muito rígidas sobre o formato de inscrição. As regras do concurso limitam o número total de páginas e especificam o número máximo de caracteres por linha e o número máximo de linhas por página. Além disso, cada palavra deve ser escrita integralmente em uma linha (ou seja, uma palavra não pode ser separada em duas linhas). Machado quer escrever uma história com o máximo de palavras possível dentro das regras do concurso e precisa da sua ajuda. Dado o número máximo de caracteres por linha, o número máximo de linhas por página e as palavras do conto que Machado está escrevendo, ele quer saber o número mínimo de páginas que seu conto ocupará, considerando as regras do concurso. Entrada A primeira linha de um caso de teste contém três inteiros N (2 ≤ N ≤ 1000), L (1 ≤ L ≤ 30) e C (1 ≤ C ≤ 70), que indicam, respectivamente, o número de palavras do conto, o número máximo de linhas por página e o número máximo de caracteres por linha. O conto de Machado é inovador e não contém caracteres além de letras maiúsculas e minúsculas e espaços em branco. A segunda linha contém o conto de Machado, consistindo de N palavras (1 ≤ comprimento de cada palavra ≤ C) separadas por exatamente um espaço em branco. O fim da entrada é determinado por EOF. Saída Para cada caso de teste, seu programa deve gerar uma única linha contendo um único inteiro indicando o número mínimo de páginas que o conto ocupará, considerando as regras do concurso. Exemplo de entrada de amostra de saída 14 4 20 Se mana Piedade tem casado com Quincas Borba só me daria uma esperança colateral 16 3 30 No dia seguinte entrou a dizer de mim nomes feios e acabou me alcunhando Dom Casmurro 5 2 2 um de eu de o 5 2 2 a e eu o você 2 1 3 3

1   2     3      4     5       6     7    8  9    10 11 12 13 14 15 16     17 18 19    20

Se mana Piedade tem 
casado com Quincas Borba apenas me daria uma esperanca colateral

N = number of words 
L = maximun number of lines per page
C = maximun number of characters per line.


Cada página terá 4 linhas no primeiro exemplo então preciso descobrir o número mínimo de páginas que esse conto vai ter.

Primeiro exemplo:
N = 14 L = 4 C = 20 

1 página
Se mana Piedade tem 
casado com Quincas 
Borba apenas me 
daria uma esperanca 

2 página
Colateral

R= 2 páginas 


Segundo exemplo

N = 16 L = 3 C = 30

1 página
No dia seguinte entrou a dizer 
de mim nomes feios e acabou 
alcunhando me Dom Casmurro

R= 1 página

Third Example

N = 5 L = 2 C = 2 

1 página
a 
De

2 página
 i 
De

3 página
 o

R= 3 página

Fourth example

N = 5 L = 2 C = 2

1 página
A 
e 

2 página
i 
o 

3 página
U

R= 3 página

02/10/2025

Entendi que eu preciso gerar funções que geram palavras aleatórias exemplo:


  def random_word_generate(min_length = 3, max_length = 10):
    import random
    import string
    length = random.randint(min_length, max_length)
    return ''.join(random.choices(string.ascii_lowercase, k=length))

agora o que eu preciso fazer ?

Dado o número de palavras que o meu conto vai ter eu poderia usar esse número para percorrer um for e gerar o número de palavras correspondente. 

Blz e dai ?

Ah eu poderia usar o número máximo de caracteres para armazenar essas palavras em um array, usando a virgula como se fosse um espaço em branco, faz sentido ?

O que eu preciso ?

O que eu quero ?

Acho que preciso achar uma forma de juntar essas palavras contando os espaços sem atingir o número máximo de caracteres e quando der o número máximo de caracteres adicionar a página.

11/01/2025

Consegui encontrar uma forma de pegar os espaços em branco usando a concatenação de strings com espaço em branco dessa forma:

for i in range(n):
    words += random_word_generate() + '  '

Dessa forma eu usei a função len() e peguei o número de caracteres contando os espaços em branco

Agora só falta eu encontrar uma forma de evitar que a quebra seja no meio da palavra.

Você é um desenvolvedor de software Sênior e vai me ajudar com o seguinte problema.

Eu tenho uma seguência de palavras armazenadas em uma string que contém caracteres em branco, tenho o número máximo de caracteres que minha linha deve ter exemplo 14. o que eu queria saber é como eu poderia saber o momento de quebrar a linha de forma que cada palavra seja escrita integralmente em cada linha ?



