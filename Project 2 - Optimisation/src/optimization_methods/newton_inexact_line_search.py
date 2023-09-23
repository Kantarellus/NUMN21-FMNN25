from .classical_newton_method import ClassicalNewtonMethod
import numpy as np

class NewtonInexactLineSearch(ClassicalNewtonMethod):
	def compute_alpha(self, x, direction, sigma=1e-4, max_backtracks=10):
		alpha = 1
		for _ in range(max_backtracks):
			# Compute Armijo condition
			f_new_x = self.opt_problem.evaluate(x + alpha * direction)
			f_x = self.opt_problem.evaluate(x)
			gradient_f_x = self.opt_problem.gradient(x)
			armijo_condition = f_x + sigma * alpha * np.dot(gradient_f_x, direction)
			
			# Check Armijo rule
			if f_new_x <= armijo_condition:
				return alpha
			alpha *= 0.5
		
		return alpha # Return the latest alpha, even though it didn't satisfy the condition
