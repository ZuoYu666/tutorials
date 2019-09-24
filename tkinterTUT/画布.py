# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

# canvas（画布）放图片，好看

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

canvas = tk.Canvas(window, bg='blue', height=100, width=200)     # 添加一个画布（颜色，高，宽）
image_file = tk.PhotoImage(file='ins.gif')     # 加入图片和形状
image = canvas.create_image(10, 10, anchor='nw', image=image_file)  # 放置画布中的位置（左上角）
x0, y0, x1, y1= 50, 50, 80, 80              # 加点坐标  （50，50）到（80，80）
line = canvas.create_line(x0, y0, x1, y1)    # 画线
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)       # 加个扇形
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)
canvas.pack()

def moveit():
    canvas.move(rect, 0, 2)        # 选定正方形移动

b = tk.Button(window, text='move', command=moveit).pack()


window.mainloop()

