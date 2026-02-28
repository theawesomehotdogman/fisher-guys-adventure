import pygame
import random
from loadassets import *
import fishsys
import popups
pygame.init()
screen = pygame.display.set_mode((500,500))   
pygame.display.set_caption("Fish Game")
icon_image = pygame.image.load('daicon.png')
pygame.display.set_icon(icon_image)
money = 0
rodlevel = 1
locationlevel = 1
locationprice = 450
upgraderodprice = 200
def show_text(msg, x, y, color, size):
        fontobj= pygame.font.SysFont("freesans", size,bold=True,italic=False)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
clock = pygame.time.Clock()
cheats = False
endgame = False
def mainemenu():
    x1 = 0
    y1 = 0
    global cheats
    dagame = False
    credits = False
    global endgame
    while 1:  
        screen.fill((0,0,0))
        clock.tick(60)    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                engame = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x1,y1 = event.pos
                    if x1 >= 160 and x1 <= 300 and y1 >= 200 and y1 <= 260:
                        dagame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    credits = True
                if event.key == pygame.K_COMMA:
                    cheats = True
                    print("the")
                    cheatson.play()
                if event.key == pygame.K_PERIOD:
                    cheats = False
                    cheatdisabled.play()
                if event.key == pygame.K_DELETE:
                    erase()
                    cheatdisabled.play()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_c:
                    credits = False
                if event.key == pygame.K_HOME:
                    popups.nono()
            
                
        show_text("Fisher Guy's Adventure",30,40,(255,255,255),40)
        pygame.draw.rect(screen,(0,255,0),(160,200,140,60))
        show_text("Play",200,210,(255,255,255),30)
        if dagame:
            break
        if endgame:
            break
        if credits:
            show_text("The Game By Arthur Marx",125,400,(255,255,255),20)
            show_text("Press Delete Key To Erase Save",100,380,(255,255,255),20)
        pygame.display.update()
def save():
    global rodlevel
    global locationlevel
    global money
    global locationprice
    global upgraderodprice
    operations = [str(money), str(rodlevel), str(locationlevel),str(locationprice),str(upgraderodprice)]
    file =  open("save", "w")
    for value in operations:
        file.write(value + "\n")

def load():
    file = open("save","r")
    global rodlevel
    global locationlevel
    global money
    global locationprice
    global upgraderodprice
    things = []
    things = file.read().splitlines()
    money = int(things[0])
    rodlevel = int(things[1])
    locationlevel = int(things[2])
    locationprice = int(things[3])
    upgraderodprice = int(things[4])
    file.close()
def erase():
    file = open("save","w")
    file.write("0"+"\n")
    file.write("1"+"\n")
    file.write("1"+"\n")
    file.write("450"+"\n")
    file.write("200" + "\n")
    file.close()
