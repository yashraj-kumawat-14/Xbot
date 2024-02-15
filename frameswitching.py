from tkinter import *

class pageone(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = Label(self, text="pageone")
        label.pack()
        button = Button(self, text="press", command=lambda : controller.showpage(pagetwo))
        button.pack()

        
class pagetwo(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = Label(self, text="pagetwo")
        label.pack()
        button = Button(self, text="press", command=lambda : controller.showpage(pageone))
        button.pack()

class App(Tk):
    def __init__(self):
        super().__init__()
        frame = Frame(self, bg="yellow")
        frame.pack(fill=BOTH, expand=True)
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        pageclasses = (pageone, pagetwo)
        self.pageobj = {}
        for i in pageclasses:
            page = i(frame, self)
            self.pageobj[i]=page
            page.grid(row=0, column=0)
    def showpage(self, page):
        self.pageobj[page].tkraise()
        

if __name__ == "__main__":
    app = App()
    app.geometry("700x600")
    app.title("Yashraj")


