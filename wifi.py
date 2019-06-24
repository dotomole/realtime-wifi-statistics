'''
Thomas Di Pietro 24/6/19
'''
import subprocess
import os
import sys
import time
from tkinter import *

def connected():
    cmd = 'netsh wlan show interfaces | findstr /i \"State\"'
    output = os.popen(cmd).read().split('\n')
    signal = output[0].split(": ")
    if signal[1] == 'connected':
        return True
    else:
        return False

def getDefGateway():
    cmd = 'ipconfig | findstr /i \"Gateway\"'
    output = os.popen(cmd).read().split(' ')
    return output[15]

def getSigStrength():
    cmd = 'netsh wlan show interfaces | findstr /i \"Signal\"'
    output = os.popen(cmd).read().split('\n')
    signal = output[0].split(": ")
    return signal[1]

def getSSID():
    cmd = 'netsh wlan show interfaces | findstr /i \"SSID\"'
    output = os.popen(cmd).read().split('\n')
    ssid = output[0].split(": ")
    return ssid[1]

def getPing():
    try:
        cmd = 'ping -w 1 /n 1 '+defGateway
        output = os.popen(cmd).read().split(' ')
        ping = output[10].split("=")
        return ping[1]
    except:
        return "INF"

def updateSig():
    sigLabel["text"] = getSigStrength()
    root.after(100, updateSig)

def updatePing():
    pingLabel["text"] = getPing()
    root.after(100, updatePing)

root = Tk()
root.title('Wi-Fi Statistics')
root.geometry("300x300")
labelfont = ('verdana', 30, 'bold')

if connected():
    defGateway = getDefGateway()

    ssid = Label(root, text=getSSID())
    sigLabel = Label(root, text=getSigStrength())
    pingLabel = Label(root, text=getPing())

    ssid.config(font=labelfont, height=2, width=10)
    pingLabel.config(font=labelfont, height=2, width=10)
    sigLabel.config(font=labelfont, height=2, width=10)

    ssid.pack()
    sigLabel.pack()
    pingLabel.pack()

    root.after(1, updateSig)
    root.after(1, updatePing)
else:
    disc = Label(root, text="Wi-Fi disconnected.")
    disc.config(font=('verdana',10,'bold'), height=2, width=30)
    disc.pack()

root.mainloop()