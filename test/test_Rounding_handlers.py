from src.precise_value import (Rounding_handler,
    Rounding_handler_keep_integral_zeroes, Rounding_handler_proper)
import unittest

class test_Rounding_handler(unittest.TestCase):
    def setUp(self):
        self.rounder = Rounding_handler

    def test_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            Rounding_handler()

    def test_add

# class test_Rounding_handler_keep_integral_zeroes(unittest.TestCase):
