from tkinter import *
from tkinter import messagebox as mbox
from Simplex import simplexup, simplexdown
class Window:
    def __init__(self,width,height,title='Loboda'):
        self.root=Tk()
        self.root.title(title)
        self.root.iconbitmap('star.ico')
        self.root.wm_attributes('-alpha',1)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False,False)

        self.canvas=Canvas(self.root)
        self.frame=Frame(self.root,bg='#008B8B',height=550, width=400)
        self.frame2=Frame(self.root, bg='#008B8A',height=200, width=200 )
        self.title=Label(self.frame, bg='#2F4F4F', text="Добро пожаловать в мою работу по МоДо", fg='#FFFFE0')
        self.desribe=Label(self.frame, bg='#2F4F4F',wraplength='140', text='Эта программа решает задачи линейного программирования с ограничением на целочисленность и без него',fg='#FFFFE0')
        self.instr1=Label(self.frame,  bg='#2F4F4F', text="Введите кол-во коэффициентов основной функции: ",fg='#FFFFE0')
        self.vr=Entry(self.frame, bg='white')
        self.instr2=Label(self.frame, bg='#2F4F4F', text="Введите кол-во уравнений в системе ограничений: ",fg='#FFFFE0')
        self.rs=Entry(self.frame, bg='white')
        self.instr3=Label(self.frame, bg='#2F4F4F',padx=5, wraplength=380,text="Введите через пробел коэффициенты в таком порядке: коэффициенты основной функции, коэффициенты левой части системы ограничений, коэфициенты правой части ",fg='#FFFFE0')
        self.nums=Entry(self.frame, width=50, bg='white')
        self.r_var= BooleanVar()
        self.r_var.set(0)
        self.r1 = Radiobutton(self.frame,bg='#008B8B',text='Max',width=3,
                 variable=self.r_var, value=0)
        self.r2 = Radiobutton(self.frame,bg='#008B8B',text='Min',
                 variable=self.r_var, value=1)
        self.btn=Button(self.frame,font='Arial 15',text='Розрахувати', bg='#FF4500' , command=self.btn_click)
        self.r_vari = BooleanVar()
        self.r_vari.set(0)
        self.r3 = Radiobutton(self.frame2, bg='#008B8B', text='Integer',
                              variable=self.r_vari, value=1)
        self.r4 = Radiobutton(self.frame2, bg='#008B8B', text='NonInteger',
                              variable=self.r_vari, value=0)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()
    def draw_widgets(self):
        self.canvas.pack()
        self.frame.place(relwidth=1, relheight=1)
        self.frame2.place(x=75, y=362)
        self.title.pack(pady=10)
        self.desribe.pack(pady=7, padx=5, anchor=NE)
        self.instr1.pack(pady=5,padx=5, anchor=NW)
        self.vr.pack(pady=5,padx=5, anchor=NW)
        self.instr2.pack(pady=5,padx=5, anchor=NW)
        self.rs.pack(pady=5,padx=5, anchor=NW)
        self.instr3.pack(pady=5, padx=5,anchor=NW)
        self.nums.pack(pady=5,padx=5, anchor=NW)
        self.r1.pack(padx=15, anchor=NW)
        self.r2.pack(padx=15, anchor=NW)
        self.r3.pack(padx=15, anchor=NW)
        self.r4.pack(padx=15, anchor=NW)
        self.btn.pack(pady=4)
    def btn_click(self):
        vari= int(self.vr.get())
        rsys = int(self.rs.get())
        numes = self.nums.get()
        numes= numes.split()
        for i in range(len(numes)):
            numes[i]=float(numes[i])
        if self.r_var.get():
            answers=simplexdown(vari,rsys,numes,self.r_vari.get())
        else:
            answers=simplexup(vari,rsys,numes,self.r_vari.get())
        print(answers)
        mbox.showinfo(title="Take an answer!", message=answers)




window=Window(400,550,'Вячеслав Лобода')
window.run()