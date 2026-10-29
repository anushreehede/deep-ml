import numpy as np
import math
def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
	"""
	Compute partial derivatives of multivariable functions.
	
	Args:
		func_name: Function identifier
			'poly2d': f(x,y) = x²y + xy²
			'exp_sum': f(x,y) = e^(x+y)
			'product_sin': f(x,y) = x·sin(y)
			'poly3d': f(x,y,z) = x²y + yz²
			'squared_error': f(x,y) = (x-y)²
		point: Point (x, y) or (x, y, z) at which to evaluate
	
	Returns:
		Tuple of partial derivatives (∂f/∂x, ∂f/∂y, ...) at point
	"""
	# Your code here
	if func_name == 'poly2d':
		d_dx = (2 * point[0] * point[1]) + (point[1] * point[1])
		d_dy = (point[0] * point[0]) + (2 * point[0] * point[1])
		return (d_dx, d_dy)
	elif func_name == 'exp_sum':
		d_dx = math.exp(point[0] + point[1])
		d_dy = math.exp(point[0] + point[1])
		return (d_dx, d_dy)
	elif func_name == 'product_sin':
		d_dx = math.sin(point[1])
		d_dy = point[0] * math.cos(point[1])
		return (d_dx, d_dy)
	elif func_name == 'poly3d':
		d_dx = 2 * point[0] * point[1]
		d_dy = (point[0] * point[0]) + (point[2] * point[2])
		d_dz = 2 * point[1] * point[2]
		return (d_dx, d_dy, d_dz)
	elif func_name == 'squared_error':
		d_dx = 2 * (point[0] - point[1])
		d_dy = -2 * (point[0] - point[1])
		return (d_dx, d_dy)