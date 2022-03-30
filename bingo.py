from PIL import Image
import random

print("Bingo Generator v1.11 (c) 2022, Michał Nikonowicz")

images_number = input("number of images: ")

a = 2
images = [[0 for x in range(a)] for y in range(int(images_number))]

for i in range(int(images_number)):
	images[i][0]=str(i+1)+".png"

img = Image.open("bingo.png")
used = 5
used = 0

random.seed(input("seed: "))


x = 0
y = 0

while used<25:
	r_number = random.randint(0, 25)
	for i in range(25):
		is_broken=0
		if images[r_number][1]==1:
			if r_number < (int(images_number)-1):
				r_number = r_number+1
			else:
				r_number = 0
			break
		else:
			images[r_number][1]=1
			used = used + 1
			img2 = Image.open(images[r_number][0])
			img.paste(img2, (x, y))
			x = x + 350
			if x > 1400:
				x = 0
				y = y + 350
			is_broken=1
		if is_broken==1:
			break
img.save("bingo_ready.png")