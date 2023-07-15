import numpy as np


def identify_outliers(arr):
    arr = np.array(arr)
    mean = np.mean(arr)
    std_dev = np.std(arr)
    threshold = -0.5

    outliers = []
    for value in arr:
        z_score = (value - mean) / std_dev
        if z_score < threshold:
            outliers.append(value)

    return outliers


values = [
    36.527,
    87.065,
    118.969,
    91.317,
    179.423,
    120.971,
    46.140,
    24.216,
    131.703,
    155.251,
    157.171,
    94.395,
    110.127,
    53.026,
    60.065,
    107.268,
    107.331,
    161.152,
    255.967,
    247.487,
    49.618,
    59.500,
    130.331,
    121.057,
    80.661,
    96.950,
    102.791,
    49.534,
    30.764,
    178.425,
    143.575
]

print(identify_outliers(values))
