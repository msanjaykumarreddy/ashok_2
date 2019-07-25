import unittest
import pytest
from mathoperations.standard import Standardmathemeticaloperations
from mathoperations.advanced import Advancedmathemeticaloperations
from Area_calculations.Area import Differentareacalaculations


class testcalculation(unittest.TestCase):

    def test_addition(self):
        """
        testing addition
        :return:
        """
        self.assertEqual(Standardmathemeticaloperations(5, 10).addition(), 15)
        self.assertEqual(Standardmathemeticaloperations(5, -1).addition(), 4)
        self.assertEqual(Standardmathemeticaloperations(-5, -1).addition(), -6)

    def test_multiplication(self):
        """
        testing multiplication
        :return:
        """
        self.assertEqual(Standardmathemeticaloperations(5, 10).multiplication(), 50)
        self.assertEqual(Standardmathemeticaloperations(5, -1).multiplication(), -5)
        self.assertEqual(Standardmathemeticaloperations(-5, -1).multiplication(), 5)

    def test_substraction(self):
        """
        testing substraction
        :return:
        """
        self.assertEqual(Standardmathemeticaloperations(10, 5).substraction(), 5)
        self.assertEqual(Standardmathemeticaloperations(5, -1).substraction(), 6)
        self.assertEqual(Standardmathemeticaloperations(-5, -1).substraction(), -4)

    def test_division(self):
        """
        testing division
        :return:
        """
        self.assertEqual(Standardmathemeticaloperations(10, 5).division(), 2)
        self.assertEqual(Standardmathemeticaloperations(5, -1).division(), -5)
        self.assertEqual(Standardmathemeticaloperations(-5, -1).division(), 5)

    def test_square(self):
        """
        testing square
        :return:
        """
        self.assertEqual(Advancedmathemeticaloperations(10, 10).square(), 100)
        self.assertEqual(Advancedmathemeticaloperations(4, 10).square(), 40)
        self.assertEqual(Advancedmathemeticaloperations(2, 2).square(), 4)

    def test_cube(self):
        """
        testing cube
        :return:
        """
        self.assertEqual(Advancedmathemeticaloperations(10, 10).cube(), 1000)
        self.assertEqual(Advancedmathemeticaloperations(4, 10).cube(), 160)
        self.assertEqual(Advancedmathemeticaloperations(2, 2).cube(), 8)

    def test_squareeoot(self):
        """
        testing square root
        :return:
        """
        self.assertEqual(Advancedmathemeticaloperations(25, 100).squareroot(), 5)
        self.assertEqual(Advancedmathemeticaloperations(144, 100).squareroot(), 12)
        self.assertEqual(Advancedmathemeticaloperations(81, 100).squareroot(), 9)

    def test_cuberoot(self):
        """
        testing cuberoot
        :return:
        """
        self.assertEqual(Advancedmathemeticaloperations(125, 100).cuberoot(), 5)
        self.assertEqual(Advancedmathemeticaloperations(27, 100).cuberoot(), 3)
        self.assertEqual(Advancedmathemeticaloperations(8, 100).cuberoot(), 2)

    def test_square_area(self):
        """
        testing square area
        :return:
        """
        self.assertEqual(Differentareacalaculations(5, 10, 15).square_area(), 50)
        self.assertEqual(Differentareacalaculations(12, 12, 250).square_area(), 144)
        self.assertEqual(Differentareacalaculations(15, 10, 100).square_area(), 150)

    def test_triangle_area(self):
        """
        testing triangle area
        :return:
        """
        self.assertEqual(Differentareacalaculations(5, 10, 15).triangle_area(), 106.06601717798213)
        self.assertEqual(Differentareacalaculations(12, 12, 250).triangle_area(), 23133.444404152186)
        self.assertEqual(Differentareacalaculations(15, 10, 100).triangle_area(), 3947.9029243384393)

    def test_rectangle_area(self):
        """
        testing rectangle triangle
        :return:
        """
        self.assertEqual(Differentareacalaculations(5, 6, 15).rectangle_area(), 30)
        self.assertEqual(Differentareacalaculations(12, 7, 250).rectangle_area(), 84)
        self.assertEqual(Differentareacalaculations(15, 15, 100).rectangle_area(), 225)

    def test_hexagon_area(self):
        """
        testing hexagon area
        :return:
        """
        self.assertEqual(Differentareacalaculations(5, 6, 15).hexagon_area(), 1.462008869106433)
        self.assertEqual(Differentareacalaculations(12, 7, 250).hexagon_area(), 2.6207413942088964)
        self.assertEqual(Differentareacalaculations(15, 15, 100).hexagon_area(), 3.0411009977866996)
