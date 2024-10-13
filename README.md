# Calculadora de Salário de Funcionários

Este projeto é uma calculadora de salário líquido para funcionários, implementada utilizando a técnica **Test Driven Development (TDD)**. O cálculo do salário líquido varia de acordo com o cargo do funcionário e segue regras específicas para DESENVOLVEDOR, DBA, TESTADOR e GERENTE.

## Funcionalidades

- Calcula o salário líquido de funcionários com base em seu cargo e salário-base.
- Regras de desconto diferentes para cada cargo:
  - **DESENVOLVEDOR**: 20% de desconto para salários ≥ 3.000,00; 10% para salários < 3.000,00.
  - **DBA e TESTADOR**: 25% de desconto para salários ≥ 2.000,00; 15% para salários < 2.000,00.
  - **GERENTE**: 30% de desconto para salários ≥ 5.000,00; 20% para salários < 5.000,00.

## Pré-requisitos

- Python 3.x instalado
- Bibliotecas padrão do Python

## Estrutura do Projeto

```bash
├── src
│   ├── funcionario.py      
│   └── calculadora_salario.py 
├── tests
│   └── test_calculadora_salario.py 
└── README.md
```

## Instruções de Build e Execução

### 1. Clonar o repositório

```bash
git clone https://github.com/Desduh/calculadora_salario_TDD
cd calculadora-salario
```

### 2. Instalar dependências

Este projeto utiliza apenas as bibliotecas padrão do Python, então não há necessidade de instalar pacotes externos.

### 3. Executar os testes

Os testes são escritos utilizando o **unittest**, uma biblioteca padrão do Python para testes. Para executar os testes:

```bash
python -m unittest discover tests
```

Este comando irá rodar todos os testes presentes no diretório \`tests\`. Se os testes passarem, o sistema está funcionando corretamente.