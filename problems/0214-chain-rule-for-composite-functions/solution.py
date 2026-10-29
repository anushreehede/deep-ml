import numpy as np
import math

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(xÂ²)
		['exp', 'sin', 'square'] represents exp(sin(xÂ²))
	"""
	last_func = functions[-1]
	if last_func == 'sin':
		derivative = math.cos(x)
		func = math.sin(x)
	elif last_func == 'square':
		derivative = 2 * x
		func = math.pow(x, 2)
	elif last_func == 'exp':
		derivative = math.exp(x)
		func = math.exp(x)
	elif last_func == 'log':
		derivative = 1/x
		func = math.log(x)
	
	for i in range(len(functions)-2, -1, -1):
		if functions[i] == 'sin':
			derivative *= math.cos(func)
			func = math.sin(func)
		elif functions[i] == 'square':
			derivative *= (2 * func)
			func = math.pow(func, 2)
		elif functions[i] == 'exp':
			derivative *= math.exp(func)
			func = math.exp(func)
		elif functions[i] == 'log':
			derivative *= (1 / func)
			func = math.log(func)
	
	return derivative
		