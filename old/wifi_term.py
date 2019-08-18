'''
Thomas Di Pietro 24/6/19
'''
import subprocess
import os
import sys
import time

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

def getPing():
    try:
        cmd = 'ping -w 1 /n 1 '+defGateway
        output = os.popen(cmd).read().split(' ')
        ping = output[10].split("=")
        return ping[1]
    except:
        return "INF"

def getSSID():
    cmd = 'netsh wlan show interfaces | findstr /i \"SSID\"'
    output = os.popen(cmd).read().split('\n')
    ssid = output[0].split(": ")
    return ssid[1]

def getSigStrength():
    cmd = 'netsh wlan show interfaces | findstr /i \"Signal\"'
    output = os.popen(cmd).read().split('\n')
    signal = output[0].split(": ")
    return signal[1]

def display():
    start_time = time.time()
    while True:
        sys.stdout.write('\rSignal Strength: %s' %getSigStrength())
        sys.stdout.write('Ping: %s ' %getPing())
        elapsed_time = time.time() - start_time
        sys.stdout.write('Time elapsed: %d seconds   ' %(elapsed_time))
        time.sleep(0.1)
        sys.stdout.flush()

if connected():
    print("-------------------------------------------------")
    print("|            Wi-Fi Statistics v0.01             |")
    print("-------------------------------------------------")
    print("| This program shows the wi-fi signal strength, |")
    print("| and ping to the default gateway in realtime.  |")
    print("-------------------------------------------------")
    defGateway = getDefGateway()
    print("Wi-Fi: "+getSSID())
    display()
else:
    print("Wi-Fi disconnected - restart program.")