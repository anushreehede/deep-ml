import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X = np.asarray(X)
	y = np.asarray(y)

	XtX_inv = np.linalg.inv(X.transpose() @ X)
	theta = XtX_inv @ X.transpose() @ y

	return theta.round(4).tolist()