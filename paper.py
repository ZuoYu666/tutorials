import tkinter as tk

window = tk.Tk()
window.title('螺栓智能分类系统')
window.geometry('200x200')

counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter+=1

window.iconbitmap("bitbug_favicon.ico")

# 菜单
menubar = tk.Menu(window)          # 加一个菜单条
filemenu = tk.Menu(menubar)       # 设置菜单条的参数
menubar.add_cascade(label='连接设备')  # 在菜单条上加东西
filemenu.add_command(label='New')  # 在子菜单条上加东西
filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_separator()            # 加分开的线
filemenu.add_command(label='Exit', command=window.quit)


viewmenu = tk.Menu(menubar)       # 设置菜单条的参数
menubar.add_cascade(label='编辑')  # 在菜单条上加东西
viewmenu.add_command(label='New')  # 在子菜单条上加东西
viewmenu.add_command(label='Open')
viewmenu.add_command(label='Save')
viewmenu.add_separator()            # 加分开的线
viewmenu.add_command(label='Exit')

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='显示', menu=editmenu)
editmenu.add_command(label='Cut',)
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='工具', menu=editmenu)
editmenu.add_command(label='Cut',)
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')

qmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='系统', menu=editmenu)
editmenu.add_command(label='Cut',)
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')

wmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='分类器', menu=editmenu)
editmenu.add_command(label='Cut',)
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')

emenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='图像设置', menu=editmenu)
editmenu.add_command(label='Cut',)
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')


# 放“螺钉自动检测系统”
var = tk.StringVar()      # 字符串变量（被用于显示区显示）
var0 = tk.StringVar()
l = tk.Label(window, text='螺栓智能分类系统', bg='#F0F0F0', font=('方正姚体', 28), width=56,
             height=2)     # 窗体其它参数
l.pack()        # 放的位置

# 左上角 当前编号
tk.Label(window, text='当前编号:', font=('Arial', 12), width=15, height=2).place(x=26, y=100, anchor='nw')
text0 = tk.Text(window, font=('Arial', 15), height=1, width=9)         # 加个文本框
text0.place(x=136, y=105, anchor='nw')


# 第三排
def print_selection(v):
    l.config(text='you have selected ' + v)

# 滑动条
s1 = tk.Scale(window, from_=0.0001, to=1, orient=tk.HORIZONTAL,       # 定义scale（滑动条）
             length=160, resolution=0.001) # showvalue 表示每次滑动显示值。  tickinterval 表示标签单位长度。

tk.Label(window, text='训练学习率:', font=('Arial', 16), width=10, height=2).place(x=806, y=126, anchor='nw')
s1.place(x=930, y=120, anchor='nw')      # 指定放置某一点的位置（anchor表示要放物体的锚点）

tk.Label(window, text='训练批次个数:', font=('Arial', 16), width=12, height=2).place(x=1126, y=126, anchor='nw')
s2 = tk.Scale(window, from_=0, to=200, tickinterval=50, orient=tk.HORIZONTAL,       # 定义scale（滑动条）
             length=200, resolution=1)
s2.place(x=1280, y=120, anchor='nw')      # 指定放置某一点的位置（anchor表示要放物体的锚点）


image1 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/2.gif')
image2 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/1.gif')
image3 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/8.gif')
image4 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/00.gif')
image5 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/3.gif')
image6 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/6.gif')
image7 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/4.gif')
image8 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/12.gif')
image9 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/21.gif')
image10 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/9.gif')
image11 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/10.gif')
image12 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/app_store.png')
image13 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/camera.png')
image14 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/expend.png')
image15 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/layout.png')
image16 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/line.png')
image17 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/pot.png')
image18 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/save.png')
image19 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/setting.png')
image20 = tk.PhotoImage(file='C:/Users/11410/Desktop/picture/time.png')

# 左侧快捷键按钮
b61 = tk.Button(window, image=image1, width=28, height=28)       # 加一个按钮操作
b61.place(x=16, y=210, anchor='nw')

b62 = tk.Button(window, image=image2, width=28, height=28)       # 加一个按钮操作
b62.place(x=56, y=210, anchor='nw')

