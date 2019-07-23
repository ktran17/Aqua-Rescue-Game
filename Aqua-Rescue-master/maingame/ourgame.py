import pygame
import random
# pygame.init()
if not pygame.display.get_init():
    pygame.display.init()
if not pygame.font.get_init():
    pygame.font.init()
pygame.mixer.init() #comment in for music
pygame.event.get()

pygame.display.set_caption("Aqua Rescue")

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1120,630))
#backgrounds
startscreenbg = pygame.image.load("images/menuscreen.png")
levelscreen = pygame.image.load("images/levelscreen.png")
aboutpage = pygame.image.load("images/aboutbg.png")
creditspage = pygame.image.load("images/creditsbg.png")
# optionspage = pygame.image.load("")
# optionspage = pygame.image.load("images/OPTIONS.")
# hitSound = pygame.mixer.Sound("hit.wav")
def music(sound):
    if sound == 1:
        pygame.mixer.music.load("music/gameovermusic.mp3")
        pygame.mixer.music.play(0, 5)
    else:
        pygame.mixer.music.load("music/pixelparty.mp3") #comment in for music
        pygame.mixer.music.play(-1) # -1 will ensure the song keeps looping #comment in for music
    # print(sound)
# game music is 8 bit pixel party and game over music is moonlight sonata 8 bit
music(0)
#loading images
playgame = pygame.image.load("images/playgame.png")
playgamerect = playgame.get_rect()
playgamerect.center = ((1120/2,320))

options = pygame.image.load("images/options.png")
optionsrect = options.get_rect()
optionsrect.center = ((1120/2,400))

about = pygame.image.load("images/about.png")
aboutrect = about.get_rect()
aboutrect.center = ((1120/2,480))

credits = pygame.image.load("images/credits.png")
creditsrect = credits.get_rect()
creditsrect.center = ((1120/2,560))

back = pygame.image.load("images/back.png")
backrect = back.get_rect()
backrect.topleft = ((20,520))

#menu screen animation
animenu = [pygame.image.load("images/animenu/1.png"),pygame.image.load("images/animenu/2.png"),pygame.image.load("images/animenu/3.png"),pygame.image.load("images/animenu/4.png"),pygame.image.load("images/animenu/5.png"),pygame.image.load("images/animenu/6.png"),pygame.image.load("images/animenu/7.png"),pygame.image.load("images/animenu/8.png"),pygame.image.load("images/animenu/9.png"),pygame.image.load("images/animenu/10.png"),pygame.image.load("images/animenu/11.png"),pygame.image.load("images/animenu/12.png"),pygame.image.load("images/animenu/13.png"),pygame.image.load("images/animenu/14.png"),pygame.image.load("images/animenu/15.png"),pygame.image.load("images/animenu/16.png"),pygame.image.load("images/animenu/17.png"),pygame.image.load("images/animenu/18.png"),pygame.image.load("images/animenu/19.png"),pygame.image.load("images/animenu/20.png"),pygame.image.load("images/animenu/21.png"),pygame.image.load("images/animenu/22.png"),pygame.image.load("images/animenu/23.png"),pygame.image.load("images/animenu/24.png"),pygame.image.load("images/animenu/25.png"),pygame.image.load("images/animenu/26.png"),pygame.image.load("images/animenu/27.png"),pygame.image.load("images/animenu/28.png"),pygame.image.load("images/animenu/29.png"),pygame.image.load("images/animenu/30.png"),pygame.image.load("images/animenu/31.png"),pygame.image.load("images/animenu/32.png"),pygame.image.load("images/animenu/33.png"),pygame.image.load("images/animenu/34.png"),pygame.image.load("images/animenu/35.png"),pygame.image.load("images/animenu/36.png"),pygame.image.load("images/animenu/37.png"),pygame.image.load("images/animenu/38.png"),pygame.image.load("images/animenu/39.png"),pygame.image.load("images/animenu/40.png"),pygame.image.load("images/animenu/41.png"),pygame.image.load("images/animenu/42.png"),pygame.image.load("images/animenu/43.png"),pygame.image.load("images/animenu/44.png")]

