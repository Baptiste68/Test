#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    This module host the Labyrinth2D class
"""
import pygame
from pygame.locals import *

from labyrinth import *


class Labyrinth2D(Labyrinth):
    """
        This class is used to draw the laybrinth
        and to get the walls
    """
    wgrd, wwallv, hwallh = 0, 0, 0
    mywalls = []

    #initiating the structure
    def __init__(self, x, y, wgrd, hwallh, wwallv):
        super(Labyrinth2D, self).__init__(x, y)
        self.wgrd = wgrd
        self. hwallh = hwallh
        self.wwallv = wwallv
        self.bigger = 200
        self.window = pygame.display.set_mode((self.wgrd * self.height + self.bigger, \
        self.wgrd * self.width + 2))


        #Getting the different elements
        self.ground = pygame.image.load("images/ground.png")
        self.ground = pygame.transform.scale(self.ground, (self.wgrd, self.wgrd))

        self.groundend = pygame.image.load("images/groundend.png")
        self.groundend = pygame.transform.scale(self.groundend, (self.wgrd, self.wgrd))

        self.wallh = pygame.image.load("images/wallh.png")
        self.wallh = pygame.transform.scale(self.wallh, (self.wgrd, self.hwallh))

        self.wallv = pygame.image.load("images/wallv.png")
        self.wallv = pygame.transform.scale(self.wallv, (self.wwallv, self.wgrd))

        self.angle = pygame.image.load("images/angle.png")
        self.angle = pygame.transform.scale(self.angle, (self.wwallv, self.hwallh))

    #Drawing the Labyrinth in 2D
    def draw_lab(self):
        x_row, y_col, xmax = 0, 0, 0
        for row in self.laby:
            for col in row:
                self.window.blit(self.ground, (x_row, y_col))
                x_row = x_row + self.wgrd
                if x_row > xmax:
                    xmax = x_row
            y_col = y_col + self.wgrd
            x_row = 0

        self.window.blit(self.groundend, (xmax, y_col - self.wgrd))
        self.window.blit(self.wallh, (xmax, y_col - self.wgrd - self.hwallh / 2))
        self.window.blit(self.wallh, (xmax, y_col - self.hwallh / 2))

        # This loop is used to draw the Labyrinth according to the logic part (Labyrinth.py)
        # For each wall, we place the image of it
        # and we create a rectangle that represent the borders
        # We append the list of walls to later manage the collisions
        x, y, xl, yl = 0, 0, 0, 0
        for row in self.laby:
            for col in row:
                #Borders of the laby
                if y == 0:
                    wall = pygame.Rect(x, y - self.hwallh / 2, self.wgrd, self.hwallh)
                    self.window.blit(self.wallh, (x, y - self.hwallh / 2))
                    self.mywalls.append(wall)
                if y == (self.width - 1) * self.wgrd:
                    wall = pygame.Rect(x, y + self.wgrd - self.hwallh / 2, self.wgrd, self.hwallh)
                    self.window.blit(self.wallh, (x, y + self.wgrd - self.hwallh / 2))
                    self.mywalls.append(wall)
                if x == 0 and y != 0:
                    wall = pygame.Rect(x - self.wwallv / 2, y, self.wwallv, self.wgrd)
                    self.window.blit(self.wallv, (x - self.wwallv / 2, y))
                    self.mywalls.append(wall)
                if x == (self.height - 1) * self.wgrd and y != (self.width - 1) * self.wgrd:
                    wall = pygame.Rect(x + self.wgrd - self.wwallv / 2, y, self.wwallv, self.wgrd)
                    self.window.blit(self.wallv, (x + self.wgrd - self.wwallv / 2, y))
                    self.mywalls.append(wall)

                #inside of the laby
                if self.laby[xl][yl] == '_ ':
                    wall = pygame.Rect(yl * self.wgrd, xl * self.wgrd + self.wgrd - self.hwallh/2, \
                    self.wgrd, self.hwallh)
                    self.window.blit(self.wallh, (yl * self.wgrd, xl * self.wgrd + self.wgrd \
                    - self.hwallh/2))
                    self.mywalls.append(wall)
                if self.laby[xl][yl] == ' |':
                    wall = pygame.Rect(yl * self.wgrd + self.wgrd - self.wwallv / 2, xl * self.wgrd\
                    , self.wwallv, self.wgrd)
                    self.window.blit(self.wallv, (yl * self.wgrd + self.wgrd - self.wwallv / 2, \
                    xl * self.wgrd))
                    self.mywalls.append(wall)
                if  self.laby[xl][yl] == '_|':
                    wall = pygame.Rect(yl * self.wgrd + self.wgrd - self.wwallv / 2, xl * self.wgrd\
                    , self.wwallv, self.wgrd)
                    self.window.blit(self.wallv, (yl * self.wgrd + self.wgrd - self.wwallv / 2, \
                    xl * self.wgrd))
                    self.mywalls.append(wall)
                    wall = pygame.Rect(yl * self.wgrd, xl * self.wgrd + self.wgrd - self.hwallh/2, \
                    self.wgrd, self.hwallh)
                    self.window.blit(self.wallh, (yl * self.wgrd, xl * self.wgrd + self.wgrd \
                    - self.hwallh/2))
                    self.mywalls.append(wall)

                x = x + self.wgrd

                if yl < self.height - 1:
                    yl = yl + 1
            y = y + self.wgrd

            if xl < self.width - 1:
                xl = xl + 1
            x, yl = 0, 0
