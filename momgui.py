
import tkinter as tk
import os
import base64
import threading
import time
import win32gui
import PIL
import win32api
import random

from tkinter import scrolledtext

from PIL import ImageGrab

from PIL import Image


window = tk.Tk()  # 创建一个窗口
window.title('帝国霸略辅助程序')
window.geometry('600x400+0+0')  # 窗口的位置以及大小



# 设置图标
#with open('tmp.ico', 'wb+') as fp:
#    fp.write(base64.b64decode(Image))

#window.iconbitmap('tmp.ico')
#os.remove('tmp.ico')

# 设置图标

label = tk.Label(window, font=('微软雅黑', 12), text='请勿非法传播！')  # 显示一段文本
label.pack()

#设置图标
open_icon = open('yaodao.ico', 'rb')
b64str = base64.b64encode(open_icon.read())
open_icon.close()
write_data = "img = '%s'" % b64str
f = open('yaodao.py', 'w+')
f.write(write_data)
f.close()


# Radiobutton #
fun_var = tk.IntVar()
fun_text = ''

def move_click(x, y, t=0):  # 移动鼠标并点击左键
    win32api.SetCursorPos((x, y))  # 设置鼠标位置(x, y)
    win32api.mouse_event(win32api.MOUSEEVENTF_LEFTDOWN |
                         win32api.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 点击鼠标左键
    if t == 0:
        time.sleep(random.random()*2+1)  # sleep一下
    else:
        time.sleep(t)
    return 0

#功能选择
def print_selection():
    global fun_text
    if fun_var.get() == 1:
        fun_text = '寮突破'
    elif fun_var.get() == 2:
        fun_text = '御灵、业原火'
    elif fun_var.get() == 3:
        fun_text = '魂十队员(未完成)'
    elif fun_var.get() == 4:
        fun_text = '魂十队长(未完成)'
    elif fun_var.get() == 5:
        fun_text = '狗粮队员(未完成)'
    label.config(text='功能选择： ' + fun_text)

rb1 = tk.Radiobutton(window, text='寮突破', font=('微软雅黑', 10),
                     variable=fun_var, value=1, command=print_selection)
rb1.place(x=15, y=30)
rb2 = tk.Radiobutton(window, text='御灵、业原火', font=('微软雅黑', 10),
                     variable=fun_var, value=2, command=print_selection)
rb2.place(x=15, y=60)
rb3 = tk.Radiobutton(window, text='魂十队员', font=('微软雅黑', 10),
                     variable=fun_var, value=3, command=print_selection)
rb3.place(x=15, y=90)
rb4 = tk.Radiobutton(window, text='魂十队长', font=('微软雅黑', 10),
                     variable=fun_var, value=4, command=print_selection)
rb4.place(x=15, y=120)
rb5 = tk.Radiobutton(window, text='狗粮队员', font=('微软雅黑', 10),
                     variable=fun_var, value=5, command=print_selection)
rb5.place(x=15, y=150)
# Radiobutton #

#开始按钮

# button start#
rb_list = [rb1, rb2, rb3, rb4, rb5]
button_var = tk.StringVar()
button_var.set('开始')
is_click = False

def get_window_info():  # 获取阴阳师窗口信息
    wdname = u'帝国霸略'
    handle = win32gui.FindWindow(0, wdname)  # 获取窗口句柄
    if handle == 0:
        text.insert('end', '小轩提示：请打开PC端阴阳师\n')
        text.see('end')  # 自动显示底部
        return None
    else:
        text.insert('end', '小轩提示：已经打开帝国霸略\n')
        return win32gui.GetWindowRect(handle)



def start_mission():
    global is_start
    if fun_var.get() == 1:
        text.insert('end', time.strftime('%H:%M:%S', time.localtime()) + ' 开始执行寮突破\n')
        text.see('end')  # 自动显示底部
        window_size = get_window_info()
        if window_size:  # 打开了阴阳师
            window.geometry('240x480+%d+%d' % (window_size[0]-240, window_size[1]))
            is_start = True
            #thread1 = threading.Thread(target=liao_tupo, args=(window_size,))
            #thread1.start()

    elif fun_var.get() == 2:
        text.insert('end', time.strftime('%H:%M:%S', time.localtime()) + ' 开始执行御灵、业原火\n')
        text.see('end')  # 自动显示底部
        window_size = get_window_info()
        if window_size:  # 打开了阴阳师
            window.geometry('240x480+%d+%d' % (window_size[0] - 240, window_size[1]))
            is_start = True
            thread2 = threading.Thread(target=yu_ling, args=(window_size,))
            thread2.start()

    elif fun_var.get() == 3:
        text.insert('end', time.strftime('%H:%M:%S', time.localtime()) + ' 魂十队员功能未开发\n')
        text.see('end')  # 自动显示底部
    elif fun_var.get() == 4:
        text.insert('end', time.strftime('%H:%M:%S', time.localtime()) + ' 魂十队长功能未开发\n')
        text.see('end')  # 自动显示底部
    elif fun_var.get() == 5:
        text.insert('end', time.strftime('%H:%M:%S', time.localtime()) + ' 狗粮队员功能未开发\n')
        text.see('end')  # 自动显示底部


def stop_mission():
    global is_start
    is_start = False
    text.insert('end', time.strftime('%H:%M:%S', time.localtime()) + ' 停止执行\n')
    text.see('end')  # 自动显示底部


def click():
    global is_click
    if not is_click:
        is_click = True
        button_var.set('停止')
        label.config(text=fun_text + ' 已经开始')
        for rb in rb_list:  # 将选项锁定
            rb.config(state='disabled')
        #button_adjust.config(state='disabled')
        start_mission()
    else:
        is_click = False
        button_var.set('开始')
        label.config(text=fun_text + ' 已经停止')
        for rb in rb_list:
            rb.config(state='active')
        #button_adjust.config(state='active')
        stop_mission()

button = tk.Button(window, textvariable=button_var, width=10,
                   height=1, command=click)
button.place(x=140, y=60)

#文本显示

text = scrolledtext.ScrolledText(window, width=29, height=17)  # 滚动输出文本框
# text = tk.Text(window, width=29, height=17)  # 输出文本框
text.place(x=15, y=180)

def get_posx(x, window_size):  # 返回x相对坐标
    return (window_size[0] + x)
    #return (window_size[2] - window_size[0]) * x / 870


def get_posy(y, window_size):  # 返回y相对坐标
    return (window_size[1] + y)
    #return (window_size[3] - window_size[1]) * y / 520

window_size = get_window_info()
topx = window_size[0]
topy = window_size[1]
print(window_size[0],window_size[1])
print(window_size[2],window_size[3])

img_ready = ImageGrab.grab((topx + get_posx(27, window_size), topy + get_posy(316, window_size),
                            topx + get_posx(67, window_size), topy + get_posy(364, window_size)))
#查看图片
img_ready.show()



def hamming(hash1, hash2, n=20):
    b = False
    assert len(hash1) == len(hash2)
    if sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2)) < n:
        b = True
    return b

