#!/usr/bin/venv python

import pygame
import os

class Attack:
    def __init__(self, asset_name, damage, height, width, x, y):
        self.asset_name = asset_name
        self.damage = damage
        self.height = height
        self.width = width
        self.x_pos = x
        self.y_pos = y