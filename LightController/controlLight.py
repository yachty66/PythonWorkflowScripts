#build with https://github.com/studioimaginaire/phue
from phue import Bridge
import config

b = Bridge(config.ipAddress)

#turn on light
def turnOnLight(color):
    b.set_light("Max", 'on', True)
    #find out id of my light 
    activateScene(color)
    
#turn off light
def turnOffLight():
    b.set_light("Max", 'on', False)
    
#acitvate scene
def activateScene(scene):
    if scene == "blue":
        b.run_scene("BlackHole", "WorkHard")
    elif scene == "yellow":
        b.run_scene("BlackHole", "Serotonin?")
    
#input function    
def inputFromUser():
    i = input()
    return i
    
#cli interaction
def console():
    print("1 blue \n2 yellow \n3 off")
    i = inputFromUser()
    if i != '1' and i != '2' and i != '3':
        print("wrong input")
        exit()
    if i == '1':
        turnOnLight("blue")
    elif i == '2':
        turnOnLight("yellow")
    elif i == '3':
        turnOffLight()
    pass
    
if __name__ == "__main__":
    console()
  