from math import pi, sqrt

def to_meters(value, unit):
    unit = unit.lower()
    if unit == "cm":
        return value / 100
    elif unit == "mm":
        return value / 1000
    else:
        return value  

def asquare(a, unit):
    a = to_meters(a, unit)
    return f"{a * a} m²"

def psquare(a, unit):
    a = to_meters(a, unit)
    return f"{4 * a} m"

def arectangle(a, b, unit):
    a = to_meters(a, unit)
    b = to_meters(b, unit)
    return f"{a * b} m²"

def prectangle(a, b, unit):
    a = to_meters(a, unit)
    b = to_meters(b, unit)
    return f"{2 * (a + b)} m"

def acircle(a, unit):
    a = to_meters(a, unit)
    return f"{pi * a * a} m²"

def pcircle(a, unit):
    a = to_meters(a, unit)
    return f"{2 * pi * a} m"

def ptriangle(a, b, c, unit):
    a = to_meters(a, unit)
    b = to_meters(b, unit)
    c = to_meters(c, unit)
    return f"{a + b + c} m"

def atriangle(a, b, unit):
    a = to_meters(a, unit)
    b = to_meters(b, unit)
    return f"{(a * b) / 2} m²"

def arhombus(a, b, unit):
    a = to_meters(a, unit)
    b = to_meters(b, unit)
    return f"{(a * b) / 2} m²"

def tsacube(a, unit):
    a = to_meters(a, unit)
    return f"{6 * a * a} m²"

def csacube(a, unit):
    a = to_meters(a, unit)
    return f"{4 * a * a} m²"

def vcube(a, unit):
    a = to_meters(a, unit)
    return f"{a ** 3} m³"

def tsacuboid(l, b, h, unit):
    l = to_meters(l, unit)
    b = to_meters(b, unit)
    h = to_meters(h, unit)
    return f"{2 * (l * h + b * h + l * b)} m²"

def csacuboid(l, b, h, unit):
    l = to_meters(l, unit)
    b = to_meters(b, unit)
    h = to_meters(h, unit)
    return f"{2 * h * (l + b)} m²"

def vcuboid(l, b, h, unit):
    l = to_meters(l, unit)
    b = to_meters(b, unit)
    h = to_meters(h, unit)
    return f"{l * b * h} m³"

def tsacylinder(r, h, unit):
    r = to_meters(r, unit)
    h = to_meters(h, unit)
    return f"{2 * pi * r * (r + h)} m²"

def csacylinder(r, h, unit):
    r = to_meters(r, unit)
    h = to_meters(h, unit)
    return f"{2 * pi * r * h} m²"

def vcylinder(r, h, unit):
    r = to_meters(r, unit)
    h = to_meters(h, unit)
    return f"{pi * r * r * h} m³"

def tsacone(r, l, unit):
    r = to_meters(r, unit)
    l = to_meters(l, unit)
    return f"{pi * r * (r + l)} m²"

def csacone(r, l, unit):
    r = to_meters(r, unit)
    l = to_meters(l, unit)
    return f"{pi * r * l} m²"

def tsasphere(r, unit):
    r = to_meters(r, unit)
    return f"{4 * pi * r * r} m²"

def vsphere(r, unit):
    r = to_meters(r, unit)
    return f"{(4 / 3) * pi * r ** 3} m³"

def tsahemisphere(r, unit):
    r = to_meters(r, unit)
    return f"{3 * pi * r * r} m²"

def csahemisphere(r, unit):
    r = to_meters(r, unit)
    return f"{2 * pi * r * r} m²"

def vhemisphere(r, unit):
    r = to_meters(r, unit)
    return f"{(2 / 3) * pi * r ** 3} m³"

def aeqitriangle(a, unit):
    a = to_meters(a, unit)
    return f"{(sqrt(3) / 4) * a * a} m²"

def strapezium(a, b, h, unit):
    a = to_meters(a, unit)
    b = to_meters(b, unit)
    h = to_meters(h, unit)
    return f"{0.5 * (a + b) * h} m²"
