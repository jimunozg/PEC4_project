import unittest
import pandas as pd
import os
from PEC4.Ex1.Ex1 import ex1
from PEC4.Ex2.Ex2 import ex2
from PEC4.Ex3.Ex3 import ex3
from PEC4.Ex4.Ex4 import ex4
from PEC4.Ex5.Ex5 import ex5
from PEC4.main import main
from unittest.mock import patch
from io import StringIO


class TestPEC4(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para las pruebas."""
        # Carga inicial del dataset
        self.data = ex1()
        self.assertIsNotNone(self.data, "El dataset no debería ser None.")

    def test_ex1_import(self):
        """Prueba que ex1 importe correctamente el dataset."""
        self.assertFalse(self.data.empty, "El dataset no debería estar vacío.")
        self.assertTrue(all(col in self.data.columns for col in ['dorsal', 'biker', 'club', 'time']), "Falta una columna esperada en el dataset.")

    def test_ex2_cleaning(self):
        """Prueba que ex2 limpie y anonimize el dataset."""
        self.data2 = ex2(self.data)
        self.assertTrue('biker' in self.data2.columns, "Falta la columna anonimizada.")
        self.assertNotEqual(self.data['biker'].to_list(), self.data2['biker'].to_list(), "La columna original debería haber sido eliminada.")

    def test_ex3_grouping(self):
        """Prueba que ex3 agrupe correctamente y genere el histograma."""
        self.data3, data_grouped = ex3(self.data)
        self.assertIn('time_grouped', self.data3.columns, "Falta la columna agrupada.")
        self.assertGreater(len(data_grouped), 0, "El agrupamiento no debería ser vacío.")

        hist_path = './img/histograma.png'
        self.assertTrue(os.path.exists(hist_path), f"El histograma no se ha creado en la ruta esperada: {hist_path}")
        self.assertGreater(os.path.getsize(hist_path), 0, f"El archivo del histograma está vacío: {hist_path}")

    def test_ex4_club_grouping(self):
        """Prueba que ex4 agrupe por clubes."""
        self.data4, clubs_grouped = ex4(self.data)
        self.assertIn('club_clean', self.data4.columns, "Falta la columna 'club_clean' en los datos actualizados.")
        self.assertGreater(clubs_grouped.shape[0], 0, "Los datos agrupados por clubes no deberían estar vacíos.")

    def test_ex5_analysis(self):
        """Prueba que ex5 realice el análisis final sin errores."""
        try:
            self.data4, _ = ex4(self.data)
            ex5(self.data4)
        except Exception as e:
            self.fail(f"ex5 falló con la excepción: {e}")

    @patch('builtins.input', side_effect=['999', '0'])  # Entrada no válida, luego salir
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_input(self, mock_stdout, mock_input):
        """Prueba que el programa maneje entradas no válidas."""
        main()  # Ejecuta la función principal

        # Verifica que se muestra el mensaje de error correcto
        output = mock_stdout.getvalue()
        self.assertIn("Por favor, selecciona una opción del 0 al 6.", output)

    @patch('builtins.input', side_effect=['2', '0'])  # El usuario intenta ejecutar ex2 sin haber ejecutado ex1
    @patch('sys.stdout', new_callable=StringIO)
    def test_missing_prerequisite(self, mock_stdout, mock_input):
        """Prueba que el programa maneje la falta de ejecución de ejercicios previos."""
        main()  # Ejecuta la función principal

        # Verifica que se muestra el mensaje de advertencia correcto
        output = mock_stdout.getvalue()
        self.assertIn("Por favor, ejecuta primero el ejercicio 1.", output)


if __name__ == '__main__':
    unittest.main()
