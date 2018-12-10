import autopy

import win32api

import tkinter

from win32api import GetSystemMetrics

import win32gui

import PIL

import time





win32api.ShellExecute(0, 'open', 'C:\\Users\\hao\\Desktop\\帝国霸略.lnk', '','',1)

autopy.mouse.move(1200, 200) # 移动鼠标

#autopy.mouse.smooth_move(0, 0) # 平滑移动鼠标（上面那个是瞬间的）

autopy.mouse.click() # 单击

#autopy.mouse.toggle(True,'down')


#autopy.mouse.toggle(False,'down')




#Python获取屏幕分辨率

def DisplaySize():
    return GetSystemMetrics(0), GetSystemMetrics(1)


#就需要定位到阴阳师的窗口
def get_window_info():  # 获取阴阳师窗口信息
    wdname = u'阴阳师-网易游戏'
    handle = win32gui.FindWindow(0, wdname)  # 获取窗口句柄
    if handle == 0:
        # text.insert('end', '小轩提示：请打开PC端阴阳师\n')
        # text.see('end')  # 自动显示底部
        return None
    else:
        return win32gui.GetWindowRect(handle)


def get_posx(x, window_size):  # 返回x相对坐标
    return (window_size[2] - window_size[0]) * x / 870


def get_posy(y, window_size):  # 返回y相对坐标
    return (window_size[3] - window_size[1]) * y / 520

