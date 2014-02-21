import random
import sys
import subprocess
import time

time.sleep(2)
subprocess.Popen(["xdo", "keypress", "-k", "49"])
time.sleep(0.2)
subprocess.Popen(["xdo", "keyrelease", "-k", "49"])

def keydown(k):
    print("keydown "+k)
    process = subprocess.Popen(["xdo", "keypress", "-k", k])
    time.sleep(random.random() * 0.075)
    process.wait()
    print("keyup "+k)
    process = subprocess.Popen(["xdo", "keyrelease", "-k", k])
    process.wait()

while 1:
    number = random.random()
    if number < 0.03333: # nerf the start button
        keydown('36')
    else:
        keydown(random.choice(['116','111','113','114','56','61']))
