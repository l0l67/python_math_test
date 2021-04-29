import cv2 as cv
import numpy as np
import random



circle1_pos_x = 50
circle1_pos_y = 50
delay = 0
x_drag = 0
y_drag = 0
override = False
key = cv.waitKey(1)

def get_pointer_coords(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv.EVENT_LBUTTONDOWN:
        mouseX,mouseY = x,y
        print(mouseX, mouseY)
        global delay
        global circle1_pos_x
        global circle1_pos_y
        global x_drag
        global y_drag

        delay = random.randint(50, 100)
        circle1_pos_x = mouseX
        circle1_pos_y = mouseY

        x_drag = random.randint(1, 10)
        y_drag = random.randint(1, 10)


while(True):
    img = np.zeros((500, 500, 3), np.uint8)

    

    cv.setMouseCallback('RGB', get_pointer_coords)

    cv.circle(img, (circle1_pos_x, circle1_pos_y), 10, (0, 150, 255), -1)

    

    if (circle1_pos_x < 500 and circle1_pos_x > 0 and circle1_pos_y < 500 and circle1_pos_y > 0) or override == True: 
        if delay > 0:
            circle1_pos_x += int(delay / x_drag)
            circle1_pos_y += int(delay / y_drag)
            delay -= 1
            override = False
    else:
        circle1_pos_y = 500 - circle1_pos_y
        circle1_pos_x = 500 - circle1_pos_x
        override = True


    
    cv.imshow('RGB', img)

    key = cv.waitKey(1)

    if key == ord('q'):
        break