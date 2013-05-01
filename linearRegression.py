import pygame, sys, os
from pygame.locals import *

from linearRegressionConstants import *
from gradientDescentOfCostFunction import gradientDescent, costFunction

# Main window setup
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAIN_WIDTH, MAIN_HEIGHT), 0, 0)
pygame.display.set_caption("Test")


# Draw phase
DISPLAYSURF.fill(WHITE)
fontObj = pygame.font.Font('freesansbold.ttf', FONT_SIZE)


##### Draw cartesian Plane

## Draw x axe
# Draw actual axe
pygame.draw.line(DISPLAYSURF, BLACK, BOTTOM_LEFT_BORDER, BOTTOM_RIGHT_BORDER, AXE_WIDTH)

# Draw his line 'arrow'
pygame.draw.lines(DISPLAYSURF, BLACK, False, [(475, 375), (480, 380), (475, 385)], AXE_WIDTH)

# Write what does x axe represent
textSurfaceObj = fontObj.render(X_AXE_WRITE, True, BLACK, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = X_AXE_WRITE_POSITION
DISPLAYSURF.blit(textSurfaceObj, textRectObj)

# Draw slashes on x axe (as for now, (10-1-1)=8 slashes seems good (start and end not drawn)
# every slash is the number 46*n, for n in range(8)
for x in range(20 + 460//10, 460, 460//10):
    pygame.draw.line(DISPLAYSURF, BLACK, (x, 375), (x, 385), 1)

# Write numbers on slashes on x axe. Numbers represent the house's size in squared metres
for x in range(20 + 460//10, 460, 460//10):
    # Subtract BORDER_DISTANCE=20 from x
    textSurfaceObj = fontObj.render(str(x-20), True, BLACK, WHITE)
    
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x, 390)

    DISPLAYSURF.blit(textSurfaceObj, textRectObj)


## Draw y axe
# Draw actual axe
pygame.draw.line(DISPLAYSURF, BLACK, BOTTOM_LEFT_BORDER, TOP_LEFT_BORDER, AXE_WIDTH)

# Draw his line 'arrow'
pygame.draw.lines(DISPLAYSURF, BLACK, False, [(15, 25), (20, 20), (25, 25)], AXE_WIDTH)

# Write what does y axe represent
textSurfaceObj = fontObj.render(Y_AXE_WRITE, True, BLACK, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = Y_AXE_WRITE_POSITION
DISPLAYSURF.blit(textSurfaceObj, textRectObj)

# Draw slashes on y axe (as for now, (8-1-1)=6 slashes seems good (start and end not drawn):
# every slash is the number 45*n, for n in range(6)
for y in range(20 + 360//8, 360, 360//8):
    pygame.draw.line(DISPLAYSURF, BLACK, (15, y), (25, y), 1)

# Write numbers on slashes on y axe. Numbers represent the house's price in thousands €
for y in range(20 + 360//8, 360, 360//8):
    # Subtract BORDER_DISTANCE=20 from y
    textSurfaceObj = fontObj.render(str(y-20), True, BLACK, WHITE)
    
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (10, 400-y)

    DISPLAYSURF.blit(textSurfaceObj, textRectObj)


## Draw center
textSurfaceObj = fontObj.render('O', True, BLACK, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (15, 385)
DISPLAYSURF.blit(textSurfaceObj, textRectObj)

### End of Draw cartesian Plane


# Draw points taken from houseStockPrice.txt as circles

# Open file with info about the houses. Format: '<squared metres>, <price/1000>\n'
with open("houseStockPrice.txt", "r") as f:
    a = ((line[:-1].split(',')) for line in f.readlines())
    trainingSet = [(float(couple[0]), float(couple[1])) for couple in a]

for point in trainingSet:
    circleCenter = (MAIN_BORDER + round(point[0]), MAIN_HEIGHT - MAIN_BORDER - round(point[1]))
    pygame.draw.circle(DISPLAYSURF, RED, circleCenter, CIRCLE_RADIUS, AXE_WIDTH)
    
##### End of Draw phase


##### Machine learning algorithm

# This is exactly the same loop inside the while
Theta0, Theta1 = THETA_0, THETA_1
tempTheta0, tempTheta1 = gradientDescent(Theta0, Theta1, ALPHA, trainingSet)
total = 1

# The small decimal value into the while means that, when the condition is no more
# true, then the two values are convergent, so we have our Theta0 and Theta1

while (abs(tempTheta0 - Theta0) > CONVERGENCY) or (abs(tempTheta1 - Theta1) > CONVERGENCY):
    Theta0 = tempTheta0
    Theta1 = tempTheta1
    tempTheta0, tempTheta1 = gradientDescent(Theta0, Theta1, ALPHA, trainingSet)
    #total = costFunction(tempTheta0, tempTheta1, ALPHA, trainingSet)
    #print("Cost function:", total)

# The while loop left the correct thetas values inside the temporary variables
Theta0 = tempTheta0
Theta1 = tempTheta1
print("\n\nFinal values: ",Theta0, Theta1)

##### End of Machine learning algorithm

### Plot my final line
# Compute two values: the first (start) if x=0; the second(end) if x=random value.
randomValue = 220

start = (MAIN_BORDER, MAIN_HEIGHT - MAIN_BORDER - Theta0)
end = (randomValue, MAIN_HEIGHT - MAIN_BORDER - Theta0 - (Theta1*randomValue))

pygame.draw.line(DISPLAYSURF, RED, start, end, AXE_WIDTH)
### End of Plot my final line

if 0:
    x = input("Quanti metri quadri e' la tua casa? ")
    y = Theta0 + (int(x)*Theta1)
    print("La casa costa",round(y),"mila euro")


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
