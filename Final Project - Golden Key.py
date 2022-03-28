from graphics import *
import random
import time

UPDATE_RATE=30
MAINBG_WW=700
MAINBG_WH=700
KEY_SIZE_HEIGHT=21
KEY_SIZE_WIDTH=42
CHEST_SIZE_HEIGHT=71
CHEST_SIZE_WIDTH=83
KEY_UPDATE_RATE=60
KEY_OUTLINE=3
KEY_NUMS=25
keyList=[]
moveX=[]
moveY=[]
xdir=[]
ydir=[]
direction=[1,-1]
xSpeed=[]
ySpeed=[]
KEY_MSPEED=1
GKEY_MSPEED=1
order=0
score=30

main_win=GraphWin("Golden Key", MAINBG_WW, MAINBG_WH, autoflush=False)
main_win.setBackground("lightyellow")
def gameover():
    GO=Text(Point(MAINBG_WW/2, MAINBG_WH/2), "Game Over")
    GO.setSize(36)
    GO.setTextColor("black")
    GO.setStyle("bold")
    GO.draw(main_win)
    update(UPDATE_RATE)
    time.sleep(5)
    GO.undraw()
    main_win.close()
def youwon():
    WON=Text(Point(MAINBG_WW/2, MAINBG_WH/2), "You Win")
    WON.setSize(36)
    WON.setTextColor("blue")
    WON.setStyle("bold")
    WON.draw(main_win)
    update(UPDATE_RATE)
    time.sleep(1)
    WON.undraw()
while 1:
    if order==0:
        order+=1
        GKxposition=random.randint(KEY_SIZE_WIDTH//2+1, MAINBG_WW-KEY_SIZE_WIDTH//2-1)
        GKyposition=random.randint(KEY_SIZE_HEIGHT//2+1, MAINBG_WH-KEY_SIZE_HEIGHT//2-1)
        GoldenKey=Image(Point(GKxposition,GKyposition),"GoldenKey.gif")
        GoldenKey.draw(main_win)
        GKmoveX=random.randint(10,20)
        GKmoveY=random.randint(10,20)
        GKxdir=random.choice(direction)
        GKydir=random.choice(direction)
        GKySpeed=random.randint(int(GKEY_MSPEED/GKEY_MSPEED), GKEY_MSPEED)
        GKxSpeed=random.randint(int(GKEY_MSPEED/GKEY_MSPEED), GKEY_MSPEED)
        for i in range (KEY_NUMS):
            xposition=random.randint(KEY_SIZE_WIDTH//2+1, MAINBG_WW-KEY_SIZE_WIDTH//2-1)
            yposition=random.randint(KEY_SIZE_HEIGHT//2+1, MAINBG_WH-KEY_SIZE_HEIGHT//2-1)
            keyList.append(Image(Point(xposition, yposition), "StoneKey.gif"))
            keyList[i].draw(main_win)
            moveX.append(random.randint(10,20))
            moveY.append(random.randint(10,20))
            xdir.append(random.choice(direction))
            ydir.append(random.choice(direction))
            ySpeedInit=random.randint(int(KEY_MSPEED/KEY_MSPEED), KEY_MSPEED)
            xSpeedInit=random.randint(int(KEY_MSPEED/KEY_MSPEED), KEY_MSPEED)
            xSpeed.append(xSpeedInit)
            ySpeed.append(ySpeedInit)
        while True:
            clickPoint = main_win.checkMouse()
            for x in range (KEY_NUMS):
                if keyList[x].getAnchor().getX() > (MAINBG_WW-KEY_SIZE_WIDTH//2):
                    xdir[x]=xdir[x]*-1
                if keyList[x].getAnchor().getX() < KEY_SIZE_WIDTH//2:
                    xdir[x]=xdir[x]*-1
                if keyList[x].getAnchor().getY() > (MAINBG_WH-KEY_SIZE_HEIGHT//2):
                    ydir[x]=ydir[x]*-1
                if keyList[x].getAnchor().getY() < KEY_SIZE_HEIGHT//2+1:
                    ydir[x]=ydir[x]*-1
                keyList[x].move(xSpeed[x]*xdir[x],ySpeed[x]*ydir[x])
            if GoldenKey.getAnchor().getX() > (MAINBG_WW-KEY_SIZE_WIDTH//2)-5:
                GKxdir=GKxdir*-1
            if GoldenKey.getAnchor().getX() < KEY_SIZE_WIDTH//2+5:
                GKxdir=GKxdir*-1
            if GoldenKey.getAnchor().getY() > (MAINBG_WH-KEY_SIZE_HEIGHT//2-5):
                GKydir=GKydir*-1
            if GoldenKey.getAnchor().getY() < KEY_SIZE_HEIGHT//2+5:
                GKydir=GKydir*-1
            GoldenKey.move(GKxSpeed*GKxdir,GKySpeed*GKydir)
            if clickPoint != None:
                ClickPointX=clickPoint.getX()
                ClickPointY=clickPoint.getY()
                GoldenKeyP1=GoldenKey.getAnchor().getX()
                GoldenKeyP2=GoldenKey.getAnchor().getY()
                GoldenKeyXmin=GoldenKeyP1-KEY_SIZE_HEIGHT/2
                GoldenKeyXmax=GoldenKeyP1+KEY_SIZE_HEIGHT/2
                GoldenKeyYmin=GoldenKeyP2-KEY_SIZE_WIDTH/2
                GoldenKeyYmax=GoldenKeyP2+KEY_SIZE_WIDTH/2
                score-=5
                print("Score:", score)
                if ClickPointX>GoldenKeyXmin and ClickPointX<GoldenKeyXmax:
                    if ClickPointY>GoldenKeyYmin and ClickPointY<GoldenKeyYmax:
                        for e in range(KEY_NUMS):
                            keyList[e].undraw()
                            GoldenKey.undraw()
                        break
                if score<=50:
                    GKEY_MSPEED=1
                    KEY_MSPEED+=1
                if score<0:
                    for e in range(KEY_NUMS):
                        keyList[e].undraw()
                        GoldenKey.undraw()
                        gameover()
            update(KEY_UPDATE_RATE)
    if score>50:
        GKEY_MSPEED+=1
        KEY_MSPEED+=1
    order-=1
    score+=10
    print("Score:", score)
    if score>=100:
        youwon()
    update(UPDATE_RATE)
