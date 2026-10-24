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
            if len(parameters) == 3:
                value = trimf(input_val, *parameters)
            else:
                value = trapmf(input_val, *parameters)
            sonuc[name] = value
        return sonuc

# Fuzzification demo: membership degrees of a sample applicant's inputs
print("Market value 300k $ :", fuzzification(300, market_value))
print("Location 7          :", fuzzification(7, house_location))
print("Asset 400k $        :", fuzzification(400, applicant_asset))
print("Income 50k $        :", fuzzification(50, applicant_salary))
print("Interest 5 %        :", fuzzification(5, interest_rate))
print()


# Rule format: ({variable: fuzzy_set, ...}, output_set)

# 1. House Evaluation (14 rules)
house_rules = [
    ({"Market": "Low"}, "Low"),                                     # 1
    ({"Location": "Bad"}, "Low"),                                   # 2
    ({"Location": "Bad", "Market": "Low"}, "Very Low"),             # 3
    ({"Location": "Bad", "Market": "Medium"}, "Low"),               # 4
    ({"Location": "Bad", "Market": "High"}, "Medium"),              # 5
    ({"Location": "Bad", "Market": "Very High"}, "High"),           # 6
    ({"Location": "Fair", "Market": "Low"}, "Low"),                 # 7
    ({"Location": "Fair", "Market": "Medium"}, "Medium"),           # 8
    ({"Location": "Fair", "Market": "High"}, "High"),               # 9
    ({"Location": "Fair", "Market": "Very High"}, "Very High"),     # 10
    ({"Location": "Excellent", "Market": "Low"}, "Medium"),         # 11
    ({"Location": "Excellent", "Market": "Medium"}, "High"),        # 12
    ({"Location": "Excellent", "Market": "High"}, "Very High"),     # 13
    ({"Location": "Excellent", "Market": "Very High"}, "Very High"),# 14
]

# 2. Applicant Evaluation (12 rules)
applicant_rules = [
    ({"Asset": "Low", "Income": "Low"}, "Low"),                     # 1
    ({"Asset": "Low", "Income": "Medium"}, "Low"),                  # 2
    ({"Asset": "Low", "Income": "High"}, "Medium"),                 # 3
    ({"Asset": "Low", "Income": "Very High"}, "High"),              # 4
    ({"Asset": "Medium", "Income": "Low"}, "Low"),                  # 5
    ({"Asset": "Medium", "Income": "Medium"}, "Medium"),            # 6
    ({"Asset": "Medium", "Income": "High"}, "High"),                # 7
    ({"Asset": "Medium", "Income": "Very High"}, "High"),           # 8
    ({"Asset": "High", "Income": "Low"}, "Medium"),                 # 9
    ({"Asset": "High", "Income": "Medium"}, "Medium"),              # 10
    ({"Asset": "High", "Income": "High"}, "High"),                  # 11
    ({"Asset": "High", "Income": "Very High"}, "High"),             # 12
]

# 3. Loan Amount Evaluation (15 rules)
credit_rules = [
    ({"Income": "Low", "Interest": "Medium"}, "Very Low"),          # 1
    ({"Income": "Low", "Interest": "High"}, "Very Low"),            # 2
    ({"Income": "Medium", "Interest": "High"}, "Low"),              # 3 
    ({"Applicant": "Low"}, "Very Low"),                             # 4
    ({"House": "Very Low"}, "Very Low"),                            # 5
    ({"Applicant": "Medium", "House": "Very Low"}, "Low"),          # 6
    ({"Applicant": "Medium", "House": "Low"}, "Low"),               # 7
    ({"Applicant": "Medium", "House": "Medium"}, "Medium"),         # 8
    ({"Applicant": "Medium", "House": "High"}, "High"),             # 9
    ({"Applicant": "Medium", "House": "Very High"}, "High"),        # 10
    ({"Applicant": "High", "House": "Very Low"}, "Low"),            # 11
    ({"Applicant": "High", "House": "Low"}, "Medium"),              # 12
    ({"Applicant": "High", "House": "Medium"}, "High"),             # 13
    ({"Applicant": "High", "House": "High"}, "High"),               # 14
    ({"Applicant": "High", "House": "Very High"}, "Very High"),     # 15
]

# Evaluate a fuzzy set over the whole universe (returns an array)
def membership_over_universe(x_universe, parameters):
    if len(parameters) == 3:
        return np.array([trimf(x, *parameters) for x in x_universe])
    else:
        return np.array([trapmf(x, *parameters) for x in x_universe])
        

def mamdani(inputs, rules, output_sets, x_universe):
    aggregated = np.zeros(len(x_universe))

    # take each rule
    for conditions, output_name in rules:
        
        # Step 1: rule strength = min of all condition memberships (AND)
        strength = 1
        for variable, fuzzy_set in conditions.items():
            strength = min(strength, inputs[variable][fuzzy_set])

        # Skip rules that do not fire
        if strength == 0:
            continue

        # Step 2: clip the output set at the rule strength
        output_mf = membership_over_universe(x_universe, output_sets[output_name])
        clipped = np.minimum(strength, output_mf)

        # Step 3: aggregate with max
        aggregated = np.maximum(aggregated, clipped)

    # Step 4: centroid defuzzification
    if np.sum(aggregated) == 0:
        return 0  # no rule fired
    return np.sum(x_universe * aggregated) / np.sum(aggregated)

# Hierarchical evaluation: house -> applicant -> loan amount
def evaluate_loan(market, location, asset, income, interest):
    # Fuzzify crisp inputs
    market_f   = fuzzification(market, market_value)
    location_f = fuzzification(location, house_location)
    asset_f    = fuzzification(asset, applicant_asset)
    income_f   = fuzzification(income, applicant_salary)
    interest_f = fuzzification(interest, interest_rate)

    # Stage 1: house evaluation (0-10)
    house_inputs = {"Market": market_f, "Location": location_f}
    house_score = mamdani(house_inputs, house_rules, house_evaluation, x_house_eval)

    # Stage 2: applicant evaluation (0-10)
    applicant_inputs = {"Asset": asset_f, "Income": income_f}
    applicant_score = mamdani(applicant_inputs, applicant_rules, applicant_evaluation, x_applicant_eval)

    # Stage 3: loan amount
    # Re-fuzzify stage 1 and 2 outputs using their output sets
    credit_inputs = {
        "Income":    income_f,
        "Interest":  interest_f,
        "House":     fuzzification(house_score, house_evaluation),
        "Applicant": fuzzification(applicant_score, applicant_evaluation),
    }
    credit_amount = mamdani(credit_inputs, credit_rules, credit, x_credit)

    return house_score, applicant_score, credit_amount

# test scenerios
# scenarios = [
#     ("Ideal applicant",               800, 9, 800, 90, 3),
#     ("Average applicant",             300, 7, 400, 50, 5),
#     ("Low income, high interest",     400, 6, 200, 15, 9),
#     ("Wealthy applicant, poor house", 100, 2, 900, 85, 4),
#     ("Great house, weak applicant",   900, 9,  50, 20, 5),
# ]

# print("=" * 75)
# print(f"{'Scenario':32} | {'House':>6} | {'Applicant':>9} | {'Loan':>12}")
# print("=" * 75)

# for name, market, location, asset, income, interest in scenarios:
#     house, applicant, loan = evaluate_loan(market=market, location=location, asset=asset,
#                                            income=income, interest=interest)
#     print(f"{name:32} | {house:6.2f} | {applicant:9.2f} | {loan:8.1f}k $")

# print("=" * 75)