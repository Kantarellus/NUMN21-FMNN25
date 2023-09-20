


# Super class for optimization method
class OptimizationMethod:
	def __init__(self, opt_problem):
		self.opt_problem = opt_problem
		
	def solve(self):
		raise NotImplementedError("The solve method should be implemented by derived classes")
	
	
#------------- Derived Quasi Newton Methods -----------------------
	
class ClassicalNewtonMethod(OptimizationMethod):
	def __init__(self, opt_problem, h=1e-5, tolerance=1e-5,max_iterations=1000):
		# initialise method
		super().__init__(opt_problem)
		
		# initialise paramaters
		self.h = h
		self.tolerance = tolerance
		self.max_iterations=max_iterations

		if self.h <= 0:
			raise ValueError("Invalid parameter. h should be bigger than 0")
		if self.tolerance <= 0:
			raise ValueError("Invalid parameter. tolerance should be bigger than 0")
		if self.max_iterations <= 0:
			raise ValueError("Invalid parameter. max_iterations should be bigger than 0")

	def solve(self):

		import numpy as np
		import helper_methods 

		number_input_parameters=len(self.inspect.signature(self.objective_func))
		
		point=np.zeros(number_input_parameters)		#starting at 0
		
		

		for i in range(0,self.max_iterations-1):
			invhessian=helper_methods.inv_numerical_hessian(self,point)
			gradient=helper_methods.numerical_gradient(self,point)
			point[i+1]=point[i]-invhessian.dot(gradient)



		print(f"Solving using Quasi-Newton Method X with params {self.param1}, {self.param2}")
		# lots of math...