# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')
tk.Label(window, text='on the window').pack()       # 定义一个零部件并放置window上

frm = tk.Frame(window)      # 刚刚那个框架下面再加一个框架，（window上放一个框架）
frm.pack()
frm_l = tk.Frame(frm, )     # 定义长在框架上的框架（左侧的框架）
frm_r = tk.Frame(frm)       # 定义长在框架上的框架（右侧的框架）
frm_l.pack(side='left')     # 装在左边
frm_r.pack(side='right')    # 装在右边（基于主fram的左右）

tk.Label(frm_l, text='on the frm_l1').pack()
tk.Label(frm_l, text='on the frm_l2').pack()
tk.Label(frm_r, text='on the frm_r1').pack()
window.mainloop()









