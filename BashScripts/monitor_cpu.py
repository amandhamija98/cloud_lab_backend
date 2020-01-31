import psutil
import os

threshold = 75
while True:
    val = psutil.cpu_percent(interval = 5)
    if  val >= threshold :
        print("Cpu usage exceeded")
        os.system("shutdown /r /t 1")

