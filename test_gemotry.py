# test_geometry.py

import unittest
from geometry import volume_sphere, volume_cylinder, volume_cone, volume_cube

class TestGeometry(unittest.TestCase):

    def test_volume_sphere(self):
        self.assertAlmostEqual(volume_sphere(3), 113.097335, places=5)  # volume d'une sphère avec un rayon de 3
        self.assertRaises(ValueError, volume_sphere, -1)  # cas où le rayon est négatif

    def test_volume_cylinder(self):
        self.assertAlmostEqual(volume_cylinder(3, 5), 141.371669, places=5)  # volume d'un cylindre avec rayon 3 et hauteur 5
        self.assertRaises(ValueError, volume_cylinder, -1, 5)  # cas où le rayon est négatif
        self.assertRaises(ValueError, volume_cylinder, 3, -5)  # cas où la hauteur est négative

    def test_volume_cone(self):
        self.assertAlmostEqual(volume_cone(3, 5), 47.123889, places=5)  # volume d'un cône avec rayon 3 et hauteur 5
        self.assertRaises(ValueError, volume_cone, -1, 5)  # cas où le rayon est négatif
        self.assertRaises(ValueError, volume_cone, 3, -5)  # cas où la hauteur est négative

    def test_volume_cube(self):
        self.assertEqual(volume_cube(3), 27)  # volume d'un cube avec côté 3
        self.assertRaises(ValueError, volume_cube, -1)  # cas où le côté est négatif

if __name__ == "__main__":
    unittest.main()
