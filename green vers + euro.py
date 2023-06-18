from math import radians
import math
import rsk
from math import *
import time
import numpy as np
color = "blue"
opponentColor = "green" if color == "blue" else "blue"
attaquantTempsProcheBalle = time.time()
while True:
 def Defenseur(xball,yball):
    if client.ball is not None:
        if xball>client.blue2.position[0] and yball<0.30 and yball>-0.30:
                client.blue2.goto((-0.90, yball, radians(0)), wait=False)
        if yball>=-0.30 and yball<=0.30 and xball<=-0.50 and xball>=-0.94:
            client.blue2.goto((xball-0.10,yball, radians(0)), wait=False)
            client.blue2.kick(1)
            time.sleep(1)
            client.blue2.kick()
        else:
            if yball>0.30:
                client.blue2.goto((-0.90, 0.30, radians(0)))  
            else: 
                if yball<-0.30:
                    client.blue2.goto((-0.90, -0.30, radians(0)))
        if client.referee['teams']['blue']['robots']['1']['penalized'] is True:
                if xball<=xb1:
                    if client.blue2.goto((xball-k, yb1, -ANGLe), wait=False):
                        client.blue2.kick(1)
                        time.sleep(1)
                        client.blue2.kick()
        return
    

 def Attaquant(xball,yball,xb1,yb1,k,ANGLe):
    try:
            balle = np.array([xball, yball])
            posRobot = attacker.position
            entreBalleEtRobot = posRobot - balle
            entreBalleEtRobot = entreBalleEtRobot*100
            if client.ball is not None:
                if xball<=xb1:
                    if client.blue1.goto((xball-k, yb1, -1*ANGLe), wait=False):
                        client.blue1.kick(1)
                        time.sleep(1)
                        client.blue1.kick()
                else :
                    if client.blue1.goto((xball-k-entreBalleEtRobot[0], yball, radians(0)), wait=False):
                        client.blue1.kick()
                        time.sleep(1)
                        client.blue1.kick()
                if client.referee['teams']['blue']['robots']['2']['penalized'] is True:
                    if xball>client.blue1.position[0] and yball<0.30 and yball>-0.30:
                        client.blue1.goto((-0.90, yball, radians(0)), wait=False)
                    if yball>=-0.30 and yball<=0.30 and xball<=-0.50 and xball>=-0.94:
                        client.blue1.goto((xball-0.10,yball, radians(0)), wait=False)
                        client.blue1.kick(1)
                        time.sleep(1)
                        client.blue1.kick()
                    else:
                        if yball>0.30:
                         client.blue1.goto((-0.90, 0.30, radians(0)))  
                        else: 
                         if yball<-0.30:
                            client.blue1.goto((-0.90, -0.30, radians(0)))
            return
    except Exception as e:
        print(e)

 with rsk.Client(host='localhost',key='') as client:
  def test(dista):
    global attaquantTempsProcheBalle
    if dista>=0.25:
            attaquantTempsProcheBalle=time.time()
    elif (time.time() - attaquantTempsProcheBalle) >=1:
            print("ball abuse")
            print(xball)
            balle = np.array([xball, yball])
            posRobot = attacker.position
            entreBalleEtRobot = posRobot - balle
            entreBalleEtRobot = entreBalleEtRobot*1000
            print('iii',entreBalleEtRobot)
            attacker.goto((xball+entreBalleEtRobot[0],yball+entreBalleEtRobot[1], radians(0)),wait=False)

  while True:
        try:
            
            goal = client.robots[color][2]
            attacker = client.robots[color][1]
            ball = client.ball
            xball=ball[0]
            yball=ball[1] 
            dista=sqrt((ball[0]-attacker.position[0])**2+(ball[1]-attacker.position[1])**2) 
            test(dista)
            k=0.07 #a changer a chaque match en fonction de la caméra...
            xb1=xball+k#test
            yb1=yball+(yball/(xball+0.92))*k #test
            ANGLe=(math.atan((yb1-yball)/k))
            Attaquant(xball,yball,xb1,yb1,k,ANGLe)
            Defenseur(xball, yball)
            print("ANGLe=",(math.atan((yb1-yball)/k)))
            print("xball=",xball)
            print("xb1=",xb1)
        except Exception as e:
            print(e)
        try:
             Defenseur(xball,yball)
             Attaquant(xball,yball,xb1,yb1,k,ANGLe)
             goal = client.robots[color][2]
             attacker = client.robots[color][1]
             ball = client.ball
             xball=client.ball[0]
             yball=client.ball[1] 
             k=0.07 #a changer a chaque match en fonction de la caméra...
             xb1=xball+k#test
             yb1=yball+(yball/(xball+0.92))*k #test
             ANGLe=(math.atan((yb1-yball)/k))
             dista=sqrt((ball[0]-attacker.position[0])**2+(ball[1]-attacker.position[1])**2) 
             test(dista)

        except Exception as e:
         print(e)
# OK ce code marche mais n'a pas le time autour de la balle voila!!!