def game():
   global money
   displayamount = money
   x = 0
   y = 0


   fishcaught = 0
   cooldown = 64
   cooldowntime = 0
   
   global cheats
   oncooldown = False
   infish = False
   global upgraderodprice
   global rodlevel 
   chance = 0
   times = [32,64,96]
   global locationprice
   global locationlevel
   numbercooldown = 0
   global endgame
   groundcolor = (0,255,0)
   
   music.set_volume(0.2)
   music.play(-1)
   load()
   pointerx = 430
   pointery = 100
   if locationlevel > 1:
       print("above")
       groundcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
   direction = False
   gotit = False
   while 1: 
        screen.fill((0,150,255))
        clock.tick(32)    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x,y = event.pos
                    if x >= 150 and x <= 250 and y >= 425 and y <= 475 and oncooldown == False:
                        # chance = random.randint(1,locationlevel)
                        # if chance == 1:
                        #     fishcaught = fishsys.pickcommon()
                        #     print(fishcaught)
                            
                        #     if fishcaught.weight > rodlevel:
                        #         fishcaught = fishsys.commontable[0]
                        # if chance == 2:
                        #     fishcaught = fishsys.pickrare()
                        #     if fishcaught.weight > rodlevel:
                        #         fishcaught = fishsys.raretable[0]
                        # if chance == 3:
                        #     fishcaught = fishsys.picklegendary()
                        #     if fishcaught.weight > rodlevel:
                        #         fishcaught = fishsys.pickrare()
                        infish = True
                        oncooldown = True
                        numbercooldown = random.randint(0,rodlevel)
                        print(numbercooldown)
                        cooldown = times[numbercooldown]
                        print(cooldown)
                        splash.play()
                    if x >= 25 and x <= 125 and y >= 425 and y <= 475 and rodlevel < 3:
                        if money >= upgraderodprice:
                            rodlevel += 1
                            money -= upgraderodprice
                            upgraderodprice *= 2
                            upgradesound.play()
                    if x >= 275 and x <= 375 and y >= 425 and y <= 475:
                        if money >= locationprice:
                            locationlevel += 1
                            money -= locationprice
                            locationprice += 500
                            groundcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                            upgradesound.play()
                    if x >= 400 and x <= 500 and y >= 0 and y <= 50:
                        save()
                        cheatson.play()    
            if event.type == pygame.KEYDOWN:
                if gotit:
                        gotit = False
                if event.key == pygame.K_SPACE:
                    if infish and gotit == False:
                        if (pointery + 7 >= 100 and pointery + 7 <= 120) or (pointery +7 <= 280 and pointery + 7 >= 260):
                            fishcaught = fishsys.pickrare()
                            print("caughtrare")
                        else:
                            fishcaught = fishsys.commontable[0]
                        infish = False
                        print(fishcaught)
                        money += fishcaught.value
                        oncooldown = True
                        cooldowntime = 0
                        cooldown = random.choice([32,64,96])
                        chaching.play()
                        gotit = True
                    
                if event.key == pygame.K_h:
                    save()
                if event.key == pygame.K_HOME:
                    if cheats:
                        money += 100
                        popups.yes()
                    else:
                        popups.nono()
                if event.key == pygame.K_END:
                    if cheats:
                        if money >= 100:
                            money -= 100
                            popups.yes()
                        else:
                            popups.nono()
                    else:
                        popups.nono()
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.stop()
                    return()
                    
                if event.key == pygame.K_m:
                    pygame.mixer.stop()
                    music.play()
        if endgame:
            break
        if infish:
            screen.blit(bar,(450,100))
            screen.blit(arrow,(pointerx,pointery))
        if direction:
            pointery += 10
        if direction == False:
            pointery -=10
        if pointery <= 80:
            direction = True
        if pointery >= 270: 
            direction = False
        screen.blit(fisherdude,(60,150))
        pygame.draw.rect(screen,groundcolor,(0,400,400,400))
        pygame.draw.rect(screen,(0,0,255),(400,400,300,300))
        show_text("$",0,0,(0,255,0),32)
        show_text(str(displayamount),20,0,(0,255,0),32)
        screen.blit(fishbutton,(150,425))
        if rodlevel <= 3:
            screen.blit(upgraderod,(25,425))
            show_text(str(upgraderodprice),70,447,(0,0,0),15)
        if gotit:
            screen.blit(youcaught,(100,100))
            screen.blit(fishcaught.image,(150,200))
            show_text("$"+str(fishcaught.value),175,300,(0,0,0),32)
            show_text(str(fishcaught.name),160,280,(0,0,0),20)
        if displayamount != money:
            if displayamount < money:
                displayamount += 2
            if displayamount > money:
                displayamount -= 1
        if oncooldown:
            screen.blit(stopwatch,(250,425))
            cooldowntime += 1
            if cooldowntime == cooldown:
                oncooldown = False
        if locationlevel != 3:
            screen.blit(upgradeloaction,(280,425))
            show_text(str(locationprice),325,447,(0,0,0),15)
        screen.blit(saveicon,(400,0))
        
        pygame.display.update()  
while 1:
    mainemenu()
    game()
           