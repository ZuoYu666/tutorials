# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, text='', bg='yellow')
l.pack()
counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter+=1


menubar = tk.Menu(window)          # 加一个菜单条
filemenu = tk.Menu(menubar, tearoff=0)       # 设置菜单条的参数
menubar.add_cascade(label='File', menu=filemenu)  # 在菜单条上加东西
filemenu.add_command(label='New', command=do_job)  # 在子菜单条上加东西
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()            # 加分开的线
filemenu.add_command(label='Exit', command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

submenu = tk.Menu(filemenu)       # 子菜单条的子菜单条操作
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label="Submenu1", command=do_job)

window.config(menu=menubar)     # 把菜单条放在window上

window.mainloop()


