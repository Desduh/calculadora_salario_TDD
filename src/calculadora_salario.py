class CalculadoraSalario:
    def calcular(self, funcionario):
        regras = {
            "DESENVOLVEDOR": self._calcular_salario_desenvolvedor,
            "DBA": self._calcular_salario_dba_ou_testador,
            "TESTADOR": self._calcular_salario_dba_ou_testador,
            "GERENTE": self._calcular_salario_gerente
        }
        
        if funcionario.cargo in regras:
            return regras[funcionario.cargo](funcionario.salario_base)
        else:
            raise ValueError("Cargo inválido")
    
    def _calcular_salario_desenvolvedor(self, salario_base):
        return salario_base * 0.8 if salario_base >= 3000 else salario_base * 0.9
    
    def _calcular_salario_dba_ou_testador(self, salario_base):
        return salario_base * 0.75 if salario_base >= 2000 else salario_base * 0.85

    def _calcular_salario_gerente(self, salario_base):
        return salario_base * 0.7 if salario_base >= 5000 else salario_base * 0.8
