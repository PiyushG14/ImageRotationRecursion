import numpy as np
import cv2

count = 0
def rotate(img,x, y, width):
    
    temp = np.copy(img[y:y + width, x:x + width])
    img[y:y + width, x:x + width] = img[y+width:y + 2* width, x:x + width]
    img[y+width:y + 2* width, x:x + width] = img[y + width : y + 2* width, x+ width :x + 2 * width]
    img[y + width : y + 2* width, x+ width :x + 2 * width] = img[y:y+width, x+width : x + 2* width]
    img[y:y+width, x+width : x + 2* width] = temp
    
    global count    
    width = width //2    
    count += 1     
    if count % 100 == 0:        
        cv2.imshow('img',img)
        cv2.waitKey(1)
    
    if width == 0:
        return img

    #Width has been made half, hence *2 for quadrant
    if width > 0:           
        img = rotate(img,x, y, width)                      # Quadrant II
        img = rotate(img,x, y + 2*width , width)           # Quadrant III
        img = rotate(img,x + 2*width , y + 2*width, width) # Quadrant IV
        img = rotate(img,x + 2* width, y, width)           # Quadrant I
        
    return img

#Read the image
file_name = "test_img.jpg"
img = cv2.imread(file_name)
img_dim = img.shape[0]

#Rotating 4 times
for rotations in range(1):
    width = img_dim // 2
    x,y = 0,0    
    img = rotate(img, x, y, width)

cv2.imshow('Final',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    

