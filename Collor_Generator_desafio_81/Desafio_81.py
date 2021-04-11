from random import randint
import PySimpleGUI as sg

class Window():
    def __init__(self):
        sg.theme("reddit")

        self.layout = [[sg.Text("Cores aleatorias", font="Verdanabold", key="-text-")],
                [sg.Text(" "), sg.Button("Gerar", font="Verdanabold")],
                [sg.Input(size=(10, 0), font="Verdanabold", change_submits=False , key="-input-")]
                      ]

        self.window = sg.Window("Gerador de cor", size=(150, 100)).layout(self.layout)

        while True:
            self.event, self.values =self.window.read()
            if self.event == sg.WIN_CLOSED:
                break
            if self.event == "Gerar":
                rgb, hex_color = self.random_color()
                self.window["-text-"].update(text_color=rgb)
                self.window["-input-"].update(hex_color)
                
        self.window.close()
    
    def random_color(self):
            """Gera uma cor aleatoria e retorna ela como rgb e hex"""
            self.rgb = [255, 255, 255]
            self.color = ""
            for color_number in self.rgb:
                self.color += str(randint(10, color_number))
            return "#" + self.color[0:6], "#" + str(hex(int(self.color)))[2:]

color_generator = Window()
# copyright ErykTavares © 2021