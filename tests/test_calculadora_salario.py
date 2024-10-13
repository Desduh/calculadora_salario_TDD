import unittest
from src.funcionario import Funcionario
from src.calculadora_salario import CalculadoraSalario

class TestCalculadoraSalario(unittest.TestCase):
    
    def setUp(self):
        self.calculadora = CalculadoraSalario()

    def test_salario_desenvolvedor_maior_3000(self):
        funcionario = Funcionario("João", "joao@example.com", 4000.0, "DESENVOLVEDOR")
        salario_liquido = self.calculadora.calcular(funcionario)
        self.assertEqual(salario_liquido, 3200.0)

    def test_salario_desenvolvedor_menor_3000(self):
        funcionario = Funcionario("Maria", "maria@example.com", 2500.0, "DESENVOLVEDOR")
        salario_liquido = self.calculadora.calcular(funcionario)
        self.assertEqual(salario_liquido, 2250.0)

    def test_salario_dba_maior_2000(self):
        funcionario = Funcionario("Carlos", "carlos@example.com", 2500.0, "DBA")
        salario_liquido = self.calculadora.calcular(funcionario)
        self.assertEqual(salario_liquido, 1875.0)

    def test_salario_dba_menor_2000(self):
        funcionario = Funcionario("Ana", "ana@example.com", 1500.0, "DBA")
        salario_liquido = self.calculadora.calcular(funcionario)
        self.assertEqual(salario_liquido, 1275.0)

    def test_salario_testador_maior_2000(self):
        funcionario = Funcionario("Pedro", "pedro@example.com", 2500.0, "TESTADOR")
        salario_liquido = self.calculadora.calcular(funcionario)
        self.assertEqual(salario_liquido, 1875.0)

    def test_salario_testador_menor_2000(self):
        funcionario = Funcionario("Paula", "paula@example.com", 1500.0, "TESTADOR")
        salario_liquido = self.calculadora.calcular(funcionario)
        self.assertEqual(salario_liquido, 1275.0)

    def test_salario_gerente_maior_5000(self):
        funcionario = Funcionario("José", "jose@example.com", 6000.0, "GERENTE")
        salario_liquido = self.calculadora.calcular(funcionario)
        self.assertEqual(salario_liquido, 4200.0)

    def test_salario_gerente_menor_5000(self):
        funcionario = Funcionario("Julia", "julia@example.com", 4000.0, "GERENTE")
        salario_liquido = self.calculadora.calcular(funcionario)
        self.assertEqual(salario_liquido, 3200.0)

if __name__ == "__main__":
    unittest.main()
