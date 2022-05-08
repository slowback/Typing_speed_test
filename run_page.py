import random
from tkinter import *
from timeit import default_timer as timer  
from tkinter import messagebox


SIMPLE_WORDS = """
    boy keep animal like like take really but do 
    almost can close walk end animal together they 
    life he men same into family look I seem down very eat water 
    it follow children hand earth high second saw were would show are 
    spell down your start food might different best little with men must 
    great four part his end never must I new will live now been while him did 
    then after few sun think only life far an I tree four on part such make carry made study last
""".split()


FONT = ('Arial', 16)


class RunPage():
    def __init__(self):
        self.word = None
        self.count_enter = False
        self.start_timer = 0
        self.end_timer = 0

        self.start_time()

        self.master = Tk()
        self.master.iconphoto(False, PhotoImage(file='keyboard.png'))
        self.set_window()
        frame = Frame(self.master)
        frame.grid()

        self.set_random_word()

        self.msg_label = Message(frame, text=self.word, font=FONT, width=100, background='yellow')
        self.msg_label.grid(column=2, row=1)

        self.enter_entry = Entry(frame, width=20, justify=CENTER, font=('Arial', 12))
        self.enter_entry.grid(column=2, row=3)
        self.enter_entry.bind('<Return>', self.check_result)
        self.enter_entry.focus_force()

        self.time_label = Label(frame, text='Time', font=FONT)
        self.time_label.grid(column=0, row=5)

        self.done_button = Button(frame, text='Up Skill', font=('Arial', 14), command=self.up_skill, background='cyan')
        self.done_button.grid(column=0, row=7)

        self.tryagin_button = Button(frame, text='Try Again', font=('Arial', 14), command=self.try_agin, background='#F39C12')
        self.tryagin_button.grid(column=2, row=7)

        self.close_button = Button(frame, text='Close', font=('Arial', 14), command=self.master.destroy, background='#E74C3C')
        self.close_button.grid(column=4, row=7)

        self.var_timer = StringVar()
        self.show_timer_label = Label(frame, textvariable=self.var_timer, font=('Arial', 16))
        self.show_timer_label.grid(column=2, row=5)

        # blank cols
        self.blank1 = Label(frame, width=3)
        self.blank1.grid(column=1, row=0)
        self.blank2 = Label(frame, width=3)
        self.blank2.grid(column=3, row=0)

        # blank row
        self.blank3 = Label(frame, width=3)
        self.blank3.grid(column=1, row=0)
        self.blank4 = Label(frame, width=3)
        self.blank4.grid(column=1, row=2)
        self.blank5 = Label(frame, width=3)
        self.blank5.grid(column=1, row=4)
        self.blank6 = Label(frame, width=3)
        self.blank6.grid(column=1, row=6)
        self.blank7 = Label(frame, width=3)
        self.blank7.grid(column=1, row=8)
        self.master.mainloop()

    def up_skill(self):
        self.master.destroy()
        UpSkill()

    def check_result(self, var):
        
        if not self.count_enter:
            input_word = self.enter_entry.get()
            self.end_time()
            self.var_timer.set(str(round(self.end_timer - self.start_timer, 2)) + ' second')
            self.show_timer_label.config(text=self.var_timer)

            if input_word != self.word:
                messagebox.showinfo('info', f'instead of \"{self.word}\" you typed \"{input_word}\".')
            self.count_enter = True

    def set_window(self):
        self.master.title('Typeing Games')
        self.master.geometry('420x250')
        self.master.resizable(False, False)

        self.master['padx'] = 10
        self.master['pady'] = 10

        self.master.columnconfigure(0, weight=2)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=2)
        self.master.columnconfigure(3, weight=1)
        self.master.columnconfigure(4, weight=2)

        self.master.rowconfigure(0, weight=1)    
        self.master.rowconfigure(1, weight=2)    
        self.master.rowconfigure(2, weight=1)    
        self.master.rowconfigure(3, weight=2)    
        self.master.rowconfigure(4, weight=1)    
        self.master.rowconfigure(5, weight=2)    
        self.master.rowconfigure(6, weight=1)    
        self.master.rowconfigure(7, weight=2)    
        self.master.rowconfigure(8, weight=1)    

    def start_time(self):
        self.start_timer = timer()

    def end_time(self):
        self.end_timer = timer()

    def try_agin(self):
        self.count_enter = False

        self.enter_entry.delete(0, END)
        self.var_timer.set('')
        self.set_random_word()

        self.msg_label.config(text=self.word)
        self.start_time()

    def set_random_word(self):
        self.word = random.choice(SIMPLE_WORDS)



