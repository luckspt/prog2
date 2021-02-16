#1 - Identifique o resultado de cada um dos seguintes excertos de código asumindo que o conteúdo do ficheiro frutas.txt é:
#   a)
def um_a():
    in_file = open('frutas.txt', 'r')
    indata = in_file.read()
    print(indata)

#   b)
def um_b():
    in_file = open("frutas.txt",'r')
    indata = in_file.readline()
    print(indata)

#   c)
def um_c():
    in_file = open("frutas.txt",'r')
    indata = in_file.readlines()
    print(indata)

#   d)
def um_d():
    in_file = open("frutas.txt",'r')
    indata = list(in_file)
    print(indata)

#   e)
def um_e():
    in_file = open("frutas.txt",'r')
    for i in range(5):
        print(in_file.readline())

#2 - Escreva uma função le_ficheiro que leia um ficheiro de texto linha a linha e escreva o seu conteúdo no ecrã.
def le_ficheiro(caminho):
    with open(caminho) as f:
        print(''.join(f.readlines()))

#3 - Modifique a função da alínea anterior de forma a aparecer também o número de cada linha.
def le_ficheiro_com_linha(caminho):
    with open(caminho) as f:
        for i, linha in enumerate(f):
            print(f'{i} : {linha}', end='')

#4 - Escreva uma função escreve_ficheiro que peça ao utilizador várias linhas e as escreva num ficheiro. O programa termina quando o utilizador introduzir uma linha vazia.
def escreve_ficheiro(caminho):
    with open(caminho, 'w') as f:
        print('Insira as linhas:')
        while True:
            inp = input()
            
            if not inp:
                return
            f.write(f'{inp}\n')

#5 - Escreva uma função conta_linhas que dado um nome de ficheiro, abra este ficheiro e conte o número de linhas de texto que contém.
def conta_linhas(caminho):
    with open(caminho) as f:
        return len(f.readlines())

#6 - Escreva uma função conta_linhas_com_string que dado um nome de ficheiro e uma string, conte o número de linhas que contém essa string
def conta_linhas_com_string(caminho, query):
    with open(caminho) as f:
        return len([False for linha in f if (query in linha)])

#7 - Escreva uma função conta_linhas_caracteres que dado um nome de ficheiro, devolva um par com o número de linhas e o número de caracteres.
def conta_linhas_caracteres(caminho):
    with open(caminho) as f:
        chrs = 0
        lins = 0
        for linha in f:
            chrs += len(linha)
            lins += 1
        return (lins, chrs)

#8 - Escreva uma função copia_ficheiro que dado um nome de ficheiro e uma string, faz uma cópia do ficheiro para um novo ficheiro com o nome da string.
def copia_ficheiro(de, para):
    with open(de, "r") as d, open(para, "w") as p:
        p.write(d.read())

#9 - Escreva uma função lista_floats que dada uma lista de strings, cada uma representando um número, devolve uma outra lista com osnúmeros em vírgula flutuante correspondentes. Verifique que a função levanta a exceção ValueError quando pelo menos um elemento da lista não for convertível para float. Exemplos:
#Exemplos:
"""
    >>> lista_floats(['3.14', '1', '-0.4'])
    [3.14, 1.0, -0.4]
    >>> lista_floats(['3.14', 'um', '-0.4'])
    ...
    ValueError: could not convert string to float: 'um'
"""
def lista_floats(lista):
    return [float(num) for num in lista]

#10 -  Escreva uma função media que calcula a média de uma lista de números. Verifique que a função levanta a exceção ZeroDivisionError quando a lista estiver vazia.
#Exemplos:
"""
    >>> l = [1, 2.0]; media(l)
    1.5
    >>> l = []; media(l)
    ...
    ZeroDivisionError: integer division or modulo by zero
"""
def media(nums):
    if len(nums) == 0:
        raise ZeroDivisionError("A lista não pode estar vazia.")
    else:
        return sum(nums)/len(nums)

#11 - Dados referentes a observações são frequentemente guardados em ficheiros de texto. Por exemplo, as temperaturas lidas a várias horas do dia, ao longo de vários dias, podem ser guardadas num ficheiro de números em vírgula flutuante, onde cada linha contém os valores das várias temperaturas medidas num dia.
"""
    5.6 7.8 11.7 12.6 9.3 7.3
    6.7 8.5 11.6 11.6 9.4 7.0
    5.4 7.2 10.5 11.1 10.0 8.3
"""
# Utilizando as funções lista_floats e media dos exercícios anteriores, escreva uma função imprime_medias que, dado o nome de um ficheiro de texto como o acima, imprima as temperaturas médias diárias. Deverá imprimir um valor por linha e tantos valores quantas as linhas do ficheiro. Sugestão: utilize o método string.split(s) para obter a lista de palavras existentes numa string.
# A função imprime_medias deve apanhar as exceções lançadas pelas funções lista_floats e media. No caso de divisão por zero deverá mprimir "linhavazia"; no caso de uma linha que contenha uma palavra que não representa um número em vírgula flutuante deverá imprimir "linha mal formada".
# Uma das pré-condições da função imprime_medias é que o nome do ficheiro argumento representa um ficheiro válido, um ficheiro que pode ser aberto para leitura sem levantar exceção alguma.
#   a) Escreva a função imprime_medias que imprima algo (a média ou uma mensagem de erro) para cada linha no ficheiro. Utilize o comando with
def imprime_medias(caminho):
    with open(caminho) as f:
        for linha in f:
            try:
                print(round(media(lista_floats([num for num in linha[:-1].split(' ') if num])), 2))
            except ZeroDivisionError:
                print('linha vazia')
            except ValueError:
                print('linha mal formada')
#   b) Adapte a versão da alínea anterior de modo a que a função pare ao primeiro erro, depois de escrever a mensagem de erro adequada.
def imprime_medias_stop(caminho):
    with open(caminho) as f:
        for linha in f:
            try:
                print(round(media(lista_floats([num for num in linha[:-1].split(' ') if num])), 2))
            except ZeroDivisionError:
                print('linha vazia')
                return
            except ValueError:
                print('linha mal formada')
                return

#13 - Por vezes os ficheiros de observações trazem informação sobre os dado sna forma de linhas comentadas, cada qual iniciada pelo carater cardinal #. Eis um exemplo:
"""
# Localização: Observatório de Muge
# 14/2/20165.6
7.8 11.7 12.6 9.3 7.3
# 15/2/2016
6.7 8.5 11.6 11.6 9.4 7.0
# 16/2/2016
5.4 7.2 10.5 11.1 10.0 8.3
"""
#Escreva uma função salta_comentario que, dado um ficheiro aberto para leitura, devolva a primeira linha que não está comentada.
def salta_comentario(ficheiro):
    for linha in ficheiro:
        if len(linha) and linha[0] != '#':
            return linha
    return None

#14 - Usando a função salta_comentario, altere a função imprime_medias do exercício 11, de modo a ignorar linhas comentadas no ficheiro. Apelide-a de medias_salta_comentario.
def medias_salta_comentario(caminho):
    with open(caminho) as f:
        linha = salta_comentario(f)
        while linha:
            try:
                print(round(media(lista_floats([num for num in linha.strip().split(' ') if num])), 2))
            except ZeroDivisionError:
                print('linha vazia')
            except ValueError:
                print('linha mal formada')
            finally:
                linha = salta_comentario(f)