animenurect = animenu[0].get_rect()
animenurect.centerx = (1120/2)
animenurect.top = 15
#dog images
dogright = [pygame.image.load("images/dright1.png"),pygame.image.load("images/dright2.png")]
dogleft = [pygame.image.load("images/dleft1.png"),pygame.image.load("images/dleft2.png")]
dogjetpack = [pygame.image.load("images/djetleft.png"),pygame.image.load("images/djetright.png")]
#dolphin images
dolphinleftnormal = [pygame.image.load("images/dolfinleft.png"),pygame.image.load("images/dolheadleft.png")]
dolphinleftgreen = [pygame.image.load("images/dolfinleftg.png"),pygame.image.load("images/dolheadleftg.png")]
dolphinrightnormal = [pygame.image.load("images/dolfinright.png"),pygame.image.load("images/dolheadright.png")]
dolphinrightgreen = [pygame.image.load("images/dolfinrightg.png"),pygame.image.load("images/dolheadrightg.png")]


escapeimg = [pygame.image.load("images/blackyes.png"),pygame.image.load("images/greenyes.png"),pygame.image.load("images/blackno.png"),pygame.image.load("images/greenno.png")]
gameoverimg = [pygame.image.load("images/whitemainmenu.png"),pygame.image.load("images/greenmainmenu.png"),pygame.image.load("images/whiteretry.png"),pygame.image.load("images/greenretry.png")]
optionsmusicimg = []
#more images
algae = pygame.image.load("images/algae.png")
# panel = pygame.image.load("panel.png")
# playgame = pygame.transform.scale(playgame, (int(playgame.get_width()), int(playgame.get_height()/6)))
# playgamerect = playgame.get_rect ()
# playgamerect.center = ((1120/2,630/2))
smoke = [pygame.image.load("images/smoke1.png"),pygame.image.load("images/smoke2.png"),pygame.image.load("images/smoke3.png"),pygame.image.load("images/smoke4.png"),pygame.image.load("images/smoke5.png")]
panel = pygame.image.load("images/panel.png")

imglist = [playgamerect, optionsrect, aboutrect, creditsrect]
imglistshow = [playgame, options, about, credits]
imgliststr = ["playgame", "options","about","credits"]
imglistrun = [False, False, False, False]

# fonts
font = pygame.font.Font('fonts/INVASION2000.ttf', 60)
fonttwo = pygame.font.Font('fonts/INVASION2000.ttf', 40)
fontthree = pygame.font.Font('fonts/INVASION2000.ttf', 20)
black = (0, 0, 0)
white = (255, 255, 255)

flag = False
# music = pygame.mixer.music.load("pixelparty.wav")
# pygame.mixer.music.play(-1)
# while pygame.mixer.music.get_busy():
#     clock.tick(16)
#     pygame.mixer.music.play(-1)

def escapeover(t):
    global flag
    if t <= 0:
        music(1)
        screen.fill(black)
        text = 'Game Over'
        color = white
        list = gameoverimg
        firsttop = 274
        secondtop = 280
        firstleft = 280
        secondright = 840
        print('game over')
    else:
        text = 'Escape to Main Menu?'
        color = black
        list = escapeimg
        firsttop = 285
        secondtop = 285
        firstleft = 420
        secondright = 700
        print('escape')
    maintext = font.render(text, True, color)
    maintextrect = maintext.get_rect()
    maintextrect.center = (560,200)
    screen.blit(maintext, maintextrect)
    firsttext = list[0]
    firsttextrect = firsttext.get_rect()
    firsttextrect.left = firstleft
    firsttextrect.top = firsttop
    secondtext = list[2]
    secondtextrect = secondtext.get_rect()
    secondtextrect.right = secondright
    secondtextrect.top = secondtop
    while 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if firsttextrect.right > pygame.mouse.get_pos()[0] > firsttextrect.left:
                    if firsttextrect.bottom > pygame.mouse.get_pos()[1] > firsttextrect.top:
                        flag = True
                        if text == 'Game Over':
                            music(0)
                        return
                if secondtextrect.right > pygame.mouse.get_pos()[0] > secondtextrect.left:
                    if secondtextrect.bottom > pygame.mouse.get_pos()[1] > secondtextrect.top:
                        if text == 'Game Over':
                            music(0)
                        return
        if firsttextrect.right > pygame.mouse.get_pos()[0] > firsttextrect.left:
            if firsttextrect.bottom > pygame.mouse.get_pos()[1] > firsttextrect.top:
                firsttext = list[1]
            else:
                firsttext = list[0]
        else:
            firsttext = list[0]
        if secondtextrect.right > pygame.mouse.get_pos()[0] > secondtextrect.left:
            if secondtextrect.bottom > pygame.mouse.get_pos()[1] > secondtextrect.top:
                secondtext = list[3]
            else:
                secondtext = list[2]
        else:
            secondtext = list[2]
        screen.blit(firsttext, firsttextrect)
        screen.blit(secondtext, secondtextrect)
        clock.tick(16)
        pygame.display.update()

