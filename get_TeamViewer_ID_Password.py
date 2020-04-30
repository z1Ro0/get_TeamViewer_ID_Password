#!/usr/bin/python
# # -*- coding: utf-8 -*-
import win32gui,win32api,win32con

def get_child_windows(parent):        
    '''     
    获得parent的所有子窗口句柄
     返回子窗口句柄列表
     '''     
    if not parent:         
        return      
    hwndChildList = []     
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd),  hwndChildList)          
    return hwndChildList 

def get_edit(edtextHwnd):
    # 获取识别结果中输入框文本
    length = win32gui.SendMessage(edtextHwnd, win32con.WM_GETTEXTLENGTH)+1
    buf = win32gui.PyMakeBuffer(length)
    #发送获取文本请求
    win32api.SendMessage(edtextHwnd, win32con.WM_GETTEXT, length, buf)
    #下面应该是将内存读取文本
    address, length = win32gui.PyGetBufferAddressAndLen(buf[:-1])
    text = win32gui.PyGetString(address, length)
    return text

def get_program(hwnd,program_name):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        if win32gui.GetWindowText(hwnd) == program_name:
            childs = get_child_windows(hwnd)
            passwd_is = False
            for i in range(len(childs)):
                if win32gui.GetWindowText(childs[i]) == "您的ID" or win32gui.GetWindowText(childs[i]) == "Your ID":
                    print('ID: {}'.format(get_edit(childs[i+1])))
                    passwd_is = True
                if win32gui.GetWindowText(childs[i]) == "密码" or win32gui.GetWindowText(childs[i]) == "Password" and passwd_is:
                    print('Password: {}'.format(get_edit(childs[i+1])))

program_name = 'TeamViewer'           
win32gui.EnumWindows(get_program, program_name)