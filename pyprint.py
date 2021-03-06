import os.path
import tkinter as tk
from tkinter import ttk

from pyprint.menubars import PyPrintMenus
from pyprint.serialsettings import Serial_Settings
from pyprint.printingtabs import Printing_Tabs
from pyprint.printbuttons import PrintButtons

class Pyprint(tk.Tk):
    def __init__(self):
        super().__init__()
        self.icon_path = os.path.join('.', 'printer.ico')
        self.option_add('*tearOff', tk.FALSE)


        self.title("PyPrint")
        self.columnconfigure(0, weight=1)
        self.resizable(False, False)

        menubar = PyPrintMenus(self)
        self.iconbitmap(self.icon_path)

        self.config(menu=menubar)


class MainFrame(ttk.Frame):
    def __init__(self, root, **kwargs):
        super().__init__(root, padding="1 1 1 1")

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.grid(kwargs)

        self.combo_frame = Serial_Settings(self, column=0, row=0,  sticky=(tk.W), padx=10)
        self.action_buttons = PrintButtons(self, column=1, row=0, sticky=(tk.N, tk.E, tk.S, tk.W), padx=10)
        self.action_buttons.bind_buttons(self.print_it, self.clear)
        self.tabs = Printing_Tabs(self, column=0, row=1, columnspan=2, padx=10, pady=10)

        coms_detected = self.check_coms()

        if (coms_detected):
            root.bind('<F1>', self.print_it)

        root.bind('<Control-q>', exit)
        root.bind('<Control-Q>', exit)

    def print_it(self):
        print("Printing")
        text_to_print = self.tabs.Get_Text_Input()
        com = self.combo_frame.com_combobox.get()
        baud = self.combo_frame.baud_combobox.get()

        print(baud)
        
        if len(text_to_print) > 0:
            print(text_to_print, com, baud)

    def clear(self):
        print("Clearing Text")
        self.tabs.Clear_Text()

    def check_coms(self):
        if self.combo_frame.active_coms:
                print(list(com.device for com in self.combo_frame.active_coms))
                return True
        else:
                self.action_buttons.print_button.configure(state="disabled")
                return False




#### Main ####

if __name__ == "__main__":
    pyPrint = Pyprint()
    mainFrame = MainFrame(pyPrint, column=0, row=0, sticky=(tk.N, tk.E, tk.S, tk.W))
    pyPrint.mainloop()