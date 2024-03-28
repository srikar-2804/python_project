from tkinter import *
from tkinter import ttk

class todolist:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do-List')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-Do-List-App', 
                           font='lucida, 25 bold', width=10,bd=5,bg='red',fg='white')
        self.label.pack(side='top',fill=BOTH)

        self.label = Label(self.root, text='Add Task', 
                           font='lucida, 17 bold', width=10,bd=5,bg='orange',fg='white')
        self.label.place(x=40, y=54)

        self.label = Label(self.root, text='Tasks', 
                           font='lucida, 17 bold', width=10,bd=5,bg='orange',fg='white')
        self.label.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9,bd=5, width=23,font='ariel,20 bold')
        self.main_text.place(x=280,y=100)

        self.main_text = Text(self.root, height=2,bd=5, width=30,font='lucida,10 bold')
        self.text.place(x=20,y=120)


        #----------do task---------------#

        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END,content)
            with open('data.txt','a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0,END)

        def delete():
            delete_ =self.main_text.curselection()
            look=self.main_text.get(delete_)
            with open('data.txt','r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item=str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()  







def main():
    root = Tk()
    ui = todolist(root)
    root.mainloop()

if __name__ == "__main__":
    main()