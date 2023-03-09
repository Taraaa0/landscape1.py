# pygame template

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT,MOUSEBUTTONDOWN

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)


screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
screen_color=(135, 206, 235)

cloud_x = 50
cloud_y = 50
cloud_x_speed=2
cloud_color=(255,255,255)
radius_c=22


right_cloud_x=600
right_cloud_y=48
right_cloud_x_speed=2

s_rain_x=150
s_rain_y=110
e_rain_x=150
e_rain_y=140

sun_x=376
sun_y=219
sun_color=(255, 204, 0)
radius=25
sun_y_speed=4
sun_x_speed=3


# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            print(event.pos)

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    if cloud_x + radius_c == WIDTH or cloud_x - radius_c==0:
            cloud_x_speed =-cloud_x_speed
    cloud_x+=cloud_x_speed
    if right_cloud_x + radius_c == WIDTH or right_cloud_x - radius_c==0:
        right_cloud_x_speed = -right_cloud_x_speed
    right_cloud_x-=right_cloud_x_speed
   
    
    # DRAWING
    screen.fill(screen_color)  # always the first drawing command
    # star
    pygame.draw.circle(screen,(135, 206, 235),(75,110),4)
    pygame.draw.circle(screen,(135, 206, 235),(105,125),4)
    pygame.draw.circle(screen,(135, 206, 235),(91,155),4)
    pygame.draw.circle(screen,(135, 206, 235),(180,125),4)
    pygame.draw.circle(screen,(135, 206, 235),(150,150),4)
    pygame.draw.circle(screen,(135, 206, 235),(210,155),4)
    pygame.draw.circle(screen,(135, 206, 235),(240,175),4)
    pygame.draw.circle(screen,(135, 206, 235),(145,185),4)
    pygame.draw.circle(screen,(135, 206, 235),(265,125),4)
    pygame.draw.circle(screen,(135, 206, 235),(295,170),4)
    pygame.draw.circle(screen,(135, 206, 235),(30,130),4)
    pygame.draw.circle(screen,(135, 206, 235),(40,185),4)
    pygame.draw.circle(screen,(135, 206, 235),(315,130),4)
    pygame.draw.circle(screen,(135, 206, 235),(345,165),4)
    pygame.draw.circle(screen,(135, 206, 235),(380,160),4)
    pygame.draw.circle(screen,(135, 206, 235),(400,125),4)
    pygame.draw.circle(screen,(135, 206, 235),(435,160),4)
    pygame.draw.circle(screen,(135, 206, 235),(500,160),4)
    pygame.draw.circle(screen,(135, 206, 235),(475,130),4)
    pygame.draw.circle(screen,(135, 206, 235),(570,145),4)
    pygame.draw.circle(screen,(135, 206, 235),(600,160),4)
    pygame.draw.circle(screen,(135, 206, 235),(545,160),4)
    pygame.draw.circle(screen,(135, 206, 235),(59,59),4)
    pygame.draw.circle(screen,(135, 206, 235),(135,58),4)
    pygame.draw.circle(screen,(135, 206, 235),(217,63),4)
    pygame.draw.circle(screen,(135, 206, 235),(289,70),4)
    pygame.draw.circle(screen,(135, 206, 235),(390,70),4)
    pygame.draw.circle(screen,(135, 206, 235),(530,19),4)
    pygame.draw.circle(screen,(135, 206, 235),(580,74),4)
    pygame.draw.circle(screen,(135, 206, 235),(601,108),4)
    pygame.draw.circle(screen,(135, 206, 235),(532,88),4)
    pygame.draw.circle(screen,(135, 206, 235),(447,65),4)
    pygame.draw.circle(screen,(135, 206, 235),(225,14),4)
    pygame.draw.circle(screen,(135, 206, 235),(413,12),4)
    # sun 
    pygame.draw.circle(screen,sun_color,(sun_x,sun_y), radius)
    sun_y-=sun_y_speed
    sun_x-=sun_x_speed
    if sun_y + radius == HEIGHT or sun_y - radius ==0 or sun_x + radius ==WIDTH or sun_x - radius ==0:
        screen_color=(0, 20, 40)
    #cloud
    pygame.draw.circle(screen,cloud_color,(cloud_x + 15,cloud_y - 1), radius_c)
    pygame.draw.circle(screen,cloud_color,(cloud_x + 45,cloud_y - 1), radius_c)
    pygame.draw.circle(screen,cloud_color,(cloud_x + 11,cloud_y + 25), radius_c)
    pygame.draw.circle(screen,cloud_color,(cloud_x + 45,cloud_y + 25), radius_c)
    pygame.draw.circle(screen,cloud_color,(cloud_x + 75,cloud_y - 1), radius_c)
    pygame.draw.circle(screen,cloud_color,(cloud_x + 80,cloud_y + 25), radius_c)
    pygame.draw.circle(screen,cloud_color,(right_cloud_x,right_cloud_y),radius_c)
    pygame.draw.circle(screen,cloud_color,(right_cloud_x - 26,right_cloud_y),radius_c)
    pygame.draw.circle(screen,cloud_color,(right_cloud_x - 55,right_cloud_y),radius_c)
    pygame.draw.circle(screen,cloud_color,(right_cloud_x,right_cloud_y + 34),radius_c)
    pygame.draw.circle(screen,cloud_color,(right_cloud_x - 27,right_cloud_y + 34),radius_c)
    pygame.draw.circle(screen,cloud_color,(right_cloud_x - 53,right_cloud_y + 34),radius_c)
