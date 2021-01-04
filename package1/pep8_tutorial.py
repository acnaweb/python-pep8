#!/usr/bin/env python
# coding: utf-8

# ## Tutorial PEP8 na prática
# ### Baseado em *https://realpython.com/python-pep8/*
# ### https://docs.python-guide.org/writing/structure/
# ### https://github.com/navdeep-G/samplemod

# functions: Use a lowercase word or words. Separate words by underscores to improve readability.
def imprimir_dados(par1):
    # constant: Use an uppercase single letter, word, or words. Separate words with underscores to improve readability.
    MY_CONSTANT = 123
    
    # variable: Use a lowercase single letter, word, or words. Separate words with underscores to improve readability.
    my_variable = "Exemplo de variavel"
    
    print(par1, MY_CONSTANT, my_variable, sep = "|")
    

# classes: Start each word with a capital letter. Do not separate words with underscores. This style is called camel case.
class MyClass:
    def __init__(self):
        pass

    def executar_segunda_func(self, par1):
        self.imprimir(par1, "par2")
    
    def imprimir(self, par1, par2):
        print(par1, par2, sep= " ")
        
    def somar(self, num1, num2):        
        # quebrar operacoes aritmeticas mantendo o operador no início da linha
        # usar parênteses em operacoes aritmeticas para permitir quebrar linha
        return (num1 
                + num2)

