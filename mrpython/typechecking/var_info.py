#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:14:36 2019

@author: 3522144
"""

class Var_info():
    
    def __init__(self, var_name, var_type, flagged_type):
        self.var_name = var_name
        self.var_type = var_type
        self.flagged_type = flagged_type
    
    def flagged_type(self):
        return self.flagged_type