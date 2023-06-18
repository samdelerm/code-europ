from math import radians
import math
import rsk
from math import *
import time
import numpy as np
from rsk import constants
color = "blue"
opponentColor = "green" if color == "blue" else "blue"
attaquantTempsProcheBalle = time.time()

def Defenseur(xball,yball):
    if client.ball is not None:
      if client.referee["teams"]["blue"]["robots"]["1"]["penalized"] is True:
             if xball<=xb1:
                    if client.blue2.goto((xball+k, yb1, radians(180)+ANGLe), wait=False):
                            print('coordonée ou va le robot')
                            print(xball+k, yb1)
                            client.blue2.kick(1)
                            client.blue2.kick()
        
      else: 
        if xball<client.blue2.position[0] and yball<0.30 and yball>-0.30:
                client.blue2.goto((0.80, yball, radians(180)), wait=False)
        if yball>-0.30 and yball<0.30 and xball>0.60 and xball<0.92:
            client.blue2.goto((xball+k,yball, radians(180)), wait=False)
            client.blue2.kick()
            client.blue2.kick()
        else: 
            if yball>=0.30:
                client.blue2.goto((0.80, 0.30, radians(180)))  
            else: 
                if yball<=-0.30:
                    client.blue2.goto((0.80, -0.30, radians(180)))
        return
def Attaquant(xball,yball,xb1,yb1,k,ANGLe):
            if client.ball is not None:
                if client.referee["teams"]["blue"]["robots"]["2"]["penalized"] is True:
                         if client.ball is not None:
                            if xball<client.blue1.position[0] and yball<0.30 and yball>-0.30:
                                client.blue1.goto((0.80, yball, radians(180)), wait=False)
                            if yball>-0.30 and yball<0.30 and xball>0.60 and xball<0.92:
                                client.blue1.goto((xball+k,yball, radians(180)), wait=False)
                                client.blue1.kick()
                                client.blue1.kick()
                            else: 
                                if yball>=0.30:
                                    client.blue1.goto((0.80, 0.30, radians(180)))  
                                else: 
                                    if yball<=-0.30:
                                         client.blue1.goto((0.80, -0.30, radians(180)))
                else:
                    if xball<=xb1:
                        if client.blue1.goto((xball+k, yb1, radians(180)+ANGLe), wait=False):
                            client.blue1.kick(1)
                            client.blue1.kick()
                    else :
                        if client.blue1.goto((xball+k-1, yball-100, radians(180)), wait=False):
                            client.blue1.kick()
                            client.blue1.kick()
                     


with rsk.Client(host='localhost',key='') as client:
   
   def test(dista):
        global attaquantTempsProcheBalle
        if dista>=0.25:
            attaquantTempsProcheBalle=time.time()
        elif (time.time() - attaquantTempsProcheBalle) >=2.5:
            print("ball abuse")
            xball=client.ball[0]
            yball=client.ball[1]
            print(xball)
            balle = np.array([xball, yball])
            posRobot = client.blue1.position
            entreBalleEtRobot = posRobot - balle
            entreBalleEtRobot = entreBalleEtRobot*1000
            print(entreBalleEtRobot)
            client.blue1.goto((xball+entreBalleEtRobot[0],yball+entreBalleEtRobot[1], radians(0)),wait=False)

   while True: 
        try:
            
            goal = client.robots[color][2]
            attacker = client.robots[color][1]
            ball = client.ball
            xball=client.ball[0]
            yball=client.ball[1] 
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
             xball=client.ball[0]
             yball=client.ball[1] 
             k=0.07 #a changer a chaque match en fonction de la caméra...
             xb1=xball+k#test
             yb1=yball+(yball/(xball+0.92))*k #test
             ANGLe=(math.atan((yb1-yball)/k))
             dist=client.ball[0 and 1]-client.blue1.position[0 and 1]
        except Exception as e:
         print(e)

    