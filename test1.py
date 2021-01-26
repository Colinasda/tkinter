import tkinter as tk

window = tk.Tk()
window.title('my window')
# 设置画布大小，使用x
window.geometry('200x100')

var = tk.StringVar()
l = tk.Label(window,textvariable=var,bg='green',font=('Arial',12),width=15,height=2)
l.pack()

on_hit =False
def hit_me():
    global on_hit
    if on_hit ==False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

# 设置button大小
b = tk.Button(window,text='Hit me',width=15,height=2,command=hit_me)
b.pack()

window.mainloop()