b63 = tk.Button(window, image=image3, width=28, height=28)       # 加一个按钮操作
b63.place(x=16, y=250, anchor='nw')

b64 = tk.Button(window, image=image4, width=28, height=28)       # 加一个按钮操作
b64.place(x=56, y=250, anchor='nw')

b65 = tk.Button(window, image=image5, width=28, height=28)       # 加一个按钮操作
b65.place(x=16, y=290, anchor='nw')

b6666 = tk.Button(window, image=image6, width=28, height=28)       # 加一个按钮操作
b6666.place(x=56, y=290, anchor='nw')

b67 = tk.Button(window, image=image7, width=28, height=28)       # 加一个按钮操作
b67.place(x=16, y=330, anchor='nw')

b68 = tk.Button(window, image=image8, width=28, height=28)       # 加一个按钮操作
b68.place(x=56, y=330, anchor='nw')

b69 = tk.Button(window, image=image9, width=28, height=28)       # 加一个按钮操作
b69.place(x=16, y=370, anchor='nw')

b70 = tk.Button(window, image=image10, width=28, height=28)       # 加一个按钮操作
b70.place(x=56, y=370, anchor='nw')

b71 = tk.Button(window, image=image11, width=28, height=28)       # 加一个按钮操作
b71.place(x=16, y=410, anchor='nw')

b72 = tk.Button(window, image=image12, width=28, height=28)       # 加一个按钮操作
b72.place(x=56, y=410, anchor='nw')

b73 = tk.Button(window, image=image13, width=28, height=28)       # 加一个按钮操作
b73.place(x=16, y=450, anchor='nw')

b76 = tk.Button(window, image=image14, width=28, height=28)       # 加一个按钮操作
b76.place(x=56, y=450, anchor='nw')

b68 = tk.Button(window, image=image15, width=28, height=28)       # 加一个按钮操作
b68.place(x=16, y=490, anchor='nw')

b69 = tk.Button(window, image=image16, width=28, height=28)       # 加一个按钮操作
b69.place(x=56, y=490, anchor='nw')

b70 = tk.Button(window, image=image17, width=28, height=28)       # 加一个按钮操作
b70.place(x=16, y=530, anchor='nw')

b71 = tk.Button(window, image=image18, width=28, height=28)       # 加一个按钮操作
b71.place(x=56, y=530, anchor='nw')

b72 = tk.Button(window, image=image19, width=28, height=28)       # 加一个按钮操作
b72.place(x=16, y=570, anchor='nw')

b73 = tk.Button(window, image=image20, width=28, height=28)       # 加一个按钮操作
b73.place(x=56, y=570, anchor='nw')


# 图像显示区
canvas0 = tk.Canvas(window, bg='#F0F0F0', height=500, width=680)     # 添加一个画布（颜色，高，宽）

image_file0 = tk.PhotoImage(file='俯视图_边框OjbK.png')     # 加入图片和形状
image_file1 = tk.PhotoImage(file='正视图_边框OjbK.png')
# image_file2 = tk.PhotoImage(file='绘图区.png')

image_one = canvas0.create_image(95, 10, anchor='nw', image=image_file0)  # 放置画布中的位置（左上角）
image_two = canvas0.create_image(95, 320, anchor='nw', image=image_file1)
# image_three = canvas0.create_image(300, 0, anchor='nw', image=image_file2)

canvas0.place(x=100, y=150, anchor='nw')      # 指定放置某一点的位置（anchor表示要放物体的锚点）

# 杆直径、半径等参数
tk.Label(window, text='螺纹长度b(mm):', font=('Arial', 12), width=12, height=2).place(x=20, y=659, anchor='nw')
t1 = tk.Text(window, font=('Arial', 15), height=1, width=6)         # 加个文本框
t1.place(x=140, y=666, anchor='nw')

tk.Label(window, text='栓头厚度K(mm):', font=('Arial', 12), width=12, height=2).place(x=230, y=659, anchor='nw')
t2 = tk.Text(window, font=('Arial', 15), height=1, width=6)         # 加个文本框
t2.place(x=350, y=666, anchor='nw')

