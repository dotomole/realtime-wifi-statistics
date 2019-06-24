'''
Thomas Di Pietro 24/5/19
'''
import subprocess
import os
import sys
import time

def main():
    print("-------------------------------------------------")
    print("|            Wi-Fi Statistics v0.01             |")
    print("-------------------------------------------------")
    print("| This program shows the wi-fi signal strength, |")
    print("| and ping to the default gateway in realtime.  |")
    print("-------------------------------------------------")
    print("Wi-Fi: "+getSSID())
    display()

def getDefGateway():
    cmd = 'ipconfig | findstr /i \"Gateway\"'
    output = os.popen(cmd).read().split(' ')
    return output[15]

defGateway = getDefGateway()

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

if __name__ == '__main__':
    main()