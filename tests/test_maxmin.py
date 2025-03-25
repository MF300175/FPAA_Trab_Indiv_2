import unittest
import sys
import os

# Adiciona o diretório src ao path do Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.main import find_max_min

class TestMaxMinSelect(unittest.TestCase):
    def test_array_vazio(self):
        """Testa o caso de array vazio"""
        max_element, min_element = find_max_min([])
        self.assertIsNone(max_element)
        self.assertIsNone(min_element)

    def test_array_um_elemento(self):
        """Testa o caso de array com um elemento"""
        max_element, min_element = find_max_min([5])
        self.assertEqual(max_element, 5)
        self.assertEqual(min_element, 5)

    def test_array_dois_elementos(self):
        """Testa o caso de array com dois elementos"""
        max_element, min_element = find_max_min([3, 1])
        self.assertEqual(max_element, 3)
        self.assertEqual(min_element, 1)

    def test_array_elementos_iguais(self):
        """Testa o caso de array com elementos iguais"""
        max_element, min_element = find_max_min([5, 5, 5, 5])
        self.assertEqual(max_element, 5)
        self.assertEqual(min_element, 5)

    def test_array_elementos_negativos(self):
        """Testa o caso de array com elementos negativos"""
        max_element, min_element = find_max_min([-1, -5, -3, -2])
        self.assertEqual(max_element, -1)
        self.assertEqual(min_element, -5)

    def test_array_elementos_mistos(self):
        """Testa o caso de array com elementos positivos e negativos"""
        max_element, min_element = find_max_min([-1, 5, -3, 2])
        self.assertEqual(max_element, 5)
        self.assertEqual(min_element, -3)

    def test_array_grande(self):
        """Testa o caso de array grande"""
        arr = list(range(1000))
        max_element, min_element = find_max_min(arr)
        self.assertEqual(max_element, 999)
        self.assertEqual(min_element, 0)

if __name__ == '__main__':
    unittest.main() 