# -*- coding: utf-8 -*-
"""
Created on Sat Aug 06 11:50:54 2016

@author: julien
"""
'''import built in modules'''
import pygame
from pygame.locals import*
import random
import sys

'''Game Init'''
pygame.init()
clock = pygame.time.Clock() #set timer which is used to slow game down

'''import game modules'''
import interface
import planets
import explorers
import config
import functions as fn
import time

class Game(object):
    def __init__(self):
        self.interface = interface.Interface(self)
        self.clock = pygame.time.Clock() #set timer which is used to slow game down
        self.months = 0

        '''Create Planets'''
        self.all_planets = pygame.sprite.Group()
        self.generate_planets()
        [p.get_in_SOF() for p in self.all_planets]
        '''create explorers and player'''
        self.all_explorers = [explorers.Explorer(self) for x in range (2)]
        self.player = explorers.Explorer(self)
        
        '''assign starting planet to player only'''
        delay, x = 20, 0
        for p in self.all_planets:
            if x == delay:
                p.unveil(self.player,False)
                p.explore(self.player)
                break  
            x += 1
        
        '''setting up game switches'''
        self.map_mode = True
        self.planet_mode = False
        
    def generate_planets(self):
        offset = 50
        w = config.Config.screen_w-offset
        h = config.Config.screen_h-offset
        
        row_nb,col_nb = 5,10
        for row in range(offset/2, int(h + offset*1.5), h/row_nb):
            for col in range(offset/2, int(w + offset*1.5), w/col_nb):
                self.all_planets.add(planets.Planet(self,(col,row)))
                
    def monthly_planet_discovery_event(self):
        for log in self.player.logbook.values():
            if log.is_explored:
                print log.instance[0].planets_in_SOF
                for planet in log.instance[0].planets_in_SOF:
                    if log.instance[0].chance_of_discovery >= random.randint(0,100):
                        planet.unveil(self.player,False)
                    
                
       
    def run(self):
        '''set up'''
        black_bg = pygame.Surface((config.Config.screen_w,config.Config.screen_h))
        black_bg.fill((0,0,0))
        pygame.time.set_timer(USEREVENT + 1, 4000) # 1 event every 10 seconds
        
        while True:
            self.clock.tick(60) #needed to slow game down
            t0 = time.time()
            for event in pygame.event.get(): #setting up quit
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    print 'has quit'
                elif event.type == USEREVENT + 1:
                    self.months += 1 #adds a months of gametime every 10 seconds
                    self.monthly_planet_discovery_event()
                    print 'current month: ',self.months
                    
            
                    
            if self.map_mode == True:
                '''Calling Display functions'''
                self.interface.screen.blit(black_bg,(0,0))
                planet = [ v for v in self.player.logbook.values()][0].instance[0]
                self.interface.view_solarsys((config.Config.screen_w/2,config.Config.screen_h/2),planet)
                
            if self.planet_mode == True:
                self.interface.view_planet(self.interface.selected)
            
            pygame.display.update()
            t1 = time.time()
            #print t1-t0
        
        