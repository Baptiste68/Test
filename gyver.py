#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    This module is used for the Gyver class
"""
import pygame
import pygame.locals


class Gyver():
    """
        Generate the object that represent McGyver
    """
    xmac, ymac, dim = 0, 0, 0

    def __init__(self, xmac, ymac, image, window, dim):
        """
            Create the object
        """
        self.xmac = xmac
        self.ymac = ymac
        self.image = image
        self.window = window
        self.dim = dim

    def changepos(self, x_mc, y_mc):
        """
            Change McGyver position
        """
        self.xmac = x_mc
        self.ymac = y_mc

    def getrect(self):
        """
            Get the rectangle that represent McGyver
        """
        return pygame.Rect(self.xmac, self.ymac, self.dim, self.dim)

    def placemc(self):
        """
            Place the MyGyver image
        """
        self.window.blit(self.image, (self.xmac, self.ymac))
