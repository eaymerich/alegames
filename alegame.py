#!/usr/bin/env python3

# MIT License
#
# Copyright (c) 2017 Edward Aymerich
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pygame

# Color constants
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# Screen resolution
screen_width = 1024
screen_height = 768

# Global variables
done = False
screen = None
currentColor = RED


def drawTriangle():
    half_x = screen_width // 2
    quarter_x = screen_width // 4
    quarter_y = screen_height // 4

    vertices = [
        [half_x, quarter_y],
        [quarter_x * 3, quarter_y * 3],
        [quarter_x, quarter_y * 3]
    ]

    pygame.draw.polygon(screen, currentColor, vertices)


def drawSquare():
    width = screen_width // 2
    height = screen_height // 2
    if width > height:
        width = height
    else:
        height = width
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    rect = [x, y, width, height]

    pygame.draw.rect(screen, currentColor, rect)


def drawCircle():
    center_x = screen_width // 2
    center_y = screen_height // 2
    if center_y < center_x:
        radius = center_y // 2
    else:
        radius = center_x // 2
    pygame.draw.circle(screen, currentColor, (center_x, center_y), radius)


drawShape = drawSquare


def changeColor():
    global currentColor
    if currentColor == RED:
        currentColor = GREEN
    elif currentColor == GREEN:
        currentColor = BLUE
    elif currentColor == BLUE:
        currentColor = RED


def handleKeyDown(event):
    global done, drawShape
    if event.mod == pygame.KMOD_LSHIFT and event.key == pygame.K_ESCAPE:
        done = True
    elif event.key == pygame.K_SPACE:
        changeColor()
    elif event.key == pygame.K_q:
        drawShape = drawSquare
    elif event.key == pygame.K_y:
        drawShape = drawTriangle
    elif event.key == pygame.K_p:
        drawShape = drawCircle


def processEvents():
    global done
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            handleKeyDown(event)


def main():
    global done, screen

    # Screen size
    SIZE = (screen_width, screen_height)

    # Init PyGame
    pygame.init()

    # Setup screen
    # screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Ale Game')

    # Get clock
    clock = pygame.time.Clock()

    # Main loop
    while not done:
        processEvents()

        screen.fill(WHITE)
        drawShape()

        pygame.display.flip()
        clock.tick(60)

    # End PyGame
    pygame.quit()


if __name__ == '__main__':
    main()
