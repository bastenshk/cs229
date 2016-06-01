import pygame
from pygame.locals import *
import random
import copy


width = 300
height = 200
grid_size = 20
col_num = width / grid_size
row_num = height / grid_size

def is_snake(x, y, snake_x, snake_y):

    if (x, y) in zip(snake_x[1:], snake_y[1:]):
        return True
    else:
        return False

def into_queue((x, y), queue, visited, snake_x, snake_y):
    if (x, y) == food:
        return False
    elif x < 0 or x >= col_num:
        return False
    elif y < 0 or y >= row_num:
        return False
    elif (x, y) in queue:
        return False
    elif (x, y) in visited:
        return False
    elif is_snake(x, y):
        return False
    else:
        return True

def cal_distance(snake_x, snake_y, food):
    queue = [food]
    visited = []
    for y in range(row_num):
        for x in range(col_num):
            distance[y][x] = 99999

    distance[food[1]][food[0]] = 0

    while len(queue) != 0:
        head = queue[0]
        visited.append(head)
        up_grid = head[0], head[1] - 1
        down_grid = head[0], head[1] + 1
        left_grid = head[0] - 1, head[1]
        right_grid = head[0] + 1, head[1]
        
        # print "here"

        for grid in [up_grid, down_grid, left_grid, right_grid]:
            if into_queue(grid, queue, visited):
                queue.append(grid)
                # if distance[grid[1]][grid[0]] != 99999:
                distance[grid[1]][grid[0]] = distance[head[1]][head[0]] + 1
        queue.pop(0)


def det_ai(snake_x, snake_y, food):

