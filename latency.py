import subprocess
from itertools import count
import os
from art import *
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import suppress
import sys
import re

data = []
data2 = []

testdata = []

def testdata(intt, mult):
    #sig
    res = [random.randrange(25, 50, 1) for i in range(mult + 1)]
    res.sort()
    try:
        out = res[intt]
    except IndexError:
        pass
    #ping
    res1 = [random.randrange(0, 10, 1) for i in range(mult + 1)]
    res1.sort()
    try:
        out1 = float("1." + str(res1[intt]))
    except IndexError:
        pass
    
    return(out, out1)


def maincalc():

    try:
         cmd = int(str(subprocess.check_output('iwconfig wlan0 | grep -i level=', shell=True).decode('ascii')).replace("   ", "")[35:37])
         data.append(cmd)
         avgsig = int(sum(data) / len(data))
         if len(data) > 500:
            del data[:-500]
    except subprocess.CalledProcessError as e:
        pass


 
    try:
        cmd2 = float(str(subprocess.check_output('ping 172.16.224.1 -c 1',  shell=True).decode('ascii'))[106:110])
        data2.append(cmd2)
        avgping = str(sum(data2) / len(data2))[0:3]
        if len(data2) > 1000:
            del data2[:-1000]
    except subprocess.CalledProcessError as e:
        pass




    os.system('clear')
    print(text2art(str(avgsig)))
    #print(text2art(str(avgping)))
    #return str(avgsig), str(avgping)


plt.style.use('dark_background')
plt.rcParams['toolbar'] = 'None'

xar = []
yar = []

index = count()


def animate(i):
    a,b = testdata(next(index), 50)
    os.system('clear')
    printed = str(xar).replace('[','').replace(']','').replace('\'','').replace('\"','')
    print(printed)
    xar.append(next(index))
    yar.append(int(a))
    plt.cla()
    plt.plot(xar, yar)


ani = FuncAnimation(plt.gcf(), animate, 50)


plt.tight_layout()
plt.show(block=False)

plt.show()




