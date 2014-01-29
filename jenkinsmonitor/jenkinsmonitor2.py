'''
Created on 19.01.2014

@author: thilka
'''
import time, urllib, Tkinter

URL = "http://de76dev01:8080/view/ACT3/api/python?pretty=true"

def getColorSetFromJenkins():
    try:
        jsonJenkinsOutput = eval(urllib.urlopen(URL).read())
    except:
        return ["not_connected"]
        
    colorSet = []
    for job in jsonJenkinsOutput["jobs"]:
        colorSet.append(job["color"])
    colorSet = set(colorSet)
    return colorSet

def shouldColorBlink(colorSet):
    for color in colorSet:
        if "_anime" in color:
            return True
    return False

def getMainColor(colorSet):
    if "not_connected" in colorSet:
        return "blue"
    if "red" in colorSet or "red_anime" in colorSet:
        return "red"
    if "yellow" in colorSet or "yellow_anime" in colorSet:
        return "yellow"
    if "aborted" in colorSet or "aborted_anime" in colorSet:
        return "grey"
    if "blue" in colorSet or "blue_anime" in colorSet:
        return "lawn green"

def quitApplication(root):
    master.destroy()

if __name__ == '__main__':

    master = Tkinter.Tk()
    
    master.minsize(300,300)
    master.focus_set()
    master.geometry("500x500")
    #master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
    master.configure(background = "green")
    master.bind('<Escape>', quitApplication)
    
    while True:
        colorSet = ["yellow", "blue_anime"]
        colorSet = getColorSetFromJenkins()
        
        mainColor = getMainColor(colorSet)
        
        master.configure(background = mainColor)
        master.update()
        time.sleep(2)
        
        if shouldColorBlink(colorSet):
            master.configure(background = "black")
            master.update()
            time.sleep(1)