# rain  move
    pygame.draw.line(screen,cloud_color, (s_rain_x - 44,s_rain_y),(e_rain_x - 44,e_rain_y - 15))
    pygame.draw.line(screen,cloud_color, (s_rain_x - 5,s_rain_y + 15),(e_rain_x - 5,e_rain_y))
    pygame.draw.line(screen,cloud_color, (s_rain_x + 25,s_rain_y),(e_rain_x + 25,e_rain_y - 15))
    pygame.draw.line(screen,cloud_color, (s_rain_x + 70,s_rain_y + 15),(e_rain_x + 70,e_rain_y))
    pygame.draw.line(screen,cloud_color, (s_rain_x + 110,s_rain_y),(e_rain_x + 110,e_rain_y - 15))
    pygame.draw.line(screen,cloud_color, (s_rain_x + 150,s_rain_y + 15),(e_rain_x + 150,e_rain_y -5))
    pygame.draw.line(screen,cloud_color, (s_rain_x + 180,s_rain_y),(e_rain_x + 180,e_rain_y - 15))
    pygame.draw.line(screen,cloud_color, (s_rain_x + 210,s_rain_y + 15),(e_rain_x + 210,e_rain_y))
    pygame.draw.line(screen,cloud_color, (s_rain_x + 235,s_rain_y),(e_rain_x + 235,e_rain_y - 15))
    pygame.draw.line(screen,cloud_color, (s_rain_x + 265,s_rain_y + 15),(e_rain_x + 265,e_rain_y))
    pygame.draw.line(screen,cloud_color, (s_rain_x + 290,s_rain_y),(e_rain_x + 290,e_rain_y -15))
    pygame.draw.line(screen,cloud_color, (s_rain_x + 315,s_rain_y + 15),(e_rain_x + 315,e_rain_y))
    pygame.draw.line(screen,cloud_color, (s_rain_x +335,s_rain_y),(e_rain_x + 335,e_rain_y -15))
    pygame.draw.line(screen,cloud_color, (s_rain_x + 360,s_rain_y),(e_rain_x + 360,e_rain_y - 15))
    pygame.draw.line(screen,cloud_color, (s_rain_x - 70,s_rain_y + 15),(e_rain_x - 70,e_rain_y))
    pygame.draw.line(screen,cloud_color, (s_rain_x - 100,s_rain_y),(e_rain_x - 100,e_rain_y - 15))
    pygame.draw.line(screen,cloud_color, (s_rain_x - 120,s_rain_y + 15),(e_rain_x - 120,e_rain_y))
    pygame.draw.line(screen,cloud_color, (s_rain_x -110,s_rain_y + 65),(e_rain_x - 110,e_rain_y + 50))
    pygame.draw.line(screen,cloud_color, (s_rain_x - 75,s_rain_y + 65),(e_rain_x - 75,e_rain_y + 40))
    pygame.draw.line(screen,cloud_color, (s_rain_x - 40,s_rain_y + 65),(e_rain_x - 40,e_rain_y + 50))
    pygame.draw.line(screen,cloud_color, (s_rain_x,s_rain_y + 50),(e_rain_x,e_rain_y + 35))
    pygame.draw.line(screen,cloud_color, (s_rain_x + 45,s_rain_y + 55),(e_rain_x + 45,e_rain_y + 40))
    pygame.draw.line(screen,cloud_color, (s_rain_x + 190,s_rain_y +55),(e_rain_x + 190,e_rain_y + 40))
    pygame.draw.line(screen,cloud_color,(s_rain_x + 115, s_rain_y + 50), (e_rain_x + 115,e_rain_y + 35))
    pygame.draw.line(screen,cloud_color, (s_rain_x + 265,s_rain_y + 65),(e_rain_x + 265,e_rain_y + 50))
    pygame.draw.line(screen,cloud_color, (s_rain_x + 340,s_rain_y + 55), (e_rain_x + 340,e_rain_y + 40))
    s_rain_y+=1
    e_rain_y+=1
    # grass and flowers
    pygame.draw.rect(screen,(0, 100, 0),(0,222,640,300))
    pygame.draw.circle(screen,(238,130,238),(150,255),6)
    pygame.draw.circle(screen,(255,182,193),(141,249),6)
    pygame.draw.circle(screen,(255,182,193),(159,249),6)
    pygame.draw.circle(screen,(255,182,193),(141,261),6)
    pygame.draw.circle(screen,(255,182,193),(159,261),6)
    pygame.draw.line(screen,(0,0,0),(150,262),(150,280))
    pygame.draw.circle(screen,(255,182,193),(150,244),6)
    pygame.draw.circle(screen,(255,182,193),(150,266),6)
    # plant
    pygame.draw.circle(screen, (50,205,50),(80,397),15)
    pygame.draw.circle(screen, (50,205,50),(93,383),15)
    pygame.draw.circle(screen, (50,205,50),(98,400),15)
    pygame.draw.circle(screen, (50,205,50),(214,329),15)
    pygame.draw.circle(screen, (50,205,50),(203,342),15)
    pygame.draw.circle(screen, (50,205,50),(220,348),15)
    pygame.draw.circle(screen, (50,205,50),(293,408),15)
    pygame.draw.circle(screen, (50,205,50),(279,423),15)
    pygame.draw.circle(screen, (50,205,50),(299,428),15)
    pygame.draw.circle(screen, (50,205,50),(36,253),15)
    pygame.draw.circle(screen, (50,205,50),(80,397),15)
    pygame.draw.circle(screen, (50,205,50),(20,269),15)
    pygame.draw.circle(screen, (50,205,50),(37,272),15)
    pygame.draw.circle(screen, (0,100,0),(1,219),15)
    pygame.draw.circle(screen, (0,100,0),(20,219),15)
    pygame.draw.circle(screen, (0,100,0),(40,219),15)
    pygame.draw.circle(screen, (0,100,0),(60,219),15)
    pygame.draw.circle(screen, (0,100,0),(80,219),15)
    pygame.draw.circle(screen, (0,100,0),(100,219),15)
    pygame.draw.circle(screen, (0,100,0),(120,219),15)
    pygame.draw.circle(screen, (0,100,0),(140,219),15)
    pygame.draw.circle(screen, (0,100,0),(160,219),15)
    pygame.draw.circle(screen, (0,100,0),(180,219),15)
    pygame.draw.circle(screen, (0,100,0),(200,219),15)
    pygame.draw.circle(screen, (0,100,0),(220,219),15)
    pygame.draw.circle(screen, (0,100,0),(240,219),15)
    pygame.draw.circle(screen, (0,100,0),(260,219),15)
    pygame.draw.circle(screen, (0,100,0),(280,219),15)
    pygame.draw.circle(screen, (0,100,0),(300,219),15)
    pygame.draw.circle(screen, (0,100,0),(320,219),15)
    pygame.draw.circle(screen, (0,100,0),(340,219),15)
    pygame.draw.circle(screen, (0,100,0),(360,219),15)
    pygame.draw.circle(screen, (0,100,0),(380,219),15)
    pygame.draw.circle(screen, (0,100,0),(400,219),15)
    pygame.draw.circle(screen, (0,100,0),(420,219),15)
    pygame.draw.circle(screen, (0,100,0),(440,219),15)
    pygame.draw.circle(screen, (0,100,0),(460,219),15)
    pygame.draw.circle(screen, (0,100,0),(480,219),15)
    pygame.draw.circle(screen, (0,100,0),(500,219),15)
    pygame.draw.circle(screen, (0,100,0),(520,219),15)
    pygame.draw.circle(screen, (0,100,0),(540,219),15)
    pygame.draw.circle(screen, (0,100,0),(560,219),15)
    pygame.draw.circle(screen, (0,100,0),(580,219),15)
    pygame.draw.circle(screen, (0,100,0),(600,219),15)
    pygame.draw.circle(screen, (0,100,0),(620,219),15)
    pygame.draw.circle(screen, (0,100,0),(640,219),15)
    pygame.draw.circle(screen, (50,205,50),(263,250),15)
    pygame.draw.circle(screen, (50,205,50),(277,256),15)
    pygame.draw.circle(screen, (50,205,50),(259,270),15)
    pygame.draw.circle(screen, (50,205,50),(580,226),15)
    pygame.draw.circle(screen, (50,205,50),(573,241),15)
    pygame.draw.circle(screen, (50,205,50),(590,243),15)
    pygame.draw.circle(screen, (50,205,50),(530,399),15)
    pygame.draw.circle(screen, (50,205,50),(542,417),15)
    pygame.draw.circle(screen, (50,205,50),(514,422),15)
    # house
    pygame.draw.rect(screen,(129,97,62),(420,280,150,100))
    pygame.draw.polygon(screen,(166,103,76),[(420,281),(495,206), (570,281)])
    pygame.draw.rect(screen,(0,0,0),(510,297,50,25))
    pygame.draw.rect(screen,(255,255,255),(523,301,25,15))
    pygame.draw.line(screen,(0,0,0),(535,301),(535,315))
    pygame.draw.line(screen,(0,0,0),(523,309),(548,309))
    pygame.draw.rect(screen,(0,0,0),(434,297,50,25))
    pygame.draw.rect(screen,(255,255,255),(448,301,25,15))
    pygame.draw.line(screen,(0,0,0),(460,301),(460,315))
    #sun
    pygame.draw.line(screen,(0,0,0),(448,309),(471,309))
    pygame.draw.rect(screen,(255,0,0),(485,330,30,50))
    pygame.draw.circle(screen, (0,0,0),(490,356),3)
    # flower
    pygame.draw.line(screen,(0,0,0),(358,322),(358,345))
    pygame.draw.circle(screen,(238,130,238),(358,313),6)
    pygame.draw.circle(screen,(255,182,193),(366,308),6)
    pygame.draw.circle(screen,(255,182,193),(350,308),6)
    pygame.draw.circle(screen,(255,182,193),(359,305),6)
    pygame.draw.circle(screen,(255,182,193),(351,320),6)
    pygame.draw.circle(screen,(255,182,193),(366,320),6)
    pygame.draw.circle(screen,(255,182,193),(359,325),6)

    
    
    
    
    
    
    
    

    
  
   
    
    
    
    
    
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
