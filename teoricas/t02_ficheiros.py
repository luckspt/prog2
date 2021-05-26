#!/usr/bin/env python

"""
Universidade de Lisboa
Faculdade de Ciências
Departamento de Informática
Licenciatura em Tecnologias da Informação
2020/2021

Programação II

Manipulação de ficheiros via exemplos
"""

__author__ = "Vasco T. Vasconcelos"
__copyright__ = "Programação II, LTI, DI/FC/UL, 2021"                 "Faculdade de Ciências, Universidade de Lisboa", "2020/21"]
__email__ = "docentes-prog2-lti@listas.di.ciencias.ulisboa.pt"


# 1 _ Escrever

def escrever_ola():
    """Escrever 'olá' num ficheiro chamado 'ola.txt'"""
    f = open('ola.txt', 'w')
    f.write('olá\n')
    f.write('como vais?')
    f.close()

def escrever_primeiras_potencias(nome_ficheiro, quantas=10):
    """Escrever as 1as quantas potencias de 2, começando a contar de 1.

    Args:
        nome_ficheiro (str): O nome do ficheiro onde escrever
        quantas (int, optional): Quantas potencias vou escrever. Defaults to 10.
    """
    f = open(nome_ficheiro, 'w')
    i = 1
    for _ in range(quantas):
        f.write(str(i) + '\n')  # conversao int -> str
        i = i * 2
    f.close()


# 2 _ Ler

def ler_uma_linha():
    """Ler uma linha do ficheiro 'ola.txt'
    """
    f = open('ola.txt', 'r')
    linha = f.readline()
    f.close()
    print(linha)

def ler_e_imprimir(nome_ficheiro):
    """Imprimir o conteudo de um dado ficheiro

    Args:
        nome_ficheiro (str): O ficheiro de onde lemos
    """
    f = open(nome_ficheiro, 'r')
    for linha in f:
        print(linha, end='')
    f.close()

def somar(nome_ficheiro):
    """Somar os inteiros num ficheiro.
    Assume que cada linha contem um número inteiro.

    Args:
        nome_ficheiro (str): O ficheiro de onde lemos

    Returns:
        int: A soma dos inteiros
    """
    f = open(nome_ficheiro, 'r')
    soma = 0
    for linha in f:
        soma = soma + (int(linha))  # conversao str -> int
    f.close()
    return soma


# 3 _ A sintaxe with

# Problema: a) esquecer de fechar, b) excecao na manipulacao do ficheiro

def escrever_algo(algo):
    """Escrever algo no ficheiro 'algo.txt'

    Args:
        algo (any): O que queremos escrever no ficheiro
    """
    f = open('algo.txt', 'w')
    f.write(algo)
    f.close()
    # tentar com algo = 'olá' e algo = 56291

def escrever_algo_melhorado(algo):
    """Escrever algo no ficheiro 'algo.txt'

    Args:
        algo (any): O que queremos escrever no ficheiro
    """
    f = open('algo.txt', 'w')
    try:
        f.write(algo)
    finally:
        # Fechar o ficheiro quer haja excecao ou nao
        f.close()

def escrever_usando_with(algo):
    """Escrever algo no ficheiro 'algo.txt'

    Args:
        algo (any): O que queremos escrever no ficheiro
    """
    with open('algo.txt', 'w') as f:
        f.write(algo)

def contalinhas(nome_ficheiro):
    """Conta as linhas num dado ficheiro

    Args:
        nome_ficheiro (str): O nome do ficheiro

    Returns:
        int: O número de linhas no ficheiro
    """
    quantos = 0
    for _ in open(nome_ficheiro):
        quantos = quantos + 1
    return quantos

def copia_ficheiro(ficheiro_leitura, ficheiro_escrita): # with para 2 ficheiros
    """Copia o conteúdo de um dado ficheiro para outro

    Args:
        ficheiro_leitura (str): O ficheiro de leitura
        ficheiro_escrita (str): O ficheiro de escrita
    """
    with open(ficheiro_leitura, 'r') as de, open(ficheiro_escrita, 'w') as para:
        conteudo = de.read()
        para.write(conteudo)


# 4 _ Manipulação do conteúdo de um ficheiro

def conteudo(nome_ficheiro):
    """O conteúdo de um dado ficheiro

    Args:
        nome_ficheiro (str): O nome do ficheiro

    Returns:
        str: Uma string com o conteúdo do ficheiro
    """
    with open(nome_ficheiro, 'r') as f:
        return f.read()

def conteudo_por_linhas_com_newline(nome_ficheiro):
    """O conteúdo de um dado ficheiro

    Args:
        nome_ficheiro (str): O nome do ficheiro

    Returns:
        list[str]: Uma lista com as várias linhas do ficheiro, inclui o '\n' no fim
    """
    with open(nome_ficheiro, 'r') as f:
        return f.readlines()

def conteudo_por_linhas(nome_ficheiro):
    """O conteúdo de um dado ficheiro

    Args:
        nome_ficheiro (str): O nome do ficheiro

    Returns:
        list[str]: Uma lista com as várias linhas do ficheiro, sem o '\n' no fim
    """
    with open (nome_ficheiro, 'r') as f:
        return f.read().splitlines()

def numeros_num_ficheiro(nome_ficheiro):
    """O números contidos num dado ficheiro.
    Assume que cada linha contém um número.

    Args:
        nome_ficheiro (str): O nome do ficheiro

    Returns:
        list[int]: Uma lista com os números no ficheiro
    """
    with open(nome_ficheiro, 'r') as f:
        linhas = f.readlines()
    return [int(linha.rstrip()) for linha in linhas]