def get_hash(img):
    img = img.resize((16, 16), Image.ANTIALIAS).convert('L')  # 抗锯齿 灰度
    avg = sum(list(img.getdata())) / 256  # 计算像素平均值
    s = ''.join(map(lambda i: '0' if i < avg else '1', img.getdata()))  # 每个像素进行比对,大于avg为1,反之为0
    return ''.join(map(lambda j: '%x' % int(s[j:j+4], 2), range(0, 256, 4)))

def yu_ling(window_size):
    global is_start
    topx, topy = window_size[0], window_size[1]
    state = []

    while is_start:
        # print 'start'
        # text.insert('end', 'start')
        time.sleep(0.5)
        img_ready = ImageGrab.grab((topx + get_posx(750, window_size), topy + get_posy(465, window_size),
                                    topx + get_posx(840, window_size), topy + get_posy(500, window_size)))
        if hamming(get_hash(img_ready), 'ready_hash', 10):
            state.append(0)
            move_click(topx + get_posx(740, window_size), topy + get_posy(380, window_size))
            text.insert('end', time.strftime('%H:%M:%S', time.localtime()) + ' 点击准备\n')
            text.see('end')  # 自动显示底部
            time.sleep(15)
            continue

        img_success = ImageGrab.grab((topx + get_posx(400, window_size), topy + get_posy(320, window_size),
                                      topx + get_posx(470, window_size), topy + get_posy(400, window_size)))
        if hamming(get_hash(img_success), 'success_hash'):
            time.sleep(2)
            state.append(1)
            text.insert('end', time.strftime('%H:%M:%S', time.localtime()) + ' 成功%d次\n' % state.count(1))
            text.see('end')  # 自动显示底部
            move_click(topx + get_posx(730, window_size), topy + get_posy(380, window_size))
            continue

        img_fail = ImageGrab.grab((topx + get_posx(560, window_size), topy + get_posy(340, window_size),
                                   topx + get_posx(610, window_size), topy + get_posy(390, window_size)))
        if hamming(get_hash(img_fail), 'fail_hash'):
            time.sleep(2)
            state.append(2)
            text.insert('end', time.strftime('%H:%M:%S', time.localtime()) + ' 失败%d次\n' % state.count(2))
            text.see('end')  # 自动显示底部
            move_click(topx + get_posx(720, window_size), topy + get_posy(380, window_size))
            continue

        img_attack = ImageGrab.grab((topx + get_posx(615, window_size), topy + get_posy(350, window_size),
                                     topx + get_posx(675, window_size), topy + get_posy(375, window_size)))
        if hamming(get_hash(img_attack), 'yu_attack_hash'):
            move_click(topx + get_posx(670, window_size), topy + get_posy(365, window_size))
            text.insert('end', time.strftime('%H:%M:%S', time.localtime()) + ' 点击进攻\n')
            text.see('end')  # 自动显示底部
            state.append(3)
            if state[-6:] == [3]*6:
                text.insert('end', time.strftime('%H:%M:%S', time.localtime()) + ' 痴汉券可能不够了\n')
                text.see('end')  # 自动显示底部
                click()
                break
            continue

#window.mainloop()

#https://blog.csdn.net/zydarChen/article/details/77587967