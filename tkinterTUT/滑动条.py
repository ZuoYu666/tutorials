# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_selection(v):
    l.config(text='you have selected ' + v)

s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,       # 定义scale（滑动条）
             length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
# showvalue 表示每次滑动显示值。  tickinterval 表示标签单位长度。

s.pack()

window.mainloop()