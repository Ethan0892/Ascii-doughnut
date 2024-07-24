import math
import numpy as np
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
A = 0
B = 0

# Size of the doughnut
WIDTH = 1920
HEIGHT = 1080

# Create a Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create NumPy arrays for z and b
z = np.zeros((HEIGHT, WIDTH))
b = np.full((HEIGHT, WIDTH), ' ', dtype=object)

# Create a surface for the doughnut
surf = pygame.Surface((WIDTH, HEIGHT))

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the b array and surface
    b.fill(' ')
    surf.fill((20, 20, 40))  # Set the background color to a dark blue

    # Create the doughnut
    for j in range(0, 628, 8):
        for k in range(0, 628, 4):
            c = math.sin(k)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(k)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(WIDTH / 2 + 600 * D * (l * h * m - t * n))  # Increased the radius to 600
            y = int(HEIGHT / 2 + 300 * D * (l * h * n + t * m))  # Increased the radius to 300
            if HEIGHT > y > 0 and WIDTH > x > 0:
                if D > z[y, x]:
                    z[y, x] = D
                    b[y, x] = ".,-~:;=!*#$@"[max(int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n)), 0)]
                    surf.set_at((x, y), (255, 255, 255))  # Set the pixel color to white

    # Blit the surface to the screen
    screen.blit(surf, (0, 0))

    # Update the display
    pygame.display.flip()

    # Update rotation angles
    A += 0.04
    B += 0.02

    # Cap framerate to reduce flicker and improve performance
    pygame.time.delay(40)