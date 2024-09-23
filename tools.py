import pandas as pd

def import_thetas():
    # Theta import
    theta = pd.read_csv('theta.csv')
    theta_f = pd.DataFrame(theta)
    theta_0 = theta_f["theta0"].values[-1]
    theta_1 = theta_f["theta1"].values[-1]
    return theta_0, theta_1

def import_data():
    # Data import
    data = pd.read_csv('data.csv')
    df = pd.DataFrame(data)

    kms = df["km"]
    prices = df["price"]

    return df, kms, prices

def estimate_price(km, t0, t1):
    return t1 * km + t0

def get_normalized_list(values, min, max):
    return [get_normalized_value(x, min, max) for x in values]

def get_denormalized_list(values, min, max):
    return [get_denormalized_value(x, min, max) for x in values]

def get_normalized_value(value, min, max):
    return (value - min) / (max - min)

def get_denormalized_value(value, min, max):
    return value * (max - min) + min

def save_thetas(theta_0, theta_1):
    f = open("theta.csv", "a+")
    f.write("%f, %f\n" % (theta_0, theta_1))
    f.close()

