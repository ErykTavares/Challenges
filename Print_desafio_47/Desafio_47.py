import PySimpleGUI as sg 
import pyautogui as auto

class Window():
    def __init__(self):
        sg.theme("reddit")

        self.layout = [[sg.Button("Print", size=(6, 1)), sg.Exit()],
                [sg.Text(size=(10,0), font="Verdanabold", text_color="Black", key="-texto-")],
                [sg.Input("print_01", font="Verdanabold", size=(12, 0,), key="-name-")],
                [sg.FolderBrowse("Salvar",enable_events=True, key="-save-")]
        ]

        self.window =  sg.Window("Print", finalize=True, layout=self.layout)

        while True:
            self.event, self.values = self.window.read()
            if self.event in (sg.WIN_CLOSED, "Exit"):
                break
            if self.event == "Print":
                print = auto.screenshot()
            self.window["-texto-"].update("Print tirada!")
            if self.event == "-save-":

                print.save(self.values["-save-"] + "\\" + self.values["-name-"] + ".png")
                #print(str(self.values["-save-"]))
        self.window.close()
        
print = Window() 

# copyright FideumaEgua © 2021