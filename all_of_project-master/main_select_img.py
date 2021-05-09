from PIL import Image
import os
import shutil

key = 'y'

while key == 'y':
	my_width = int(input('Enter Width :  '))
	my_height = int(input('Enter Height :  '))

	output_folder = input('Enter Output Folder Name :  ')

	if not os.path.exists(output_folder):
		os.mkdir(output_folder)

	for filename in os.listdir('.'):
		if not filename.endswith((".png", "jpg", "jpeg")):
			continue
		image = Image.open(filename)
		width , height = image.size

		if width == my_width and height == my_height: ## image should be greated than the yor size
			shutil.copy(filename, output_folder)
			os.remove(filename)
		print('----------------------------------------------------')

	print('Done Resizing All Images')

	key = input('Do Want Repeat This Proccess...? ( y or n )')

