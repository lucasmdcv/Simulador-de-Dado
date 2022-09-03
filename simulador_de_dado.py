# Simulador de dado
# Simular o uso de um dado, gerando o valor de 1 até 6
from ast import Try
from logging import exception
import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDoDado()
            elif resposta =='não' or resposta == 'n':
                print('agradecemos sua participação!')    
            else:
                print('Favor digitar sim ou não')
        except:
            print('ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))
        
simulador = SimuladorDeDado()            
simulador.Iniciar()