tk.Label(window, text='栓头直径dk(mm):', font=('Arial', 12), width=13, height=2).place(x=440, y=659, anchor='nw')
t3 = tk.Text(window, font=('Arial', 15), height=1, width=6)         # 加个文本框
t3.place(x=560, y=666, anchor='nw')

tk.Label(window, text='六角内径s(mm):', font=('Arial', 12), width=12, height=2).place(x=650, y=659, anchor='nw')
t4 = tk.Text(window, font=('Arial', 15), height=1, width=6)         # 加个文本框
t4.place(x=770, y=666, anchor='nw')

tk.Label(window, text='螺纹中径d(mm):', font=('Arial', 12), width=12, height=2).place(x=860, y=659, anchor='nw')
t5 = tk.Text(window, font=('Arial', 15), height=1, width=6)         # 加个文本框
t5.place(x=990, y=666, anchor='nw')

tk.Label(window, text='牙距极限公差(mm):', font=('Arial', 12), width=15, height=2).place(x=1080, y=659, anchor='nw')
t5 = tk.Text(window, font=('Arial', 15), height=1, width=6)         # 加个文本框
t5.place(x=1220, y=666, anchor='nw')

tk.Label(window, text='螺栓质量m(mm):', font=('Arial', 12), width=13, height=2).place(x=1310, y=659, anchor='nw')
t6 = tk.Text(window, font=('Arial', 15), height=1, width=6)         # 加个文本框
t6.place(x=1430, y=666, anchor='nw')


# 最后一排的各个按钮
b1 = tk.Button(window, font=('Arial', 12), text='型号选择', width=16,
              height=3, bg='gray')       # 加一个按钮操作
b1.place(x=36, y=720, anchor='nw')

b2= tk.Button(window, font=('Arial', 12), text='图像存储', width=16,
              height=3, bg='gray')       # 加一个按钮操作
b2.place(x=296, y=720, anchor='nw')

b3 = tk.Button(window, font=('Arial', 12), text='模型分析', width=16,
              height=3, bg='gray')       # 加一个按钮操作
b3.place(x=556, y=720, anchor='nw')

b4 = tk.Button(window, font=('Arial', 12), text='样本统计', width=16,
              height=3, bg='gray')       # 加一个按钮操作
b4.place(x=816, y=720, anchor='nw')

b5 = tk.Button(window, font=('Arial', 12), text='模型评测', width=16,
              height=3, bg='gray')       # 加一个按钮操作
b5.place(x=1076, y=720, anchor='nw')

b6 = tk.Button(window, font=('Arial', 12), text='界面设置', width=16,
              height=3, bg='gray')       # 加一个按钮操作
b6.place(x=1336, y=720, anchor='nw')


# 工作模式
tk.Label(window, text='工作模式选择:', font=('黑体', 15), width=16, height=2).place(x=860, y=176, anchor='nw')
r1 = tk.Radiobutton(window, text='智能模式一', font=('Arial', 12),       # 定义rediobutton，
                    variable=var, value='A')
r1.place(x=900, y=220, anchor='nw')

r2 = tk.Radiobutton(window, text='智能模式二', font=('Arial', 12),
                    variable=var, value='B')
r2.place(x=900, y=255, anchor='nw')

r3 = tk.Radiobutton(window, text='手动模式', font=('Arial', 12),
                    variable=var, value='C')
r3.place(x=900, y=290, anchor='nw')


# 分类方案
tk.Label(window, text='分类方案选择:', font=('黑体', 15), width=16, height=2).place(x=1200, y=176, anchor='nw')

r21 = tk.Radiobutton(window, text='方案一', font=('Arial', 12),       # 定义rediobutton，
                    variable=var0, value='A')
r21.place(x=1200, y=220, anchor='nw')

r22 = tk.Radiobutton(window, text='方案二', font=('Arial', 12),
                    variable=var0, value='B')
r22.place(x=1360, y=220, anchor='nw')

r23 = tk.Radiobutton(window, text='方案三', font=('Arial', 12),
                    variable=var0, value='C')
r23.place(x=1200, y=255, anchor='nw')

r24 = tk.Radiobutton(window, text='方案四', font=('Arial', 12),
                    variable=var0, value='D')
