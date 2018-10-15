#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    This module host the Labyrinth class
"""

from random import choice, randint

class Labyrinth:
    """
    This class is used to generate the logic of the Labyrinth
    """

    width, height = 0, 0
    already, laby = [], []

    def __init__(self, width, height):
        """
            Create labyrinth by giving dimensions
        """
        self.width = width
        self.height = height
        self.laby = [([''] * self.height) for _ in range(self.width)]
        for i in range(self.width):
            for j in range(self.height):
                self.laby[i][j] = "_|"

    def visited(self, x_check, y_check):
        """
            Function to see if a given square as been already visited
        """
        return [x_check, y_check] in self.already

    def neighbours(self, x_ngb, y_ngb):
        """
            Function to find what case has not been visited around the given one
        """
        if x_ngb > 0 and not self.visited(x_ngb-1, y_ngb):
            yield (x_ngb - 1, y_ngb)
        if x_ngb + 1 < self.width and not self.visited(x_ngb + 1, y_ngb):
            yield (x_ngb + 1, y_ngb)
        if y_ngb > 0 and not self.visited(x_ngb, y_ngb - 1):
            yield (x_ngb, y_ngb - 1)
        if y_ngb + 1 < self.height and not self.visited(x_ngb, y_ngb + 1):
            yield (x_ngb, y_ngb + 1)

    def checkin(self, alist):
        """
            Function to check which already visited square still has available neighbours
        """
        j = len(alist) - 1
        while j >= 0:
            x_check, y_check = alist[j]
            if list(self.neighbours(x_check, y_check)):
                return (x_check, y_check)
            j = j - 1

    def generate_lab(self):
        """
            Function to generate the labyrinth
        """
        curx = randint(0, self.width - 1)
        cury = randint(0, self.height - 1)
        self.already.append([curx, cury])

        # As long as there is an available neighbours
        while isinstance(self.checkin(self.already), tuple):
            if  not list(self.neighbours(curx, cury)):
                compx, compy = self.checkin(self.already)
                nextx, nexty = choice(list(self.neighbours(compx, compy)))
                self.already.append([nextx, nexty])
                if nextx > compx:
                    self.laby[compx][compy] = self.laby[compx][compy].replace("_", " ")
                elif nextx < compx:
                    self.laby[nextx][nexty] = self.laby[nextx][nexty].replace("_", " ")
                elif nexty > compy:
                    self.laby[compx][compy] = self.laby[compx][compy].replace("|", " ")
                elif nexty < compy:
                    self.laby[nextx][nexty] = self.laby[nextx][nexty].replace("|", " ")
                curx = nextx
                cury = nexty
            else:
                nextx, nexty = choice(list(self.neighbours(curx, cury)))
                self.already.append([nextx, nexty])
                if nextx > curx:
                    self.laby[curx][cury] = self.laby[curx][cury].replace("_", " ")
                elif nextx < curx:
                    self.laby[nextx][nexty] = self.laby[nextx][nexty].replace("_", " ")
                elif nexty > cury:
                    self.laby[curx][cury] = self.laby[curx][cury].replace("|", " ")
                elif nexty < cury:
                    self.laby[nextx][nexty] = self.laby[nextx][nexty].replace("|", " ")
                curx = nextx
                cury = nexty

        self.laby[self.width -1][self.height - 1] = \
        self.laby[self.width -1][self.height - 1].replace("|", " ")

    def show_in_console(self):
        """
            Display the labyrinth in console for debug purpose
        """
        print(' '+'_' * self.height * 2)
        for i in range(self.width):
            if i == 0:
                print(' .'+''.join(self.laby[i]))
            else:
                print(' '+'|'+''.join(self.laby[i]))
