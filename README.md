# Check_VNC
This Python Script checks the VNCs that have a website displayed.
import pyautogui
import subprocess
import os
import time, datetime
from PIL import Image
from passwdStuff import whatPasswd

Need all of these modules installed.

The passwdStuff is a .py file that has passwords stored in it.  Below is the function I use.  If using this script you will have to provide your own passwords.

def whatPasswd(appStuff):

    #going to return a dict for this function
    dictStuff = {'User':'' , 'Password':''}
    tightVNCPassword = '-password=<Your Password Here>'
    upsUser = '<your user>'
    upsPassword = '<your password>'
    if appStuff == 'TightVNC':
        dictStuff['User'] = 'None'
        dictStuff['Password'] = tightVNCPassword
    if appStuff == 'UPS':
        dictStuff['User'] = upsUser
        dictStuff['Password'] = upsPassword
   
    
    return dictStuff
