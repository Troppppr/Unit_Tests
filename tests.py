
import math
import unittest
import functions

class MyTestCase(unittest.TestCase):
    def test_arctg_x(self):
        self.assertEqual(functions.arctg(1), math.pi/4)
        self.assertEqual(functions.arctg(0), 0)
        self.assertEqual(functions.arctg(-1), -math.pi/4)
        self.assertEqual(functions.arctg(float('inf')), math.pi/2)
        self.assertEqual(functions.arctg(float('-inf')), -math.pi/2)
        self.assertEqual(functions.arctg(2), 1.1071487177940904)
        self.assertEqual(functions.arctg(-2), -1.1071487177940904)
        self.assertEqual(functions.arctg(3), 1.2490457723982544)
        self.assertEqual(functions.arctg(-3), -1.2490457723982544)
        self.assertEqual(functions.arctg(4), 1.3258176636680326)

    def test_x_cubed(self):
        self.assertEqual(functions.x_cubed(1), 1)
        self.assertEqual(functions.x_cubed(0), 0)
        self.assertEqual(functions.x_cubed(-1), -1)
        self.assertEqual(functions.x_cubed(2), 8)
        self.assertEqual(functions.x_cubed(-2), -8)
        self.assertEqual(functions.x_cubed(3), 27)
        self.assertEqual(functions.x_cubed(-3), -27)
        self.assertEqual(functions.x_cubed(4), 64)
        self.assertEqual(functions.x_cubed(-4), -64)
        self.assertEqual(functions.x_cubed(5), 125)

    def test_y(self):
        self.assertEqual(functions.y(1), math.pi / 4 + 1)
        self.assertEqual(functions.y(2), 9.10714871779409)
        self.assertEqual(functions.y(3), 28.249045772398254)
        self.assertEqual(functions.y(-1), -1.7853981633974483)
        self.assertEqual(functions.y(-2), -9.10714871779409)

if __name__ == '__main__':
    unittest.main()