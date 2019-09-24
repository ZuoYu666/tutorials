# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')    # 设置窗体名称
window.geometry('200x100')   # 设置窗体尺寸

var = tk.StringVar()      # 字符串变量（被用于显示区显示）
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15,
             height=2)     # 窗体其它参数
# l = tk.Label(window, text='OMG! this is TK!', bg='green', font=('Arial', 12), width=15, height=2)
l.pack()        # 放的位置

on_hit = False   # 控制显示还是不现实


def hit_me():           # 定义按钮函数
    global on_hit       # 标出
    if on_hit == False:  # 按下就显示
        on_hit = True
        var.set('you hit me')   # 被用于按钮上的名字
    else:
        on_hit = False     # 不按就不显示
        var.set('')


b = tk.Button(window, text='hit me', width=15,
              height=2, command=hit_me)       # 加一个按钮操作
b.pack()


window.mainloop()
