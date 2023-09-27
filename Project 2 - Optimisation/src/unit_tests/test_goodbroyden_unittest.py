# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:00:16 2023

@author: laptop
"""
from numpy import *
from matplotlib.pyplot import *
from src.functions import numerical_gradient
from .optimization_method import OptimizationMethod
import unittest

class TestGoodBroyden(unittest.TestCase):
    
    
    def test_descentDir(self):
        
        x = array([0]*2)
        func = lambda x: (x[0]+4)**2 + x[1]**2
        opt_problem = OptimizationProblem(func)    
        
        
        #evaluate_func = opt_problem.evaluate(x)
        gradient_func = opt_problem.get_gradient()
        current_gradient = gradient_func(x)
        
        s = compute_direction(x, gradient_func, current_gradient)
        check_sign = current_gradient @ s
        
        self.assertTrue(check_sign < 0)
        
if __name__ == "__main__"
    unittest.main()
        
        
        