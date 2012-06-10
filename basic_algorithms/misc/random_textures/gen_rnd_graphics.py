from __future__ import division

import math

import Image, ImageDraw
import numpy as np

#This is a perlin noise generating script

def generate_noise(w, h, rnd):
	noise = np.array(np.zeros(w*h))
	noise = noise.reshape((w,h))
	for x in xrange(w):
		for y in xrange(h):
			noise[x][y] = (rnd.random_integers(0, 32768) / 32768)
	return noise

def smoothnoise(w, h, x, y, noise):
	x_i = int(x)
	y_i = int(y)
	fract_x = x - x_i
	fract_y = y - y_i

	x1 = (x_i + w) % w
	y1 = (y_i + h) % h

	#Neighbour Values
	x2 = (x1 + w - 1) % w
	y2 = (y1 + h - 1) % h

	#smooth the noise with bilinear interpolation
	val = 0.0
	val += fract_x * fract_y * noise[x1][y1]
	val += fract_x * (1 - fract_y) * noise[x1][y2]
	val += (1 - fract_x) * fract_y * noise[x2][y1]
	val += (1 - fract_x) * (1 - fract_y) * noise[x2][y2]
	return val

def turbulence(w, h, x, y, noise, size):
	val = 0.0
	init_size = size
	while(size>=1):
		val += smoothnoise(w, h, x/size, y/size, noise) * size
		size /= 2.0
	
	return (128 * val/init_size)

def gen_img(w, h, seed=6712):
	img = Image.new("RGB", (w, h), "#FFFFFF")
	draw = ImageDraw.Draw(img)
	rnd = np.random.RandomState(seed)
	noise = generate_noise(w, h, rnd)
	for x in xrange(w):
		for y in xrange(h):
			r = g = b = int(turbulence(w, h, x, y, noise, 64))
			draw.point((x, y) , fill=(r, g, b))
	img.save("out.png", "PNG")

if __name__=="__main__":
	gen_img(640, 480)
