import math

kelvin = 273.15
adc_max = 4096


def temp(sens, adc_value):
    if sens == 'CTZ-01':                # Udetemperaturføler
        a, b, c = __steinhart(-40, 345275, 30, 8050, 120, 388)
        r1 = 5600

        t = __calc(a, b, c, r1, adc_value + 1)

        return t

    if sens == 'CT2a':                  # Røggas / Kedel føler
        a, b, c = __steinhart(-40, 345275, 40, 5314, 150, 177)
        r1 = 5600

        t = __calc(a, b, c, r1, adc_value + 1)

        return t

    if sens == 'CTP-02':                # Rumtemperatur sensor
        a, b, c = __steinhart(0, 32560, 50, 3600, 100, 680)
        r1 = 5600  # mangler verifikation

        t = __calc(a, b, c, r1, adc_value + 1)

        return t


def __calc(a, b, c, res, adc_reading):

    resistance = res / ((adc_max / adc_reading) - 1)
    t = math.log(resistance)
    t = 1 / (a + (b * t) + (c * t * t * t))
    t = t - kelvin

    return t


def __steinhart(t1, r1, t2, r2, t3, r3):
    # Convert celcius to kelvin
    k1 = t1 + kelvin
    k2 = t2 + kelvin
    k3 = t3 + kelvin

    l1 = math.log(r1)
    l2 = math.log(r2)
    l3 = math.log(r3)

    y1 = 1 / k1
    y2 = 1 / k2
    y3 = 1 / k3

    u2 = (y2 - y1) / (l2 - l1)
    u3 = (y3 - y1) / (l3 - l1)
    # Calculate steinhart A, B & C coefficients
    c = (u3 - u2) / (l3 - l2) * math.pow(l1 + l2 + l3, -1)
    b = u2 - c * (l1 * l1 + l1 * l2 + l2 * l2)
    a = y1 - (b + l1 * l1 * c) * l1

    return a, b, c
