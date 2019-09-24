import tkinter as tk

window = tk.Tk()
window.title('my window')    # 设置窗体名称
window.geometry('200x100')   # 设置窗体尺寸

var = tk.StringVar()      # 字符串变量（被用于显示区显示）
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15,
             height=2)     # 窗体其它参数
# l = tk.Label(window, text='OMG! this is TK!', bg='green', font=('Arial', 12), width=15, height=2)
l.pack()        # 放的位置


image1 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/1.gif')
b = tk.Button(window, image=image1, width=15, height=20)       # 加一个按钮操作
b.pack()


window.mainloop()

image1 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/1.gif')
b61 = tk.Button(window, image=image1, width=15, height=20)       # 加一个按钮操作
b61.place(x=30, y=210, anchor='nw')