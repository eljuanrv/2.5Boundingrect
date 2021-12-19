import cv2
import numpy as np

cap = cv2.VideoCapture(0)

verdeClaro = np.array([60,0,0],np.uint8)
verdeOscuro = np.array([120,255,255],np.uint8)
while(True):
    ret,frame = cap.read()

    if (ret == True):
        frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frameHSV,verdeClaro,verdeOscuro)
        contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        #solo toma los contornos externos, los internos los ignora   
        #realiza una aproximacion comprimida de la representacion de los contornos
        for c in contornos:
            area=cv2.contourArea(c)
            if area>3000:
                xr,yr,w,h=cv2.boundingRect(c) #calcula el rect que lo redea
                cv2.rectangle(frame,(xr,yr),(xr+w,yr+h),(255,0,0),3) #dibuja el rect
                (xc,yc),radio=cv2.minEnclosingCircle(c) #lo calcula
                #tarea: encontrar el centro del circulo por moments

                M = cv2.moments(c)
                xm=M['m10']/M['m00']
                ym=M['m01']/M['m00']
                centro=(int(xm),int(ym))
                #centro=(int(xc),int(yc))
                radio=int(radio)
                cv2.circle(frame,centro,radio,(33,243,238),3) #lo dibuja
        cv2.imshow('Frame',frame)
        cv2.imshow('Mascara',mask)
        if( cv2.waitKey(1) & 0xFF == ord('s')):
            break
cap.release()
cv2.destroyAllWindows()