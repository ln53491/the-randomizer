import pygame
import os
from random import *

#Učitava sučelje i stvara gumbove, slike...
pygame.init();
screen = pygame.display.set_mode((400,400));
pozadina = pygame.image.load("files/pozadina.jpg").convert()
top = pygame.image.load("files/top.jpg").convert()
screen.blit(pozadina, [0, 0])
main = pygame.image.load("files/main.png")
screen.blit(main, [12, 215])
pygame.display.set_caption("Spitify");
play = pygame.image.load("files/play.png")
screen.blit(play, [136, 290])
pause = pygame.image.load("files/pause.png")
screen.blit(pause, [240, 327])
repeat = pygame.image.load("files/repeat.png")
screen.blit(repeat, [98, 327])
menuAtivo = True;

#Traži u root mapi sve pjesme čije nazive stavlja u liste te ih filtrira
f=[];f2=[];f3=[];f4=[]
for root, dirs, files in os.walk("songs"):  
    for c in files:
        f.append(c)
for c in f:
    if '.mp3' in c:
        f2.append(c)
for c in f2:
    if 'www.my-free-mp3.net' in c:
        f3.append(c.replace('www.my-free-mp3.net','').replace('.mp3','').strip())
    else:
        f3.append(c.replace('.mp3','').strip())
for c in f3:
    a=c[0:c.index('-')].strip()
    b=c[c.index('-')+1:].strip()
    f4.append(a);f4.append(b)

#Kreira sve tekstove
def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()
def text_objects1(text, font):
    textSurface = font.render(text, True, (255,155,0))
    return textSurface, textSurface.get_rect()

#Stvara ime kreatora i godinu proizvodnje
largeText = pygame.font.SysFont('Arial Black',13)
TextSurf, TextRect = text_objects1('By: Luka Nestić', largeText)
TextRect.center = (60,392)
screen.blit(TextSurf, TextRect) 
pygame.display.flip();
largeText = pygame.font.SysFont('Arial Black',13)
TextSurf, TextRect = text_objects1('2018', largeText)
TextRect.center = (380,392)
screen.blit(TextSurf, TextRect)
pygame.display.flip();

#Započinje glavni loop
br=[];f5=[i for i in range(len(f2))]
k=0;h=0
while menuAtivo:
    for event in pygame.event.get():
        #Definira lokaciju klika miša za pokretanje pjesama
        if event.type==pygame.MOUSEBUTTONDOWN:
            mišx,mišy=pygame.mouse.get_pos()
            k=1
            if mišx>=177 and mišx<=220 and mišy<=379 and mišy>=330:
                #Odabire random pjesmu (bez ponavljanja istih dok ne napravi puni krug)
                if len(f5)==0:
                    f5=[i for i in range(len(f2))]
                c=sample(f5,1)
                f5.remove(c[0])
                c=f2[c[0]]
                r=f2.index(c)
                pygame.mixer.music.load("songs/"+c)
                pygame.mixer.music.play()
                a=f3[r]
                #Prikazuje naslov pjesme te izvođača
                largeText = pygame.font.SysFont('Arial Black',20)
                TextSurf, TextRect = text_objects(a[a.index('-')+1:].strip(), largeText)
                TextRect.center = (203,150)
                screen.blit(top, [0, 0])
                screen.blit(TextSurf, TextRect)
                largeText = pygame.font.SysFont('Verdana',17)
                TextSurf, TextRect = text_objects(a[0:a.index('-')].strip(), largeText)
                TextRect.center = (200,110)
                screen.blit(TextSurf, TextRect)
                pygame.display.update()
            #Definira lokaciju i funkciju klika miša za ponovno pokretanje pjesme
            if mišx>=110 and mišx<=145 and mišy<=375 and mišy>=340:
                pygame.mixer.music.rewind()
            #Definira lokaciju i funkciju klika miša za pauziranje pjesme
            if mišx>=251 and mišx<=289 and mišy<=378 and mišy>=340 and h%2!=0:
                h+=1
                pygame.mixer.music.pause()
            else:
                h+=1
                pygame.mixer.music.unpause()
    #Ukoliko pjesma završi, program automatski svira sljedeću pjesmu (random)
    if pygame.mixer.music.get_busy()==False and k==1:
            if len(f5)==0:
                f5=[i for i in range(len(f2))]
            c=sample(f5,1)
            f5.remove(c[0])
            c=f2[c[0]]
            r=f2.index(c)
            pygame.mixer.music.load(c)
            pygame.mixer.music.play()
            a=f3[r]
            largeText = pygame.font.SysFont('Arial Black',20)
            TextSurf, TextRect = text_objects(a[a.index('-')+1:].strip(), largeText)
            TextRect.center = (203,150)
            screen.blit(top, [0, 0])
            screen.blit(TextSurf, TextRect)
            largeText = pygame.font.SysFont('Verdana',17)
            TextSurf, TextRect = text_objects(a[0:a.index('-')].strip(), largeText)
            TextRect.center = (200,110)
            screen.blit(TextSurf, TextRect)
            pygame.display.update()

#Ovim komentarom stavlja se veto na bilo kakvo kopiranje ili modificiranje
#ovog koda te datoteka krucijalnih za normalan rad programa koji pripada Luki Nestiću.

#Originalnost koda: 69%
#Originalnost ideje: 99%
#Originalnost estetike: 420%

#proljeće na ljeto 2018.
