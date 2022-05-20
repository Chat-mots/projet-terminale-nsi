import sys, pygame
from pygame.locals import *
import tkinter as tk

root =tk.Tk()
pygame.init()

hauteur = root.winfo_screenheight()
longueur = hauteur*(4/3)
print(hauteur,longueur)

black = (0, 0, 0)
grey = (200,200,200)
rouge = (255,100,100)
r_fonce = (255,50,50)
vert = (100,255,100)
v_fonce = (50,255,50)
blanc = (255,255,255)
mauve = (178,102,255)
bleu = (120, 120, 255)
screen = pygame.display.set_mode((longueur, hauteur))

a = 0
b = pygame.time.get_ticks()
font = pygame.font.SysFont(None, 24)

def collision(rectA, rectB):
    if rectB.right < rectA.left:
        return False
    if rectB.bottom < rectA.top:
        return False
    if rectB.left > rectA.right:
        return False
    if rectB.top > rectA.bottom:
        return False
    return True

depart = False

while True:
    a = pygame.time.get_ticks()
    if a - 1000 > b:
        b = a
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEWHEEL:
               print(event)
               
    pos_j = (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
    
    rect_depart = pygame.Rect(int((1/6)*longueur),int((6/9)*hauteur),int((1/6)*longueur),int((1/9)*hauteur))
    rect_j = pygame.Rect(pos_j[0]-10, pos_j[1]-15 , 20, 30)
    rect_col = pygame.Rect(int((7/12)*longueur),int((2/7)*hauteur),int((1/12)*longueur),int((7/9)*hauteur))
    rect_win = pygame.Rect(int((3/4)*longueur),int((7/9)*hauteur),int((1/8)*longueur),int((1/9)*hauteur))
    
    screen.fill(grey)
    
    if depart is False:
        pygame.draw.rect(screen, mauve, (rect_depart[0]-20, rect_depart[1]-30, rect_depart[2]+40, rect_depart[3]+60))
        pygame.draw.rect(screen, blanc, rect_depart)
        pygame.draw.rect(screen, rouge, rect_col)
        pygame.draw.rect(screen, vert, rect_win)
        pygame.draw.rect(screen, bleu, rect_j)
    
        img = font.render("PLACEZ VOUS DANS LE CERCLE GROS FDP", True, bleu)
        screen.blit(img, (20, 20))
        if collision (rect_j,rect_depart) is True:
            depart = True
   
    else:
        if collision(rect_j,rect_col) == True:
            pygame.mouse.set_pos(50,400)
    
        if collision(rect_j,rect_win) is True:
            print("Congratulations !")
            pygame.quit()
            sys.exit()
        pygame.draw.rect(screen, r_fonce, rect_col)
        pygame.draw.rect(screen, v_fonce, rect_win)
        pygame.draw.rect(screen, bleu, rect_j)
        font = pygame.font.SysFont(None, 24)
        img = font.render("C4EST parti mon kiki", True, (0,0,200))
        screen.blit(img, (20, 20))
    pygame.display.flip()
    
    
