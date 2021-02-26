#John Schuster
#jschuster@ridedart
#Checking Arrival/Departure Outdoor Signs at DCSLounge
#Must have TightVNC installed on computer running this script

import pyautogui
import subprocess
import os
import time, datetime
from PIL import Image
from passwdStuff import whatPasswd
OpenVNCTime = "07,30,00"

DartBlue = (128,0,255)
TightVNC = 'C:\\Program Files\\TightVNC\\tvnviewer.exe'
PlatformB = '-host=10.1.103.27'
PlatformC = '-host=10.1.103.29'
PlatformH = '-host=10.1.103.25'
PlatformI = '-host=10.1.103.24'
PlatformN = '-host=10.1.103.28'
PlatformO = '-host=10.1.103.26'
DCSLounge = '-host=DCSLoungeS1-PC2.dmmta.com'
VNCList = [PlatformB,PlatformC,PlatformH,PlatformI,PlatformN];
#VNCList = [PlatformB,PlatformC];
VNCDict = {PlatformB:'Platform B',PlatformC:'Platform C',PlatformH: 'Platform H',PlatformI: 'Platform I',PlatformN: 'Platform N',DCSLounge:'DCSLounge'}

TightVNCStuff = 'Chicken'
ScreenShotLists= [];
EmailText = "Have a nice day!"


def StartTheVNC(VNCLocation, Host, PassWd, VNCStatus):
    
    #this checks VNCStatus.  If "Chicken" it opens the VNC/ closes the VNC if 'None'
    if VNCStatus == "Chicken":
    
        
        TightVNCStuff = subprocess.Popen([VNCLocation,Host,PassWd])
    
    else:
        VNCStatus.terminate()
        TightVNCStuff = "Chicken"
    
    return TightVNCStuff
    

if __name__ == '__main__':
    #get the current time
    #CurrentTime = time.strftime("%H,%M,%S",time.localtime())
    #open the VNC
    TightVNCPassword = whatPasswd('TightVNC')
#    CurrentTime == OpenVNCTime and 
    for pcs in range(len(VNCList)):

        TightVNCStuff = StartTheVNC(TightVNC, VNCList[pcs],TightVNCPassword['Password'], TightVNCStuff)
        time.sleep(10)

     
        #wait to have it load
    #    if CurrentTime == VNCLoading:
        for i in range(5):
            
            #find the icon of the vnc veiwer screen
            CurrentDay = time.strftime("%e%b%y%S",time.localtime())
            ScreenStuff = CurrentDay +VNCDict[VNCList[pcs]]+ "_VNCScreenshot.png"  
            ScreenShotLists.append(ScreenStuff)
            try:
                TVILx, TVILy = pyautogui.locateCenterOnScreen('tightvncicon.png')
                #take a screenshot of the webpage of the display
                im = pyautogui.screenshot(ScreenStuff, region=(TVILx,TVILy, 300, 400))
                DoesTheColorMatch = im.getpixel((100,100))
            except TypeError:
                TVILx, TVILy = pyautogui.locateCenterOnScreen('tightvncicon2.png')
                #take a screenshot of the webpage of the display
                im = pyautogui.screenshot(ScreenStuff, region=(TVILx,TVILy, 700, 900))
            
                #analyze the screen shot 
                DoesTheColorMatch = im.getpixel((200,100))
            #if white, press CTRL-R and delete previous screenshot (Five times)
            if DoesTheColorMatch != DartBlue and i < 4:
                try:
                    #press ctrl on the VNC veiwer
                    pyautogui.click('tightCtrl.png')
                    #keypress "r"
                    pyautogui.press('r')
                    #wait for a bit
                    time.sleep(15)
                except TypeError: 
                    #press ctrl on the VNC veiwer
                    pyautogui.click('tightCtrl2.png')
                    #keypress "r"
                    pyautogui.press('r')
                    #wait for a bit
                    time.sleep(15)
                break
            if DoesTheColorMatch != DartBlue and i ==4:
                #set the email to create a ticket that attention is needed
                EmailText = 'The computer at ' +VNCDict[VNCList[pcs]]+ ' needs attention'
                break
            if DoesTheColorMatch == DartBlue:
                
                if i > 1 and i < 4:
                    #needed to reload the page but was successful
                    EmailText = 'The computer at ' +VNCDict[VNCList[pcs]]+ ' had a blank screen but was successfully reloaded.'
                    #save the image for the email.
                    break
                if i == 1:
                    
                    #set the email to create a ticket that the task succeeded
                    EmailText = 'The computer at ' +VNCDict[VNCList[pcs]]+ ' was successfully checked and did not need reloaded.'
                    break
                
            

        #Close the VNC
        TightVNCStuff = StartTheVNC(TightVNC, VNCList[pcs],TightVNCPassword, TightVNCStuff)


        #email HDT that action was completed and outcome
        print(EmailText)



    # create loop to go through all the computers
