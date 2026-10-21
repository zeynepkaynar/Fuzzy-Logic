import numpy as np
# Membership functions

# Triangular membership function
def trimf(x, a, b, c):
    # Vertex
    if x == b:
        return 1
    if (x <= a or x >= c):
        return 0
    if (a <= x <= b):
        return (x-a)/(b-a)
    if (b <= x <= c):
        return (c-x)/(c-b)

# Trapezoidal membership function
def trapmf(x, a, b, c, d):
    if (b <= x <= c):
        return 1
    if (x <= a or x >= d):
        return 0
    if (a <= x <= b):
        return trimf(x, a, b, c)
    if (c <= x <= d):
        return trimf(x, a, c, d)

# Inputs
market_value = {"Low": (0, 0, 75, 100) ,"Medium": (50, 100, 200, 250), "High": (200, 300, 650, 850), "Very High": (650, 850, 1000, 1000)}
house_location = {"Bad": (0, 0, 1.5, 4) ,"Fair": (2.5, 5, 6, 8.5), "Excellent": (6, 8.5, 10, 10)}
applicant_asset = {"Low": (0, 0, 150) ,"Medium": (50, 250, 450, 650), "High": (500, 700, 1000, 1000)}
applicant_salary = {"Low": (0, 0, 10, 25) ,"Medium": (15, 35, 55), "High": (40, 60, 80), "Very High": (60, 80, 100, 100)}
interest_rate = {"Low": (0, 0, 2, 5) ,"Medium": (2, 4, 6, 8), "High": (6, 8.5, 10, 10)}

# Outputs
house_evaluation = {"Very Low": (0, 0, 3), "Low": (0, 3, 6) ,"Medium": (2, 5, 8), "High": (4, 7, 10), "Very High": (7, 10, 10)}
applicant_evaluation = {"Low": (0, 0, 2, 4) ,"Medium": (2, 5, 8), "High": (6, 8, 10, 10)}
credit = {"Very Low": (0, 0, 125), "Low": (0, 125, 250) ,"Medium": (125, 250, 375), "High": (250, 375, 500), "Very High": (375, 500, 500)}

x_house_eval = np.linspace(0, 10, 1001)
x_applicant_eval = np.linspace(0, 10, 1001)
x_credit = np.linspace(0, 500, 1001)

# Fuzzify
def fuzzification(input_val, var):
        sonuc = {}
        for name, parameters in var.items():
            print(name, parameters)
            if len(parameters) == 3:
                value = trimf(input_val, *parameters)
            else:
                value = trapmf(input_val, *parameters)
            sonuc[name] = value
        return sonuc