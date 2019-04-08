import time
import os
import ctypes
ctypes.windll.user32.MessageBoxW(0,"gogogo","alarm started",1)
while 1:
    time.sleep(1800)
    ctypes.windll.user32.MessageBoxW(0,"relax your eyes","eyes",1)
    time.sleep(30)
    ctypes.windll.user32.MessageBoxW(0, "relax your eyes", "eyes", 1)
    time.sleep(30)
    ctypes.windll.user32.MessageBoxW(0, "relax your eyes", "eyes", 1)
    time.sleep(1800)
    ctypes.windll.user32.MessageBoxW(0, "move your body", "body", 1)
    time.sleep(30)
    ctypes.windll.user32.MessageBoxW(0, "move your body", "body", 1)
    time.sleep(30)
    ctypes.windll.user32.MessageBoxW(0, "move your body", "body", 1)