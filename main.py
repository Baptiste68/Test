#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This is the main of our program.
    It is initiating our different class and use Pygame functions
"""
from random import randint

import pygame
import pygame.locals

from labyrinth2D import Labyrinth2D
from mc_objects import McObjects
from gyver import Gyver

# Initialisation of the Labyrinth
LABYRINTH = Labyrinth2D(5, 5, 50, 20, 20)
LABYRINTH.generate_lab()
LABYRINTH.show_in_console()

# Taking the labyrinth variables
WIDTH = LABYRINTH.width
HEIGHT = LABYRINTH.height
WGRD = LABYRINTH.wgrd
HWALLH = LABYRINTH.hwallh
WWALLV = LABYRINTH.wwallv
LABY = LABYRINTH.laby

# Coordinates of objects
XNIDDLE = randint(0, WIDTH - 1)
YNIDDLE = randint(0, HEIGHT - 1)

XTUBE = randint(0, WIDTH - 1)
YTUBE = randint(0, HEIGHT - 1)

XETHER = randint(0, WIDTH - 1)
YETHER = randint(0, HEIGHT - 1)

# Taking window variable
WINDOW = LABYRINTH.window

def mctookobj(xobj, objects, xmc, ymc, objectstaken):
    """
        Check if McGyver take an object.
        If yes, the object go to taken objects
    """
    for obj in objects:
        x_obj, y_obj = obj.get_abs_crd(WGRD)
        if (x_obj <= xmc <= x_obj + WWALLV) and (y_obj <= ymc <= y_obj + WWALLV):
            objects.remove(obj)
            obj.x_o = HEIGHT + xobj
            obj.y_o = 1
            objectstaken.append(obj)
            xobj = xobj + 1
    return xobj

def canpass(objectstaken):
    """
        If McGyver has the 3 objects he can pass the last case
        Then it is a win
    """
    return len(objectstaken) == 3

def checkcol(nxmc, nymc, ngyver, mywalls):
    """
        Function to check if the possible next position is getting into a wall
        If so, we cannot move him
    """
    colide = False
    ngyver.changepos(nxmc, nymc)
    nextrect = ngyver.getrect()
    for wall in mywalls:
        if nextrect.colliderect(wall):
            colide = True
    return colide

def object_ini():
    """
        Function that initiate the 3 objects
        It is linking the image and placing it into the labyrinth
    """
    niddleimg = pygame.image.load("images/aiguille.png")
    niddleimg = pygame.transform.scale(niddleimg, (WWALLV, WWALLV))
    tubeimg = pygame.image.load("images/tube_plastique.png")
    tubeimg = pygame.transform.scale(tubeimg, (WWALLV, WWALLV))
    etherimg = pygame.image.load("images/ether.png")
    etherimg = pygame.transform.scale(etherimg, (WWALLV, WWALLV))

    niddle = McObjects(XNIDDLE, YNIDDLE, niddleimg, WINDOW)
    tube = McObjects(XTUBE, YTUBE, tubeimg, WINDOW)
    ether = McObjects(XETHER, YETHER, etherimg, WINDOW)

    objects = [niddle, tube, ether]
    objectstaken = []

    return objects, objectstaken

def place_obj(objects, objectstaken):
    """
        Function to place objects on the screen
    """
    for obj in objects:
        obj.placeobj(WGRD, WWALLV, HWALLH)
    for obj in objectstaken:
        obj.placeobj(WGRD, WWALLV + 5, HWALLH)

def place_guard(state):
    """
        Function that create and place the guard
    """
    # Get the xmax
    x_row, xmax = 0, 0
    for row in LABY:
        for col in row:
            x_row = x_row + WGRD
            if x_row > xmax:
                xmax = x_row
        x_row = 0

    guard = pygame.image.load("images/Gardien.png")
    guard = pygame.transform.scale(guard, (WWALLV, HWALLH))

    guardasleep = pygame.image.load("images/GuardASL.png")
    guardasleep = pygame.transform.scale(guardasleep, (WWALLV, HWALLH))

    if state == 1:
        WINDOW.blit(guard, (xmax + 5, (WIDTH - 1) * WGRD + HWALLH / 2))
    else:
        WINDOW.blit(guardasleep, (xmax + 5, (WIDTH - 1) * WGRD + HWALLH / 2))

    return xmax

def load_final(continuing):
    """
        Function to load the win or lost screen
    """
    while continuing != 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuing = 0
                return continuing
        pygame.display.update()
        winimg = pygame.image.load("images/win.png")
        winimg = pygame.transform.scale(winimg, (HEIGHT * WGRD + LABYRINTH.bigger, \
        WIDTH * WGRD))
        lostimg = pygame.image.load("images/lost.png")
        lostimg = pygame.transform.scale(lostimg, (HEIGHT * WGRD + LABYRINTH.bigger, \
        WIDTH * WGRD))
        if continuing == 2:
            WINDOW.blit(winimg, (0, 0))
        elif continuing == 3:
            WINDOW.blit(lostimg, (0, 0))

def mc_gyver_ini():
    """
        Initiate McGyver
    """
    mc_gyver_img = pygame.transform.scale(pygame.image.load("images/MacGyver.png"),\
    (WWALLV, HWALLH))
    # Coordinates of McGyver
    ymc = 0 + HWALLH / 2
    # Creation and placement of McGyver
    mc_gyver = Gyver(0, ymc, mc_gyver_img, WINDOW, WWALLV)
    # Place McGyver
    mc_gyver.placemc()
    # Possible McGyver's next position
    ngyver = Gyver(0, ymc, mc_gyver_img, WINDOW, WWALLV)

    return mc_gyver, ymc, ngyver


def main():
    """
        Main function of our program
        Include the loop for Pygame movement
    """
    pygame.init()
    clock = pygame.time.Clock()

    mywalls = LABYRINTH.mywalls
    x_change, y_change, xtake, xmc = 0, 0, 0, 0

    # Objects
    objects, objectstaken = object_ini()

    # Guard
    xmax = place_guard(1)

    # Mac Gyver
    mc_gyver, ymc, ngyver = mc_gyver_ini()

    LABYRINTH.draw_lab()

    # Infinite loop
    continuing = 1
    while continuing == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuing = 0

            # MyGyver moves 5 by 5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_UP:
                    y_change = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_DOWN:
                    y_change = 0
                if event.key == pygame.K_LEFT:
                    x_change = 0
                if event.key == pygame.K_UP:
                    y_change = 0

        if xmc + x_change >= xmax and ymc + y_change >= (WIDTH - 1) * WGRD:
            if canpass(objectstaken):
                continuing = 2
                break
            else:
                continuing = 3

        # Managing the movement accordingly with the collisions
        else:
            if x_change < 0 and xmc <= 0:
                xmc = xmc
            elif x_change != 0:
                if checkcol(xmc + x_change, ymc + y_change, ngyver, mywalls):
                    xmc = xmc
                else:
                    xmc = xmc + x_change

            if y_change < 0 and ymc == 10:
                ymc = ymc
            elif y_change != 0:
                if checkcol(xmc + x_change, ymc + y_change, ngyver, mywalls):
                    ymc = ymc
                else:
                    ymc = ymc + y_change

            # Otherwise we refresh the display
            LABYRINTH.mywalls = []
            LABYRINTH.draw_lab()
            xtake = mctookobj(xtake, objects, xmc, ymc, objectstaken)
            place_obj(objects, objectstaken)
            if canpass(objectstaken):
                place_guard(0)
            else:
                place_guard(1)
            mc_gyver.changepos(xmc, ymc)
            mc_gyver.placemc()
            pygame.display.update()
            clock.tick(60)

    if continuing == 2:
        load_final(continuing)

    if continuing == 3:
        load_final(continuing)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()

