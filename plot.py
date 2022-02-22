
from PIL import Image
import numpy
import os
path = os.getcwd()
import copy

inter=Image.open(path+'/Capture1.jpg')
img=copy.deepcopy(inter)
stopbar1=Image.new('RGB', (16, 3), 'red')
img.paste(stopbar1,(100,100))
img.save(path + '/final.jpg')

width,length=inter.size
inter= inter.resize((width*2,length*2), Image.ANTIALIAS)
inter.save(path + '/newinter.jpg')

#img = cv2.imread(path + '/Image/test_Image.png', cv2.IMREAD_GRAYSCALE)
img = Image.open(path + '/resize.jpg')  
up_img = Image.new('L', (648, 300), 'red') 
down_img = Image.new('L', (648, 600), 'white')  
up_img.save(path + '/up.png')
down_img.save(path + '/down.jpg')

img.paste(up_img,(100,200))
img.save(path + '/final.jpg')

up_img=Image.open(path + '/up.png')
up_img=up_img.rotate(60,expand=1)
up_img.save(path + '/up.png')


im2 = up_img.convert('RGBA')
rot = im2.rotate(60,expand=1)
fff = Image.new('RGBA', rot.size, (255, )*4)
out = Image.composite(rot,fff,rot)
out.convert(img.mode).save('test2.bmp')
