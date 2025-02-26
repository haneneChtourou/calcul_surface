# geometry.py

import math

def volume_sphere(radius):
    """Calcule le volume d'une sphère"""
    if radius < 0:
        raise ValueError("Le rayon ne peut pas inégatif.")
    return (4/3) * math.pi* (radius ** 3)

def volume_cylinder(radius, height):
    """Calcule le volume d'un cylindre"""
    if radius < 0 or height < 0:
        raise ValueError("Le rayon et la hauteur doivent être positifs.")
    return math.pi * (radius ** 2) * height

def volume_cone(radius, height):
    """Calcule le volume d'un cône"""
    if radius < 0 or height < 0:
        raise ValueError("Le rayon et la hauteur doivent être positifs.")
    return (1/3) * math.pi * (radius ** 2) * height

def volume_cube(side):
    """Calcule le volume d'un cube"""
    if side < 0:
        raise ValueError("Le côté ne peut pas être négatif.")
    return side ** 3

