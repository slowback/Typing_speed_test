from doctest import master
from email import message
from tkinter import *
from run_page import RunPage


class App():
    def __init__(self):
        self.master = Tk()
        self.master.iconphoto(False, PhotoImage(file='keyboard.png'))
        self.master.title('Typeing Games')
        self.master.geometry('500x250')
        self.master.resizable(False, False)
        
        frame = Frame(self.master)
        frame.pack()

        self.title_label = Label(frame, text='Let Start ...', font=('Arial bold', 25))
        self.title_label.pack(pady=20, padx=20)

        self.go_button = Button(frame, text='GO', font=('Arial bold', 20), bg='blue', command=self.go_run)
        self.go_button.pack(pady=20, padx=20)

        self.master.mainloop()


    def go_run(self):
        self.master.destroy()
        RunPage()


    

if __name__ == '__main__':
    App()