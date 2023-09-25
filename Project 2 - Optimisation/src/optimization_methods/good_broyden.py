# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 18:58:34 2023

@author: laptop
"""
from numpy import *
from matplotlib.pyplot import *
from .newton_inexact_line_search import NewtonInexactLineSearch 


class GoodBroyden(NewtonInexactLineSearch):
    
    def __init__(self, opt_problem, n, h=1e-5, tolerance=1e-5, max_iterations=1000, initial_guess = None):
    
        super().__init__(self, opt_problem, n, h, tolerance, max_iterations, initial_guess)
                    # Start with zeros if no initial guess is specified
        x = self.initial_guess if self.initial_guess is not None else zeros(self.n)
        
        self.Q = approximate_hessian(self.opt_problem.objective_func, \ 
                                     self.opt_problem.gradient_func, x = None)  
        self.H = inv_numerical_hessian(self.opt_problem.objective_func, \
                                       self.opt_problem.gradient_func, x = None)
    
    def compute_direction(self, x, evaluate_func, gradient_func, current_gradient):
        
        s = -self.H @ current_gradient
        
        return s
        
    def update_hessian_invHessian(self):
        
        x_new = self.path[-1]
        x_old = self.path[-2]
        
        grad_new = self.opt_problem.gradient(x_new)
        grad_old = self.opt_problem.gradient(x_old)
        
        H = self.H    
        Q = self.Q
        
        delta = x_new - x_old 
        gamma = grad_new - grad_old
        
        v = (gamma - Q @ delta)*(1/(delta.T @ delta))
        
        # Updating H
        
        self.H = H + (1/(delta.T @ H @ gamma))*(delta - H @ gamma) @ (delta.T @ H) 
        
        # Update Q
        
        self.Q = Q + v @ delta.T
        
    