# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')
# e = tk.Entry(window, show="*")
e = tk.Entry(window, show=None)
# e = tk.Entry(window, show="1")  # 加一个entry（输入框） 不管属什么都显示1
e.pack()     # 放在window上

def insert_point():
    var = e.get()
    t.insert('insert', var)      # 放到光标所指位置
def insert_end():
    var = e.get()
    # t.insert('end', var)
    t.insert(2.2, var)             # 插入到指定位置

b1 = tk.Button(window, text='insert point', width=15,
              height=2, command=insert_point)          # 加个按钮，这个函数要玩转了，能造假
b1.pack()
b2 = tk.Button(window, text='insert end',          # 这个把按钮放文本框尾部了
               command=insert_end)
b2.pack()
t = tk.Text(window, height=2)         # 加个文本框
t.pack()

window.mainloop()
