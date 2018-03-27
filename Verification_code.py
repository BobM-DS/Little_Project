# -*- encoding=utf-8 -*-
import random
import string
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

#generate a str contains four characters randomly
def random_text():
	text = string.digits + string.ascii_letters
	strcode = ''
	for i in range(0, 4):
		try:
			strcode = strcode + text[random.randint(0, len(text))]
		except IndexError:
			strcode = strcode + text[random.randint(0, len(text))]
	return strcode

def random_color():
	param = [random.randint(0, 256) for i in range(0, 3)]
	return param

def get_code(str_code):
	width = 120 #set width of picture
	height = 60 #set height of picture
	pack_color = random_color() #get background color
	color = (pack_color[0], pack_color[1], pack_color[2]) #set background color of picture
	image = Image.new('RGB', (width, height), color) #create pic

	font1 = ImageFont.truetype("simsun.ttc", 40, index=1) #set font style
	draw = ImageDraw.Draw(image) #draw the code on the picture
	
	param = random_color() #get font color
	draw.text((20, 10), str_code, fill=(param[0], param[1], param[2]), font=font1)
	image.show()


code = random_text()
get_code(code)
'''
input_code = input('Please input the code: ')
if code.lower() == input_code.lower():
	print("Fucking Right")
else:
	print("Dumn Fucking Wrong")
'''