r24.place(x=1360, y=255, anchor='nw')


# 右侧按钮 和文本框

z1 = tk.Button(window, font=('Arial', 12), fg='white', text='中径线校准', width=15,
              height=2, bg='gray')       # 加一个按钮操作
z1.place(x=1166, y=300, anchor='nw')

z2 = tk.Button(window, font=('Arial', 12), fg='white', text='SVM参数设置', width=15,
              height=2, bg='gray')       # 加一个按钮操作
z2.place(x=1166, y=375, anchor='nw')

z3 = tk.Button(window, font=('Arial', 12), fg='white', text='xgBoost参数设置', width=15,
              height=2, bg='gray')       # 加一个按钮操作
z3.place(x=1166, y=450, anchor='nw')

z4 = tk.Button(window, font=('Arial', 12), fg='white', text='螺栓规格选型', width=15,
              height=2, bg='gray')       # 加一个按钮操作
z4.place(x=1166, y=525, anchor='nw')

z5 = tk.Button(window, font=('Arial', 12), fg='white', text='废品重检', width=15,
              height=2, bg='gray')       # 加一个按钮操作
z5.place(x=1166, y=600, anchor='nw')

tk.Label(window, text='通讯状态:', font=('Arial', 12), width=12, height=2).place(x=870, y=320, anchor='nw')
t01 = tk.Text(window, font=('Arial', 15), height=1, width=9)         # 加个文本框
t01.place(x=990, y=329, anchor='nw')

tk.Label(window, text='已检个数(个):', font=('Arial', 12), width=12, height=2).place(x=870, y=370, anchor='nw')
t03 = tk.Text(window, font=('Arial', 15), height=1, width=9)         # 加个文本框
t03.place(x=990, y=379, anchor='nw')



tk.Label(window, text='相机选择:', font=('Arial', 12), width=12, height=2).place(x=870, y=420, anchor='nw')
t05 = tk.Text(window, font=('Arial', 15), height=1, width=9)         # 加个文本框
t05.place(x=990, y=429, anchor='nw')



tk.Label(window, text='精密螺栓（个）:', font=('Arial', 12), width=12, height=2).place(x=870, y=470, anchor='nw')
t07 = tk.Text(window, font=('Arial', 15), height=1, width=9)         # 加个文本框
t07.place(x=990, y=479, anchor='nw')



tk.Label(window, text='工业螺栓（个）:', font=('Arial', 12), width=12, height=2).place(x=870, y=520, anchor='nw')
t09 = tk.Text(window, font=('Arial', 15), height=1, width=9)         # 加个文本框
t09.place(x=990, y=529, anchor='nw')


tk.Label(window, text='家用螺栓（个）:', font=('Arial', 12), width=12, height=2).place(x=870, y=570, anchor='nw')
t01 = tk.Text(window, font=('Arial', 15), height=1, width=9)         # 加个文本框
t01.place(x=990, y=579, anchor='nw')

tk.Label(window, text='废品（个）:', font=('Arial', 12), width=12, height=2).place(x=870, y=620, anchor='nw')
t02 = tk.Text(window, font=('Arial', 15), height=1, width=9)         # 加个文本框
t02.place(x=990, y=629, anchor='nw')




b66 = tk.Button(window, text='启动', font=('Arial', 16),fg='white',  width=7,
              height=3, bg='green')
b66.place(x=1360, y=360, anchor='nw')


b666 = tk.Button(window, text='暂停', font=('Arial', 16), width=7,
              height=3, bg='yellow')
b666.place(x=1500, y=360, anchor='nw')

b6666 = tk.Button(window, text='停止', font=('Arial', 16), width=7,
              height=3, bg='red')
b6666.place(x=1360, y=500, anchor='nw')

b66666 = tk.Button(window, text='退出', font=('Arial', 16), width=7,
              height=3, bg='#F0F0F0')
b66666.place(x=1500, y=500, anchor='nw')


submenu = tk.Menu(filemenu)       # 子菜单条的子菜单条操作
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label="Submenu1", command=do_job)

window.config(menu=menubar)     # 把菜单条放在window上

window.mainloop()