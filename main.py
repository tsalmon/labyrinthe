#!/usr/bin/python3
# -*- coding: utf-8 -*
import pygame
from pygame.locals import *
from classes import *
from constantes import *
#boucle jeu, ecran, accueil, init()

pygame.init()
fenetre=pygame.display.set_mode((450,450),FULLSCREEN)
fond = pygame.image.load(image_accueil).convert()
fenetre.blit(fond,(0,0))
pygame.display.flip()
continuer=1
menu=1
jouer=1
niveau=0
choix=0
arrivee=[]
while continuer:
    while menu:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                menu=0
                continuer=0
                jouer=0
            elif event.type == KEYDOWN:
                if event.key == K_F1:
                    
                    choix = "n1"
                elif event.key == K_F2:
                    
                    choix = "n2"
                
        if choix!=0:            
            niveau = Niveau(choix)
            niveau.generer()
            fenetre=niveau.affichage()
            menu=0
            depart=niveau.depart()
            arrivee=niveau.arrivee()
            dk=Joueur(depart[0],depart[1])
            fenetre.blit(dk.dk,(dk.pos_x*30,dk.pos_y*30))

    while jouer:
        pygame.display.flip()
        pygame.time.Clock().tick(30)
        if arrivee[0]==dk.pos_x and arrivee[1]==dk.pos_y:
            continuer=0
            print("Vous avez gagné")
            jouer=0
        for event in pygame.event.get():
            if event.type==QUIT:
                jouer=0
                continuer=0
            if event.type==KEYDOWN:
                if event.key==K_UP and dk.pos_y>0 and niveau.structure[dk.pos_x][dk.pos_y-1]!="m":
                    dk.up()
                elif event.key==K_DOWN and dk.pos_y<14 and niveau.structure[dk.pos_x][dk.pos_y+1]!="m":
                    dk.down()
                elif event.key==K_LEFT and dk.pos_x>0 and niveau.structure[dk.pos_x-1][dk.pos_y]!="m":
                    dk.left()
                elif event.key==K_RIGHT and dk.pos_x<14 and niveau.structure[dk.pos_x+1][dk.pos_y]!="m":
                    dk.right()
        fenetre=niveau.affichage()
        fenetre.blit(dk.dk,(dk.pos_x*30,dk.pos_y*30))
            
