from PIL import Image

def convertImage():
	img = Image.open("bg_img.jpg")
	img = img.convert("RGBA")

	datas = img.getdata()

	newData = []

	for item in datas:
		if item[0] == 255 and item[1] == 255 and item[2] == 255:
			newData.append((255, 255, 255, 0))
		else:
			newData.append(item)

	img.putdata(newData)
	img.save("new_image.png", "PNG")
	print("Successful")

convertImage()
