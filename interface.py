# -*- coding: utf-8 -*-
"""
Created on Sat Aug 06 10:06:08 2016

@author: julien
"""
import pygame
import functions as fn

class Interface(object):
    def __init__(self,game):
        self.game = game
        self.screen = 'pygame screen'
        
    def centered_offset(self,offset):
        x,y = offset[0],offset[1]
        return (self.screen.centerx-x,self.screen.centery-y)
        
    def view_solarsys(self,offset):
        for p in self.game.all_planets:
            self.screen.fn.blitc(p.image,fn.sum_tulp(p.pos,self.centered_offset(offset)))
            
    def view_planet(self,planet):
        '''make buttons'''
        go_to_button = Button('Travel to',planet,600,600)
        view_solarsys_but = Button('View in Solar System',planet,600,500)
        
        buttons = []
        buttons.extend([go_to_button,view_solarsys_but])
        
        ''' blit all the planet's stats to the screen'''
        self.screen.blit(planet.stats,(0,0))
        
        (but.display(self.screen) for but in buttons)
        
        if go_to_button.selected == True:
            if self.game.player.logbook[planet.name].is_discovered == False:
                planet.explore(self.game.player)
            else:
                planet.visit(self.game.player)
                
        elif view_solarsys_but.selected == True:
            self.view_solarsys(planet.pos)
        
               
class Button(pygame.sprite.Sprite):
    def __init__(self, text, binded, x,y):
        super(Button, self).__init__()
        self.text = text
        self.image = var.but_bg
#        self.text_pos = ((x+w/2),(y+h/2))
#        self.rect2 = 0
        self.txt_color = (0,0,0)
        self.binded = binded
        
       
        self.smallText = pygame.font.Font("freesansbold.ttf",12)
        self.textSurf = self.smallText.render(self.text, True, self.txt_color)
#        self.rect2 = self.textSurf.get_rect()
#        self.rect2.center = self.text_pos
        self.image = pygame.transform.scale(self.image, (int(self.rect2.width*1.5),int(self.rect2.height*3)))
        self.rect = pygame.Rect(x,y,self.image.get_rect().width,self.image.get_rect().height)
        
        self.selected = False
        self.m_released = True
        
    def check_select(self):
        m_pos = pygame.mouse.get_pos()
        over_but = self.rect.collidepoint(m_pos) 
        
        if pygame.mouse.get_pressed()[0] ==1 and over_but == 1 and self.selected == False and self.m_released == True:
            self.selected = True
            self.txt_color = (0,200,0)
            self.m_released = False
            
        elif pygame.mouse.get_pressed()[0] == 1 and over_but == 1 and self.selected == True and self.m_released == True:
            self.selected = False
            self.txt_color = (0,0,0)
            self.m_released = False
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.m_released = True
            
            
            
    def display(self,dest_surf):
        #self.surface = pygame.draw.rect(var.screen, self.color , self.rect)
        dest_surf.blit(self.image,self.rect)
        dest_surf.blit(self.textSurf, pygame.Rect(self.rect[0]+(self.rect.centerx-self.rect[0])*0.4,self.rect[1]+self.rect[3]/4,self.rect[2],self.rect[3])) #Rect(self.rect[0]+self.rect[2]/8,self.rect[1]+20,self.rect[2],self.rect[3])

                