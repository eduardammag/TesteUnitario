import unittest

import unittest
from unittest.mock import patch

from date_dif import diferenca_datgitte_console, diferenca_date_arquivo

class TestDiferencaDates(unittest.TestCase):

    def test_diferenca_date_console(self):
        # Redefine a entrada para simular a entrada do usuário
        with patch('builtins.input', side_effect=["10 de Setembro de 2023 - 20 de Setembro de 2023"]):
            resultado = diferenca_date_console()
            self.assertEqual(resultado, 10)

    def test_diferenca_date_arquivo(self):
        # Cria um arquivo temporário com datas
        with open('datas_temporarias.txt', 'w', encoding='utf-8') as f:
            f.write("10 de Setembro de 2023 - 20 de Setembro de 2023")

        resultado = diferenca_date_arquivo('datas_temporarias.txt')
        self.assertEqual(resultado, 10)

if __name__ == '__main__':
    unittest.main()
