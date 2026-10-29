import math
import numpy as np
PI = 3.14159

def power_grid_forecast(consumption_data):
	# 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
	daily_fluctuation = [energy - (10 * math.sin(2 * PI * (i+1) / 10)) for i, energy in enumerate(consumption_data)]
	
	# 2) Perform linear regression on the detrended data.
	X = np.column_stack([np.ones(len(daily_fluctuation)), 
                     np.arange(1, len(daily_fluctuation) + 1)])
	y = np.array(daily_fluctuation)

	XtX_inv = np.linalg.inv(X.transpose() @ X)
	theta = XtX_inv @ X.transpose() @ y

	# 3) Predict day 15's base consumption.
	
	y_15 = theta[0] + 15 * theta[1]

	# 4) Add the day 15 fluctuation back.

	y_15_fluctuation = y_15 + (10 * math.sin(2 * PI * 15 / 10))

	# 5) Round, then add a 5% safety margin (rounded up).
	rounded = round(y_15_fluctuation) * 1.05

	# 6) Return the final integer.
	return math.ceil(rounded)