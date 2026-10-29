"""Автоматические тесты калькулятора на unittest."""
import sys
import unittest
from pathlib import Path

# Позволяет запускать тесты из корня репозитория без установки пакета.
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "projects"))

from calculator import calculate  # noqa: E402


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(2, "+", 3), 5)

    def test_subtraction(self):
        self.assertEqual(calculate(7, "-", 2), 5)

    def test_multiplication(self):
        self.assertEqual(calculate(4, "*", 3), 12)

    def test_division(self):
        self.assertEqual(calculate(8, "/", 2), 4)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(5, "/", 0)

    def test_unknown_operator(self):
        with self.assertRaises(ValueError):
            calculate(1, "%", 2)


if __name__ == "__main__":
    unittest.main()
