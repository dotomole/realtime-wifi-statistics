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
    cmd = 'netsh interface ip show addresses | findstr /i \"Gateway\"'
    output = os.popen(cmd).read().split(' ')
    return output[27]

def getSigStrength():
    cmd = 'netsh wlan show interfaces | findstr /i \"Signal\"'
    output = os.popen(cmd).read().split('\n')
    signal = output[0].split(": ")
    return signal[1]

def getRouterTransRate():
    cmd = 'netsh wlan show interfaces | findstr /i \"Transmit rate\"'
    output = os.popen(cmd).read().split('\n')
    trans = output[0].split(": ")
    return trans[1]

# Alternative method for signal strength
# Gives seemingly less stable results

# def getSigStrength2():
#     cmd = 'netsh wlan show networks mode=bssid'
#     output = os.popen(cmd).read().split('\n')
#     signal = output[9].split(": ")
#     return signal[1]

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

def updateTrans():
    transLabel["text"] = getRouterTransRate()+"mbps"
    root.after(100, updateTrans)

root = Tk()
root.title('Router Wi-Fi Statistics')
root.geometry("300x500")
root.resizable(False, False)

titleFont = ('verdana', 10)
resultFont = ('verdana', 25, 'bold')

if connected():
    defGateway = getDefGateway()

    ssidTitle = Label(root, text="SSID")
    sigTitle = Label(root, text="Signal Strength")
    pingTitle = Label(root, text="Ping to "+defGateway+"(Router)")
    transTitle = Label(root, text="Router Wi-Fi Speed")
   
    ssid = Label(root, text=getSSID())
    sigLabel = Label(root, text=getSigStrength())
    pingLabel = Label(root, text=getPing())
    transLabel = Label(root, text=getRouterTransRate())

    ssidTitle.config(font=titleFont, height=2, width=20)
    sigTitle.config(font=titleFont, height=2, width=20)
    pingTitle.config(font=titleFont, height=2, width=20)
    transTitle.config(font=titleFont, height=2, width=20)

    ssid.config(font=resultFont, height=2, width=10)
    pingLabel.config(font=resultFont, height=2, width=10)
    sigLabel.config(font=resultFont, height=2, width=10)
    transLabel.config(font=resultFont, height=2, width=10)

    #The layout of GUI
    ssidTitle.pack()
    ssid.pack()
    sigTitle.pack()
    sigLabel.pack()
    pingTitle.pack()
    pingLabel.pack()
    transTitle.pack()
    transLabel.pack()

    #Constant updating of details
    root.after(1, updateSig)
    root.after(1, updatePing)
    root.after(1, updateTrans)
else:
    disc = Label(root, text="Wi-Fi disconnected.")
    disc.config(font=titleFont, height=2, width=30)
    disc.pack()

root.mainloop()