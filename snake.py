# It is a class of the game


import pygame
from pygame.locals import *
import det_ai
import random
import copy
import sys

class Snake(object):


	def __init__(self):
		pygame.init()
		self.width = 300
		self.height = 200
		self.grid_size = 20
		self.col_num = self.width / self.grid_size
		self.row_num = self.height / self.grid_size
		self.top_gap = 70
		self.left_gap = 30

		self.screen = pygame.display.set_mode((self.width + self.left_gap * 2, self.height + self.top_gap * 2), 0, 32)
		self.clock = pygame.time.Clock()
		self.score = 0
		self.color = (0, 255, 0)

		self.snake_x = [5]
		self.snake_y = [5]

		self.snake_direction = "UP"
		self.speed = 10

		self.food = (1, 1)
		# self.running = True

		# self.screen.fill((255, 255, 255))
		# blit_grid()
		# pygame.draw.line(screen, (0, 0, 0), (left_gap - 2, top_gap - 2), (width + left_gap, top_gap - 2), 3)
	 #    # draw the bottom border
		# pygame.draw.line(screen, (0, 0, 0), (left_gap - 2, top_gap + height), (width + left_gap, top_gap + height), 3)
	 #    # draw the left border
		# pygame.draw.line(screen, (0, 0, 0), (left_gap - 2, top_gap - 2), (left_gap - 2, top_gap + height), 3)
	 #    # draw the right border
		# pygame.draw.line(screen, (0, 0, 0), (left_gap + width, top_gap - 2), (left_gap + width, top_gap + height), 3)


		# display_info()
		# draw_food(food)

	def get_snake(self):
		return self.snake_x, self.snake_y

	def get_food(self):
		return self.food


	def blit_grid(self):
	    
	    # for x in range(1, col_num):
	    #     pygame.draw.aaline(screen, (0, 0, 0),
	    #                        (left_gap + x * grid_size, top_gap),
	    #                        (left_gap + x * grid_size, height + top_gap))
	    # for y in range(1, row_num):
	    #     pygame.draw.aaline(screen, (0, 0, 0),
	    #                        (left_gap, y * grid_size + top_gap),
	    #                        (width + 30, y * grid_size + top_gap))

	    # draw the top border
	    pygame.draw.line(self.screen, (0, 0, 0), (self.left_gap - 2, self.top_gap - 2), (self.width + self.left_gap, self.top_gap - 2), 3)
	    # draw the bottom border
	    pygame.draw.line(self.screen, (0, 0, 0), (self.left_gap - 2, self.top_gap + self.height), (self.width + self.left_gap, self.top_gap + self.height), 3)
	    # draw the left border
	    pygame.draw.line(self.screen, (0, 0, 0), (self.left_gap - 2, self.top_gap - 2), (self.left_gap - 2, self.top_gap + self.height), 3)
	    # draw the right border
	    pygame.draw.line(self.screen, (0, 0, 0), (self.left_gap + self.width, self.top_gap - 2), (self.left_gap + self.width, self.top_gap + self.height), 3)





	def draw_snake(self):
    
	    for i in range(0, len(self.snake_x)):
			rect = pygame.Rect(self.left_gap + self.snake_x[i] * self.grid_size + 1,
	                           self.top_gap + self.snake_y[i] * self.grid_size + 1,
	                           self.grid_size - 1, self.grid_size - 1)
			pygame.draw.rect(self.screen, self.color, rect)

	    # Draw the head with a different color
	    rect = pygame.Rect(self.left_gap + self.snake_x[0] * self.grid_size + 1,
	                       self.top_gap + self.snake_y[0] * self.grid_size + 1,
	                       self.grid_size - 1, self.grid_size - 1)
	    pygame.draw.rect(self.screen, (100, 100, 100), rect)
	    pygame.display.update()


	def is_snake(self,x, y):
    
	    if (x, y) in zip(self.snake_x[1:], self.snake_y[1:]):
	        return True
	    else:
	        return False


	def add_snake(self, new_x, new_y):
	    
	    self.snake_x.insert(0, new_x)
	    self.snake_y.insert(0, new_y)
	    if (new_x, new_y) != self.food:
	        del self.snake_x[-1], self.snake_y[-1]
	    else:
	        self.score = self.score + 1
	        self.food = self.random_food()


	def snake_move(self):
		if self.snake_direction == "LEFT":
			new_x = self.snake_x[0] - 1
			new_y = self.snake_y[0]

		elif self.snake_direction == "RIGHT":
			new_x = self.snake_x[0] + 1
			new_y = self.snake_y[0]
		elif self.snake_direction == "UP":
			new_x = self.snake_x[0]
			new_y = self.snake_y[0] - 1
		elif self.snake_direction == "DOWN":
			new_x = self.snake_x[0]
			new_y = self.snake_y[0] + 1

		if new_x < 0 or new_x >= self.col_num or new_y < 0 or new_y >= self.row_num:
			self.snake_dead()
		else:
			self.add_snake(new_x, new_y)


	def snake_dead(self):
	    """
	    Do something while the snake is dead
	    """
	    print "dead"

	def random_food(self):
	    
	    rand_x = random.randint(0, self.col_num - 1)
	    rand_y = random.randint(0, self.row_num - 1)
	    while self.is_snake(rand_x, rand_y) or (rand_x, rand_y) == (self.snake_x[0], self.snake_y[0]):
	        rand_x = random.randint(0, self.col_num - 1)
	        rand_y = random.randint(0, self.row_num - 1)

	    self.draw_food((rand_x, rand_y))

	    # print "-"*80
	    # print "food:", food
	    return rand_x, rand_y


	def draw_food(self, (x, y)):
		rect = pygame.Rect(self.left_gap + x * self.grid_size + 1, self.top_gap + y * self.grid_size + 1,self.grid_size - 1, self.grid_size - 1)
	  	pygame.draw.rect(self.screen, (255, 0, 0), rect)
	  	pygame.display.update()


	def display_info(self):
	    my_font = pygame.font.SysFont('Comic Sans MS', 25)
	    title = "Score is "+ str(self.score)
	    game_info = my_font.render(title, True, (0, 0, 0), (57, 120, 158))
	    self.screen.blit(game_info, (self.width / 2 - 120, self.top_gap / 2 - 10))



	def player_play(self):
		self.screen.fill((255, 255, 255))
		self.blit_grid()
		self.display_info()
		self.draw_food(self.food)
		running = True
		while True:
		    for event in pygame.event.get():
		        if event.type == pygame.QUIT:
		            exit()

		        if event.type == KEYDOWN:
		            if event.key == K_p:
		                running = not running

		            if event.key == K_LEFT or event.key == K_a and self.snake_direction != "RIGHT":
		            	
		                self.snake_direction = "LEFT"

		            elif event.key == K_RIGHT or event.key == K_d and self.snake_direction != "LEFT":
		              	self.snake_direction = "RIGHT"

		            elif event.key == K_UP or event.key == K_w and self.snake_direction != "DOWN":
		                self.snake_direction = "UP"

		            elif event.key == K_DOWN or event.key == K_s and self.snake_direction != "UP":
		                self.snake_direction = "DOWN"

		    if not running:
		        continue

		    rect = pygame.Rect(self.left_gap + self.snake_x[-1] * self.grid_size + 1, self.top_gap + self.snake_y[-1] * self.grid_size + 1,
		                       self.grid_size - 1, self.grid_size - 1)
		    pygame.draw.rect(self.screen, (255, 255, 255), rect)

		    self.clock.tick(self.speed)
		    self.snake_move()
		    self.draw_snake()
		    self.display_info()
		    pygame.display.update()

	def AI_control(self):
		self.screen.fill((255, 255, 255))
		self.blit_grid()
		self.display_info()
		self.draw_food(self.food)
		running = True
		while True:
		    for event in pygame.event.get():
		        if event.type == pygame.QUIT:
		            exit()

		        if event.type == KEYDOWN:
		            if event.key == K_p:
		                running = not running

		    if not running:
		        continue

		    self.snake_direction = "RIGHT"

		    rect = pygame.Rect(self.left_gap + self.snake_x[-1] * self.grid_size + 1, self.top_gap + self.snake_y[-1] * self.grid_size + 1,
		                       self.grid_size - 1, self.grid_size - 1)
		    pygame.draw.rect(self.screen, (255, 255, 255), rect)

		    self.clock.tick(self.speed)
		    self.snake_move()
		    self.draw_snake()
		    self.display_info()
		    pygame.display.update()


