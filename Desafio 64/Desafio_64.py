import PySimpleGUI as sg
from models.caixa import caixa 

class Window():
    """Classe que representa a interface do programa"""
    def __init__(self):
        sg.theme("reddit")

        self.layout = [
                [sg.Text("Valor da compra", font="Verdanabold")],
                [sg.Input("0", size=(10, 0 ), key="-sale-")],
                [sg.Text("Valor do pagamento", font="Verdanabold" )],
                [sg.Input("0", size=(10, 0), key="-pay-")],
                [sg.Button("Calcular Troco",font="Verdanabold" , key="-calculo-"), sg.Exit(font="Verdanabold")],
                [sg.Output(size=(16, 7), font="Verdanabold", key="-output-")]
                ]

        self.window = sg.Window("Caixa", self.layout, size=(210, 300), finalize=True)
        while True:
            self.event, self.values = self.window.read()
            if self.event in (sg.WIN_CLOSED, "Exit"):
                break
            if self.event == "-calculo-":
                troco = caixa(int(self.values["-sale-"]), int(self.values["-pay-"]))
                for i in troco:
                    self.window["-output-"].update(print(i))
        self.window.close()

caixa = Window()

# copyright FideumaEgua © 2021