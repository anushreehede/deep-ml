import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	x = np.array(gradient)
	magnitude = np.linalg.norm(x)

	if not np.any(x):
		direction = np.zeros_like(x)
		descent_direction = np.zeros_like(x)
	else:
		direction = 1 / magnitude * x
		descent_direction = - direction

	return {
		'magnitude': magnitude.item(),
		'direction': direction.tolist(),
		'descent_direction': descent_direction.tolist()
	}