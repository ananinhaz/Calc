import unittest
from calculadora import calculate_hours

class TestCalculator(unittest.TestCase):

    def test_validar_temp(self):
        self.assertEqual(calculate_hours('09:00', '17:00'), 8)

    def test_validar_temp(self):
        with self.assertRaises(ValueError):
            calculate_hours('09:00', '17:00 PM')

    def test_calc_horas(self):
        self.assertEqual(calculate_hours('09:00', '12:00'), 3)
        self.assertEqual(calculate_hours('14:00', '17:00'), 3)

    def test_calculate_hours_with_break(self):
        self.assertEqual(calculate_hours('09:00', '17:00', '01:00'), 7)
        self.assertEqual(calculate_hours('14:00', '18:00', '00:30'), 3.5)

    def test_calculate_hours_with_swapped_times(self):
        self.assertEqual(calculate_hours('17:00', '09:00'), 16)

    def test_calculate_hours_with_alternate_formats(self):
        self.assertEqual(calculate_hours('9:00', '17:00'), 8)
        self.assertEqual(calculate_hours('0900', '1700'), 8)

if __name__ == '__main__':
    unittest.main()