def loading():
    x = 0
    y = 510
    dwalkcount = 0
    loopcount = 0
    while 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
        pygame.display.flip()
        clock.tick(16)
        screen.fill([175,104,196])
        screen.blit(dogright[dwalkcount//2], (x,y))
        # print(clock.get_fps()
        if loopcount <= 2:
            x += 15
            if loopcount <= 1:
                if x > 1120:
                    loopcount += 1
                    x = 0
                elif dwalkcount + 1 >= 4:
                    dwalkcount = 0
                else:
                    dwalkcount += 1
            else:
                screen.fill([175,104,196])
                loopcount += 1
        else:
            screen.fill([175,104,196])
            break
        # print("pupper")
# def redrawGamewindow():
#     global walkcount
#     win.blit(bg, (0,0))
#         if walkCount + 1 >= 27:
#             walkCount = 0
#         if left:
#             win.blit(dogjetpackleft[walkCount//3])
#             walkCount += 1
#     elif right:
#         win.blit(djetpackright[walkCount//3])
#         walkCount += 1
#         pygame.display.update()
def dogmove(x,y,lor): #music loop here right?
    height = 72
    width = 96
    vel = 15
    # left = False
    # right = False
    # walkcount = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and (not x < vel):
        x -= vel
        lor = 0
        return x,y,lor
    elif keys[pygame.K_RIGHT] and (not x > (1120-width-vel)) :
        x += vel
        lor = 1
        return x,y,lor
        # right = True
        # left = False
    # else:
    #  right = False
    #  left = False
    #  walkCount = 0
    # if not(isJump):
    elif keys[pygame.K_UP] and (not y < vel):  #if we don't need them moving up and down with the arrow keys keep both up and down commented out but leave in the space key
        y -= vel
        return x,y,lor
    elif keys[pygame.K_DOWN]and (not y > (630-height-vel)):
        y += vel
        return x,y,lor
    else:
        return x,y,lor
#     # screen.blit(dogjetpack[0], (585,600))
#     # redrawGameWindow()
def levelone(comp):
    global flag
    text = font.render('Level 1', True, black)
    textrect = text.get_rect()
    textrect.center = (560,315)
    screen.blit(levelscreen, (0,0))
    screen.blit(text, textrect)
    print('before wait')
    pygame.display.flip()
    pygame.time.wait(3000)
    print('after wait')
    dolphinx, dolphiny = 180, 220
    dolphindirection = "right"
    jetx, jety = 585, 525
    panelx, panely = 280, 510
    inventory = False
    inventorydone = False
    leftorright = 0
    dogrect = dogjetpack[leftorright].get_rect()
    dogrect.topleft = ((jetx,jety))
    randomcount = 0
    algaelist = []
    timer = 16 * 30 #change second number to change the seconds
    timertext = fontthree.render(str(timer/16),True,black)
    timertextrect = timertext.get_rect()
    timertextrect.topright = (1050,20)
    inventorytext = fontthree.render("inventory",True,black)
    while 1:
        if timer <= 0:
            break
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
        keys = pygame.key.get_pressed()
        if not inventorydone:
            if keys[pygame.K_SPACE]:
                print(inventory)
                if inventory:
                    print(panelx,panely)
                    panelx, panely = dogrect.topleft
                    inventory = False
                    print(panelx,panely, "two")
                    if 0 <= panelx <= 100 and 105 <= panely <= 205:
                        panelx, panely = 35, 140
                        inventorydone = True
                elif dogrect.right > panelx > dogrect.left or dogrect.right > panelx + 57> dogrect.left:
                    if dogrect.bottom > panely > dogrect.top or dogrect.bottom > panely + 33 > dogrect.top:
                        panelx, panely = 20, 588
                        inventory = True
        if keys[pygame.K_ESCAPE]:
            escapeover(timer)
        print("level one flag", flag)
        if flag:
            return comp
        jetx, jety, leftorright = dogmove(jetx, jety, leftorright)
        dogrect.topleft = ((jetx,jety))
        screen.blit(levelscreen, (0,0))
        if not inventorydone:
            if randomcount % 4 == 0:
                randomx = random.randint(250,1100)
                randomy = random.randint(20,460)
                algaelist.append((randomx,randomy))
            randomcount += 1
            screen.blit(smoke[(randomcount % 20)//4], (17,11))
        for item in algaelist:
            if dogrect.right > item[0] > dogrect.left or dogrect.right > item[0] + 33> dogrect.left:
                if dogrect.bottom > item[1] > dogrect.top or dogrect.bottom > item[1] + 27 > dogrect.top:
                    algaelist.remove(item)
            screen.blit(algae, item)
        if dolphindirection == "right":
            if dolphinx < 440:
                dolphinx += 5 #at end its at (440,220)
            elif dolphinx < 540:
                dolphinx += 5
                dolphiny += 7.5 #at end its at (540,370)
            elif dolphinx < 860:
                dolphinx += 8 #540->860 320
                dolphiny -= 7#370->90 280
             #at end its at (860,90)
            elif dolphinx < 1075:
                dolphinx += 5
            else:
                dolphindirection = "left"
        if dolphindirection == "left":
            if dolphinx > 860:
                dolphinx -= 5
            elif dolphinx > 540:
                dolphinx -= 8
                dolphiny += 7
            elif dolphinx > 440:
                dolphinx -= 5
                dolphiny -= 7.5
            elif dolphinx > 180:
                dolphinx -= 5
            else:
                dolphindirection = "right"


        timertext = fontthree.render(str(timer/16),True,black)
        screen.blit(timertext, timertextrect)
        timer -= 1
        screen.blit(inventorytext, (20,560))
        if len(algaelist) == 0:
            if dolphindirection == "right":
                if (timer%35)//7 == 0 or (timer%35)//7 == 1:
                    screen.blit(dolphinrightnormal[1],(dolphinx,round(dolphiny)))
                else:
                    screen.blit(dolphinrightnormal[0],(dolphinx,round(dolphiny)))
            else:
                if (timer%35)//7 == 0 or (timer%35)//7 == 1:
                    screen.blit(dolphinleftnormal[1],(dolphinx,round(dolphiny)))
                else:
                    screen.blit(dolphinleftnormal[0],(dolphinx,round(dolphiny)))
        else:
            if dolphindirection == "right":
                if (timer%35)//7 == 0 or (timer%35)//7 == 1:
                    screen.blit(dolphinrightgreen[1],(dolphinx,round(dolphiny)))
                else:
                    screen.blit(dolphinrightgreen[0],(dolphinx,round(dolphiny)))
            else:
                if (timer%35)//7 == 0 or (timer%35)//7 == 1:
                    screen.blit(dolphinleftgreen[1],(dolphinx,round(dolphiny)))
                else:
                    screen.blit(dolphinleftgreen[0],(dolphinx,round(dolphiny)))
        screen.blit(panel, (panelx,panely))
        screen.blit(dogjetpack[leftorright], dogrect)
        pygame.display.flip()
        clock.tick(16)
    # screen.fill((0,0,0))
    # text = font.render('Game Over', True, (255,255,255))
    # textrect = text.get_rect()
    # textrect.center = (560,315)
    # screen.blit(text, textrect)
    # pygame.display.flip()
    # pygame.time.wait(3000)
    if inventorydone and len(algaelist) == 0:
        comp = 1
        return comp
    else:
        escapeover(timer)
        return comp
def leveltwo(comp):
    global flag
    print('on level two')
    text = font.render('Level 2', True, black)
    textrect = text.get_rect()
    textrect.center = (560,315)
    screen.blit(levelscreen, (0,0))
    screen.blit(text, textrect)
    print('before wait')
    pygame.display.flip()
    pygame.time.wait(3000)
    dolphinx, dolphiny = 180, 220
    dolphindirection = "right"
    jetx, jety = 585, 525
    leftorright = 0
    dogrect = dogjetpack[leftorright].get_rect()
    dogrect.topleft = ((jetx,jety))
    timer = 16 * 30 #change second number to change the seconds
    timertext = fontthree.render(str(timer/16),True,black)
    timertextrect = timertext.get_rect()
    timertextrect.topright = (1050,20)
    while 1:
        if timer <= 0:
            break
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
        # if keys[pygame.K_SPACE]: #change to boat
            # if dogrect.right > panelx > dogrect.left or dogrect.right > panelx + 57> dogrect.left:
            #     if dogrect.bottom > panely > dogrect.top or dogrect.bottom > panely + 33 > dogrect.top:
            #         panelx, panely = 20, 588
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            escapeover(timer)
        if flag:
            return comp
        jetx, jety, leftorright = dogmove(jetx, jety, leftorright)
        dogrect.topleft = ((jetx,jety))
        screen.blit(levelscreen, (0,0))
        timertext = fontthree.render(str(timer/16),True,black)
        screen.blit(timertext, timertextrect)
        timer -= 1
        screen.blit(dogjetpack[leftorright], dogrect)
        pygame.display.flip()
        clock.tick(16)
#Menu functions
def gamefunction(levelcomplete):
    global flag
    while 1:
        print("levelcompleted",levelcomplete)
        # loading()
        if levelcomplete == 0:
            levelcomplete = levelone(levelcomplete)
        elif levelcomplete == 1:
            levelcomplete = leveltwo(levelcomplete)
        print("gamefunction flag", flag)
        if flag:
            print(levelcomplete)
            return levelcomplete
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
        # pygame.time.delay(100)
        # pygame.display.update()

def optionsfunction(nacomp):
    # x = 500
    # y = 500
    # display_surface = pygame.display.set_mode((x, y))
    # pygame.display.set_caption('Show Text')
    # font = pygame.font.Font(system, 32)
    # text = text.render("ON   OFF", True, purple)
    # textRect = text.get.rect()
    # textRect.center(x//2, y//2)

    # screen.blit(, (0, 0))
    screen.fill([255, 255, 255])
    screen.blit(back, backrect)
    # if event.type == MOUSEBUTTONDOWN:
    #     if event.pos[0] > :
    #         if m

    while 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backrect.right > pygame.mouse.get_pos()[0] > backrect.left:
                    if backrect.bottom > pygame.mouse.get_pos()[1] > backrect.top:
                        return nacomp
        pygame.display.flip()
        clock.tick(16)

def aboutfunction(nacomp):
    screen.blit(aboutpage, (0,0))
    screen.blit(back, backrect)
    while 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backrect.right > pygame.mouse.get_pos()[0] > backrect.left:
                    if backrect.bottom > pygame.mouse.get_pos()[1] > backrect.top:
                        return nacomp
        pygame.display.flip()
        clock.tick(16)

def creditsfunction(nacomp):
    screen.blit(creditspage, (0,0))
    screen.blit(back, backrect)
    while 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backrect.right > pygame.mouse.get_pos()[0] > backrect.left:
                    if backrect.bottom > pygame.mouse.get_pos()[1] > backrect.top:
                        return nacomp
        pygame.display.flip()
        clock.tick(16)

menufunc = [gamefunction, optionsfunction, aboutfunction, creditsfunction]
animenucount = 0

#main code
def mainmenu():
    global flag
    numlevelcomplete = 0
    animenucount = 0
    while 1:
        clock.tick(16)
        flag = False
        print("main menu flag",flag)
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                for image in range(len(imglist)):
                    if imglist[image].right > pygame.mouse.get_pos()[0] > imglist[image].left:
                        if imglist[image].bottom > pygame.mouse.get_pos()[1] > imglist[image].top:
                            numlevelcomplete = menufunc[image](numlevelcomplete)
        print(numlevelcomplete)
        animenucount += 1
        screen.blit(startscreenbg, (0,0))
        for image in range(len(imglist)):
            screen.blit(imglistshow[image], imglist[image])
        screen.blit(animenu[animenucount % 44], animenurect)
        pygame.display.flip()

mainmenu()
pygame.quit()


# x = 50
# y = 50
# width = 40
# height = 60
# vel = 10
#
# isJump = False
# jumpCount = 8
#
# run = True
# while run:
#     pygame.time.delay(10)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
    # keys= pygame.key.get_pressed()
    #
    # if keys[pygame.K_LEFT] and (not x < vel):
    #     x -= vel
    # if keys[pygame.K_RIGHT] and (not x > (1120-width-vel)) :
    #     x += vel
    #   if not(isJump):
    # if keys[pygame.K_UP] and (not y < vel):  #if we don't need them moving up and down with the arrow keys keep both up and down commented out but leave in the space key
    #     y -= vel
    # if keys[pygame.K_DOWN]and (not y > (630-height-vel)):
    #     y += vel
    #     if keys[pygame.K_SPACE]:
    #         isJump = True
    #  else:
    #     if jumpCount >= -8:
    #         neg = 1
    #         if jumpCount < 0:
    #             neg = -1
    #         y -= (jumpCount ** 2) * 0.5 * neg
    #         jumpCount -= 1
    #     else:
    #         isJump = False
    #         jumpCount = 8
#
#
    # screen.fill((0, 0, 0))
    # screen.blit(dogjetpack[0], (585,600))
    # pygame.mixer.quit()
# if __name__=='__main__':
#     cf.surface=pygame.display.set_mode((854, 480))bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
# boooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000oooooooooooooooooooooooooooooo
# ooooooooooboooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000oooooooooooooooooooooooooooooo
# oooooooooo
