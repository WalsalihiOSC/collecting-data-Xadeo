#Starting Week 9 task 1

from tkinter import *

class Multi_ChoiceGUI:
    def __init__(self, parent):
        self.choice_var = StringVar()
        self.choice_var.set("")
        
        font = ("Comic Sans MS", "10", "bold")

        #Setting up GUI
        prompt_Label = Label(parent, text = "Question.", font = font)
        prompt_Label.grid(row = 0, column = 0)

        #Created an instance of the questions class
        self.q = Questions()
        quesiton_Label = Label(parent, text = self.q.questions, font = font,  width = 30, height = 1)
        quesiton_Label.grid(row = 0, column = 1)
       
        for choice in range(len(self.q.Multi_choice)):
            RBbtn = Radiobutton(parent, variable = self.choice_var, value = str(self.q.Multi_choice[choice]),
                                text = str(self.q.Multi_choice[choice]), command = self.display_answer)
            RBbtn.grid(row = 1 + choice, column = 1, sticky = N)

        self.output_label = Label(parent, text = "Let's see if your knowlegde is impressive!", font = font)
        self.output_label.grid(row = 5, column = 1, sticky = N)
    
    def display_answer(self):
        self.output_label.configure(text = self.q.check_answer(self.choice_var.get()))

class Questions:
    def __init__(self):
        self.questions = "What is the capital of Mongolia?"
        self.answer = "Ulaanbaatar"
        self.Multi_choice = ["Vladivostok", "Astana", "Ulaanbaatar", "Lhasa"]
    
    def check_answer(self, choice):
        if str(choice) == self.answer:
            return str(choice) + " is correct!!"
        else:
            return str(choice) + " is incorrect!!"
        
#main routine
if __name__ == "__main__":        
    root = Tk()
    Multi_Choice = Multi_ChoiceGUI(root)
    root.mainloop()