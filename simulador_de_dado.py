# Simulador de dado

import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = (
            "Você gostaria de gerar um novo valor para o dado? \nSim / Não: "
        )

        self.layout = [
            [sg.Text("Jogar o dado?")],
            [sg.Button('Sim'),sg.Button('Não')]
        ]

        

    def Iniciar(self):
        self.janela = sg.Window('Simulador de dado', layout=self.layout)

        self.eventos, self.valores = self.janela.Read()
        
        try:
            if self.eventos.lower() == "sim" or self.eventos.lower() == "s":
                self.GerarValorDoDado()
                print('\n')
            elif self.eventos.lower() == "não" or self.eventos.lower() == "n":
                print("Agredecemos a sua participação!")
            else:
                print("Favor digitr sim ou não")
        except:
            print("Algo de errado não esta certo")


    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simular = SimuladorDeDado()
simular.Iniciar()
