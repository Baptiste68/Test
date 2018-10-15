#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    This is use to define the classe object
"""

class McObjects():
    """
        This class is used to represent the objects that McGyver
        need to take
    """
    x_o, y_o = 0, 0

    def __init__(self, x_o, y_o, image, window):
        """
            Creating the object with coordinates, image and the window
        """
        self.x_o = x_o
        self.y_o = y_o
        self.image = image
        self.window = window

    def placeobj(self, wsol, wmurv, hmurh):
        """
            Placing the object according to the coordinates
        """
        self.window.blit(self.image, (self.x_o * wsol + wmurv * 2 / 3, \
        self.y_o * wsol + hmurh * 2 / 3))

    def get_abs_crd(self, wgrd):
        """
            Get the absolute position of the object
        """
        x_obj = self.x_o * wgrd
        y_obj = self.y_o * wgrd
        return x_obj, y_obj
