#!/usr/bin/python3

from visual import display, save_fig
from tools import import_data, import_thetas, estimate_price, get_normalized_list, save_thetas
import imageio

# Data import
df, kms, prices = import_data()

km_min = kms.min()
km_max = kms.max()
km_mean = kms.mean()

price_min = prices.min()
price_max = prices.max()
price_mean = prices.mean()

df["normalized_price"] = get_normalized_list(prices.tolist(), price_min, price_max)
n_prices = df["normalized_price"]

df["normalized_km"] = get_normalized_list(kms.tolist(), km_min, km_max)
n_kms = df["normalized_km"]

sample_size = kms.count()

theta_0, theta_1 = import_thetas()

def denormalize_thetas(t0, t1):

    x_range = km_max - km_min
    y_range = price_max - price_min

    x_mean = km_mean
    y_mean = price_mean

    range_ratio = y_range / x_range

    # Geometrical approach
    dtheta_1 = t1 * range_ratio
    dtheta_0 = t0 * range_ratio + y_mean - dtheta_1 * x_mean

    return dtheta_0, dtheta_1

frames = []

def gif_step(i):
    image = imageio.v2.imread(f'./img/img_{i}.png')
    frames.append(image)
    if i == -1:
        imageio.mimsave('./example.gif', frames, duration = 50)

def gradient_descent(theta0, theta1, xs, ys):
    learning_rate = 1
    for i in range(0, 100):
        dt0 = 0
        dt1 = 0

        for x, y in zip(xs, ys):
            price_diff = estimate_price(x, theta0, theta1) - y
            dt0 += price_diff
            dt1 += price_diff * x

        theta0 -= learning_rate * dt0 / sample_size
        theta1 -= learning_rate * dt1 / sample_size

        dtheta0, dtheta1 = denormalize_thetas(theta0, theta1)
        save_thetas(dtheta0, dtheta1)

        save_fig(dtheta0, dtheta1, df, i)
        gif_step(i)

    return theta0, theta1

theta_0, theta_1 = gradient_descent(theta_0, theta_1, n_kms, n_prices)
nt0, nt1 = denormalize_thetas(theta_0, theta_1)

display(nt0, nt1, kms, prices, km_min, km_max)
gif_step(-1)