class UpSkill(RunPage):
    def __init__(self):
        self.sentences = None
        self.count_enter = False
        self.start_timer = 0
        self.end_timer = 0

        self.start_time()

        self.master = Tk()
        self.master.iconphoto(False, PhotoImage(file='keyboard.png'))
        self.set_window()
        frame = Frame(self.master)
        frame.grid()

        self.set_random_word()

        self.msg = Message(frame, text=self.sentences, font=('Arial', 12), width=300, background='yellow')
        self.msg.grid(column=2, row=1, columnspan=3)

        self.enter_entry = Entry(frame, width=20, justify=CENTER, font=('Arial', 12))
        self.enter_entry.grid(column=2, row=3)
        self.enter_entry.bind('<Return>', self.check_result)
        self.enter_entry.focus_force()

        self.time_label = Label(frame, text='Time', font=FONT)
        self.time_label.grid(column=0, row=5)

        self.done_button = Button(frame, text='Down Skill', font=('Arial', 14), command=self.down_skill, background='#58D68D')
        self.done_button.grid(column=0, row=7)

        self.tryagin_button = Button(frame, text='Try Again', font=('Arial', 14), command=self.try_agin, background='#F39C12')
        self.tryagin_button.grid(column=2, row=7)

        self.close_button = Button(frame, text='Close', font=('Arial', 14), command=self.master.destroy, background='#E74C3C')
        self.close_button.grid(column=4, row=7)

        self.var_timer = StringVar()
        self.show_timer_label = Label(frame, textvariable=self.var_timer, font=('Arial', 16))
        self.show_timer_label.grid(column=2, row=5)

        # blank cols
        self.blank1 = Label(frame, width=3)
        self.blank1.grid(column=1, row=0)
        self.blank2 = Label(frame, width=3)
        self.blank2.grid(column=3, row=0)

        # blank row
        self.blank3 = Label(frame, width=3)
        self.blank3.grid(column=1, row=0)
        self.blank4 = Label(frame, width=3)
        self.blank4.grid(column=1, row=2)
        self.blank5 = Label(frame, width=3)
        self.blank5.grid(column=1, row=4)
        self.blank6 = Label(frame, width=3)
        self.blank6.grid(column=1, row=6)
        self.blank7 = Label(frame, width=3)
        self.blank7.grid(column=1, row=8)

        self.master.mainloop()


    def down_skill(self):
        self.master.destroy()
        RunPage()



    def check_result(self, var):
        
        if not self.count_enter:
            input_word = self.enter_entry.get()
            self.end_time()
            self.var_timer.set(str(round(self.end_timer - self.start_timer, 2)) + ' second')
            self.show_timer_label.config(text=self.var_timer)

            set_input_words = set(input_word.split())
            set_select_words = set(self.sentences.split())

            check_words = set_input_words ^ set_select_words
            
            if check_words:
                messagebox.showinfo('info', 'instead of:\n"{}"\nyou typed:\n"{}"'.format(set_select_words, set_input_words))
            self.count_enter = True


    def set_window(self):
        self.master.title('Typeing Games')
        self.master.geometry('500x300')
        self.master.resizable(False, False)

        self.master['padx'] = 10
        self.master['pady'] = 10

        self.master.columnconfigure(0, weight=2)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=3)
        self.master.columnconfigure(3, weight=1)
        self.master.columnconfigure(4, weight=2)

        self.master.rowconfigure(0, weight=1)    
        self.master.rowconfigure(1, weight=2)    
        self.master.rowconfigure(2, weight=2)    
        self.master.rowconfigure(3, weight=2)    
        self.master.rowconfigure(4, weight=1)    
        self.master.rowconfigure(5, weight=2)    
        self.master.rowconfigure(6, weight=1)    
        self.master.rowconfigure(7, weight=2)    
        self.master.rowconfigure(8, weight=1)    


    def start_time(self):
        self.start_timer = timer()

    def end_time(self):
        self.end_timer = timer()

    def try_agin(self):
        self.count_enter = False

        self.enter_entry.delete(0, END)
        self.var_timer.set('')
        self.set_random_word()

        self.msg.config(text=self.sentences)
        self.start_time()

    def set_random_word(self):
        file = self.open_file()
        self.sentences = random.choice(file)

    def open_file(self):
        with open('test_typing.txt', encoding='utf-8') as f:
            file = f.read().split('\n')
        return file


if __name__ == '__main__':
    RunPage()
