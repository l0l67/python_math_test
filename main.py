import cv2 as cv
import numpy as np
import random



circle1_pos_x = 250
circle1_pos_y = 250
mouseX = 250
mouseY = 250
delay = 0
x_drag = 0
y_drag = 0
override = False
key = cv.waitKey(1)

def get_pointer_coords(event,x,y,flags,param):
    global mouseX,mouseY,delay,circle1_pos_x,circle1_pos_y,x_drag,y_drag

    if event == cv.EVENT_LBUTTONDOWN:
        mouseX,mouseY = x,y
        x_drag = random.randint(1, 10)
        y_drag = random.randint(1, 10)
        circle1_pos_x = 250
        circle1_pos_y = 250
        delay = 10



while(True):
    img = np.zeros((500, 500, 3), np.uint8)

    cv.setMouseCallback('RGB', get_pointer_coords)

    cv.circle(img, (circle1_pos_x, circle1_pos_y), 10, (0, 150, 255), -1)

    if (circle1_pos_x < 500 and circle1_pos_x > 0 and circle1_pos_y < 500 and circle1_pos_y > 0) or override == True: 
        if circle1_pos_x != mouseX and circle1_pos_y != mouseY:
            if delay < 10000:
                goto_x = int((mouseX -250))
                goto_y = int((mouseY -250))
                circle1_pos_x += int(goto_x / delay) 
                circle1_pos_y += int(goto_y / delay)
            delay += 1
            print(delay, circle1_pos_x ,circle1_pos_y)
            override = False
    else:
        circle1_pos_y = 500 - circle1_pos_y
        circle1_pos_x = 500 - circle1_pos_x
        override = True


    
    cv.imshow('RGB', img)

    key = cv.waitKey(1)

    if key == ord('q'):
        break