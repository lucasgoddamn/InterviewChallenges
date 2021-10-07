def rotation (hours, minutes):
    dh = 30 * (hours % 12) + (30/12) * m
    dm = 30 * (minutes / 5)
    return abs(dh - dm)


print(rotation(11, 45))