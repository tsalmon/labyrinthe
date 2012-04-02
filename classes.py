#!/usr/bin/python3
# -*- coding: utf-8 -*
import pygame
from pygame.locals import *
from constantes import *
#Niveau Perso

class Niveau:
    def __init__(self,level):
        self.niveau = level
        self.structure=None
        self.fenetre = pygame.display.set_mode((450,450),FULLSCREEN)
    def generer(self):
        struct=[]
        with open(self.niveau,"r") as Fichier:
            for i in Fichier:
                ligne=[]
                for j in i:
                    if j != "\n":
                        ligne.append(j)
                struct.append(ligne)
        self.structure=struct
    def affichage(self):
        mur = pygame.image.load(image_mur).convert()
        depart=pygame.image.load(image_depart).convert()
        arrivee=pygame.image.load(image_arrivee).convert_alpha()
        fond = pygame.image.load(image_fond).convert()
        self.fenetre.blit(fond,(0,0))
        for i in range(len(self.structure)):
            for j in range(len(self.structure[i])):
                if self.structure[i][j]=="a":
                    self.fenetre.blit(arrivee,(i*30,j*30))
                elif self.structure[i][j]=="m":
                    self.fenetre.blit(mur,(i*30,j*30))
                elif self.structure[i][j]=="d":
                    self.fenetre.blit(depart,(i*30,j*30))
        return self.fenetre

    def depart(self):
        for i in range(len(self.structure)):
            for j in range(len(self.structure[i])):
                if self.structure[i][j]=="d":
                    return [i,j]
    def arrivee(self):
        for i in range(len(self.structure)):
            for j in range(len(self.structure[i])):
                if self.structure[i][j]=="a":
                    return [i,j]
class Joueur:
    def __init__(self,x,y):
        self.dk=pygame.image.load(image_icone).convert_alpha()
        self.pos_x=x
        self.pos_y=y
    def up(self):
        self.pos_y-=1
        self.dk=pygame.image.load("images/dk_haut.png").convert_alpha()
    def down(self):
        self.pos_y+=1
        self.dk=pygame.image.load("images/dk_bas.png").convert_alpha()
    def left(self):
        self.pos_x-=1
        self.dk=pygame.image.load("images/dk_gauche.png").convert_alpha()
    def right(self):
        self.pos_x+=1
        self.dk=pygame.image.load("images/dk_droite.png").convert_alpha()
