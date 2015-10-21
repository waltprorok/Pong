# Pong Game Code
# Version 2.0.1
# Coded By: Walter Prorok
# Original Music By: Walter Prorok
# ***Original Source Code URL Below***
# www.mediafire.com/view/igmkm0mt04a/pong+v1.0.py

import pygame
from  pygame.locals import *
from sys import exit
import random
import time
import sys, os

pygame.init()
pygame.joystick.init()

screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Pong Game")
pause = False

# creating 2 bars, a ball and background
back = pygame.Surface((640,480))
background = back.convert()
background.fill((0,0,0))
bar = pygame.Surface((10,50))
bar1 = bar.convert()
bar1.fill((0,0,255))
bar2 = bar.convert()
bar2.fill((255,0,0))
circ_sur = pygame.Surface((15,15))
circ = pygame.draw.circle(circ_sur,(0,255,0),(15/2,15/2),15/2)
circle = circ_sur.convert()
circle.set_colorkey((0,0,0))

# some definitions
bar1_x, bar2_x = 10. , 620.
bar1_y, bar2_y = 215. , 215.
circle_x, circle_y, = 307.5, 232.5
bar1_move, bar2_move = 0., 0.
speed_x, speed_y, speed_circ = 250., 250., 250.
bar1_score, bar2_score = 0,0

# clock and font objects
clock = pygame.time.Clock()

# Font and Size
font = pygame.font.SysFont("calibri", 40)

# Splash Screen
for i in range (5):
    image = pygame.image.load("splashscreen.png")
    image.set_alpha(i)
    logoimage = screen.blit(image,(0,0))
    pygame.display.flip()

pygame.time.delay(3)

# Music
pygame.mixer.music.load("Pattern2.mp3")
pygame.mixer.music.play(3)
clock = pygame.time.Clock()
clock.tick(10)
pygame.mixer.music.get_busy()
pygame.event.poll()
#clock.tick(10)	


# Game Over Screen Blit and winner
def gameover1():
	screen.blit(background,(0,0))
	frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
	text = font.render("YOU WON!!!       Game Over", True, (0,0,0))
	text1 = text.get_rect()
	text1.center = (320,40)
	background.blit(text, text1)
	done()

def gameover2():
	screen.blit(background,(0,0))
	frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
	text = font.render("Robot Won :(      Game Over", True, (0,0,0))
	text1 = text.get_rect()
	text1.center = (320,440)
	background.blit(text, text1)
	done()
#	playagin()

# Pause Defined
def done():
	screen.blit(background,(0,0))
	frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
	text = font.render("Press Escape To Exit", True, (255,255,255))
	text1 = text.get_rect()
	text1.center = (320,340)
	background.blit(text, text1)
	time.sleep(1.0)
	clock.tick(0)
#	playagain()

# !!!!!!!!!!!!!!!!!!!  WORK ON THIS CODE  !!!!!!!!!!!!!!!!!!!!!!!!!!!!

#def playagain():
#	pygame.init()

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_UP:
				bar1_move = -ai_speed
			elif event.key == K_DOWN:
				bar1_move = ai_speed
		elif event.type == KEYUP:
			if event.key == K_UP:
				bar1_move = 0.
			elif event.key == K_DOWN:
				bar1_move = 0.

# Pause Key Event Code	
		if event.type == KEYUP:
			if event.key == K_SPACE:
				if event.key == K_SPACE:
					pause = False
		
		if event.type == KEYUP:
			if event.key == K_RETURN:
				if event.key == K_RETURN:
					#pygame.init()
					playagain()

	while pause == False:
		for event in pygame.event.get():
			if event.type==KEYUP:
				if event.key == K_SPACE:
					pause = True
					clock.tick(0)
# IF pause is TRUE Stop clock.tick

	score1 = font.render(str(bar1_score), True,(255,255,255))
	score2 = font.render(str(bar2_score), True,(255,255,255))

# Who is the Winner
	if bar1_score == 5: 
		gameover1()
	if bar2_score == 5:			
		gameover2()
	
	screen.blit(background,(0,0))
	frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
	middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
	screen.blit(bar1,(bar1_x,bar1_y))
	screen.blit(bar2,(bar2_x,bar2_y))
	screen.blit(circle,(circle_x,circle_y))
	screen.blit(score1,(250.,210.))
	screen.blit(score2,(380.,210.))

	bar1_y += bar1_move

# movement of circle

	time_passed = clock.tick(50)
	time_sec = time_passed / 1000.0

	circle_x += speed_x * time_sec
	circle_y += speed_y * time_sec
	ai_speed = speed_circ * time_sec

# AI of the computer
	if circle_x >= 305.:
		if not bar2_y == circle_y + 7.5:
			if bar2_y < circle_y + 7.5:
				bar2_y += ai_speed
			if bar2_y > circle_y -42.5:
				bar2_y -= ai_speed
		else:
			bar2_y == circle_y + 7.5
	
	if bar1_y >= 420.: bar1_y = 420.
	elif bar1_y <= 10. : bar1_y = 10.
	if bar2_y >= 420.: bar2_y = 420.
	elif bar2_y <= 10.: bar2_y = 10.

	if circle_x <+ bar1_x + 10.:
		if circle_y >+ bar1_y - 7.5 and circle_y <+ bar1_y + 42.5:
			circle_x + 20.
			speed_x = -speed_x
	if circle_x >= bar2_x - 15.:
		if circle_y >= bar2_y - 7.5 and circle_y <+ bar2_y + 42.5:
			circle_x + 605.
			speed_x = -speed_x
	if circle_x < 5.:
		bar2_score += 1
		circle_x, circle_y = 320., 232.5
		bar1_y,bar_2_y = 215., 215.
	elif circle_x > 620.:
		bar1_score += 1
		circle_x, circle_y = 307.5, 232.5
		bar1_y, bar2_y = 215., 215.
	if circle_y <= 10.:
		speed_y = -speed_y
		circle_y = 10.
	elif circle_y >= 457.5:
		speed_y = -speed_y
		circle_y = 457.5

	pygame.display.update()	
