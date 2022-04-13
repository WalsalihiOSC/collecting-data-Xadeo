#Collecting Data Task

from tkinter import *

class Collecting_dataGUI:
    def __init__(self, parent):
        f1 = Frame(parent, bg = "purple")
        f1.grid()

        f2 = Frame(parent)
        f2.grid()

        propmt_label = Label(f1, text = "Collecting Person Data", bg = "purple", width = 17, height = 5, anchor = W)
        propmt_label.grid(row = 0, column = 0)

        but1 = Button(f1, text = "Show All", anchor = E)
        but1.grid(row = 0, column = 1)

        collection_label1 = Label(f2, text = "First Name:", width = 17, height = 2, anchor = W)
        collection_label1.grid(row = 1, column = 0)

        self.entry_forlb1 = Entry(f2, width = 20)
        self.entry_forlb1.grid(row = 1, column = 1)

        collection_label2 = Label(f2, text = "Age:", width = 17, height = 2, anchor = W)
        collection_label2.grid(row = 2, column = 0)

        self.entry_forlb2 = Entry(f2, width = 20)
        self.entry_forlb2.grid(row = 2, column = 1)

        self.Labelquestion = Label(f2, text = "Do you have a mobile phone?")
        self.Labelquestion.grid(row = 3, column = 0)

        #Checking a radiobutton for a yes or no question
        self.choice_var = StringVar()
        self.choice_var.set("")

        RBbtn = Radiobutton(f2, variable = self.choice_var, value = "No", text = "No")
        RBbtn.grid(row = 3, column = 1, sticky = W)

        RBbtn2 = Radiobutton(f2, variable = self.choice_var, value = "Yes", text = "Yes")
        RBbtn2.grid(row = 4, column = 1, sticky = W)

        enbtn = Button(f2, text = "Enter Data", command = self.enter_data)
        enbtn.grid(row = 5, columnspan = 2)

        def enter_data(self):
            Data = Person_Data(self.entry_forlb1.get(), self.entry_forlb2.get(), self.choice_var.get())


#main routine
if __name__ == "__main__":        
    root = Tk()
    Collect_data = Collecting_dataGUI(root)
    root.mainloop()