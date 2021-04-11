import PySimpleGUI as sg


class Window():
        """Classe que representa a janela"""
        def __init__(self):
                """onde fica os principais atributos"""
                self.theme = sg.theme("Reddit")
                self.window_title = "Bloco de Notas"

                self.menu = [["Arquivo",["Abrir", "Salvar", "Sair"]],
                        ["tema", ["branco", "preto"]],   
                                ]

                self.layout = [
                        [sg.Menu(self.menu)],
                        [sg.Multiline(key="-text-", size=(50, 50), font="verdanabold", background_color="white")],
                ]

                self.window = sg.Window(title=self.window_title, size=(400, 400), resizable=True , finalize=True).layout(self.layout)
                self.window.read(timeout=1)
                #self.window.maximize()
                self.window["-text-"].expand(expand_x=True, expand_y=True)
                file = None
                while True:
                        self.event, self.values = self.window.read()
                        if self.event in (sg.WINDOW_CLOSED,"Sair"):
                                break
                        elif self.event == "Abrir":
                                try:
                                        file = str(sg.popup_get_file("Selecione o arquivo", file_types=(("Arquivo de texto", "*.txt*"),)))
                                        with open(file, "r") as f:
                                                        self.window["-text-"].update(f.read())
                                                        self.window.TKroot.title(self.window_title + "-" + f.name.split("/")[-1])
                                except FileNotFoundError:
                                        pass
                        elif self.event == "Salvar":
                                try:
                                        if not file:
                                                name = sg.popup_get_text("Nome do arquivo")
                                                folder = sg.popup_get_folder("Salvar onde")
                                                with open(folder + "\\" + name + ".txt", "a+") as f:
                                                        f.write(self.values["-text-"])
                                                        self.window.TKroot.title(self.window_title + "-" + f.name.split("\\")[-1])
                                                        
                                        else:
                                                with open(file, "w") as f:
                                                        f.write(self.values["-text-"])
                                except :
                                        pass
                        
                self.window.close()

note_pad = Window()
# copyright FideumaEgua © 2021