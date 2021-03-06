# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 21:54:13 2016

@author: julien
"""
import random
from planets import Planet
import functions as fn

class World_Mining(Planet):
    img_ref = 'Venus'
    cat = 'Mining World'
    weight = 8
    def __init__(self, game, pos):
        super(type(self), self).__init__(game,pos, type(self).img_ref)
        self.radius = random.randint(250,400) #SOF
        self.name = '{}-{}'.format(fn.name_gen(True),str(random.randint(0,100)))
        self.chance_of_discovery = random.randint(0,10)
        self.disc_kp = random.randint(0,3)
        self.disc_rp = random.randint(10,15)
        
class World_Habitable(Planet):
    img_ref = 'Earth'
    cat = 'Habitable World'
    weight = 3
    def __init__(self, game, pos):
        super(type(self), self).__init__(game,pos, type(self).img_ref)
        self.radius = random.randint(250,500) #SOF
        self.name = '{}-{}'.format(fn.name_gen(True),str(random.randint(0,100)))
        self.chance_of_discovery = random.randint(0,15)
        self.disc_kp = random.randint(5,10)
        self.disc_rp = random.randint(10,10)
        
class World_Frozen(Planet):
    img_ref = 'Frozen'
    cat = 'Frozen World'
    weight = 10
    def __init__(self, game, pos):
        super(type(self), self).__init__(game,pos, type(self).img_ref)
        self.radius = random.randint(400,700) #SOF
        self.name = '{}-{}'.format(fn.name_gen(True),str(random.randint(0,100)))
        self.chance_of_discovery = random.randint(0,15)
        self.disc_kp = random.randint(0,2)
        self.disc_rp = random.randint(0,2)
        
class World_Alien(Planet):
    img_ref = 'Alien_hive'
    cat = 'Alien World'
    weight = 1
    def __init__(self, game, pos):
        super(type(self), self).__init__(game,pos, type(self).img_ref)
        self.radius = random.randint(250,600) #SOF
        self.name = '{}-{}'.format(fn.name_gen(True),str(random.randint(0,100)))
        self.chance_of_discovery = random.randint(0,15)
        self.disc_kp = random.randint(20,30)
        self.disc_rp = random.randint(5,10)

        
        

