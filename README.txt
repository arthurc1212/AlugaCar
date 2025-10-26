# 🚗 AlugaCar — Sistema simples de aluguel de carros (Python + Orientação a Objetos)

## 🧾 Descrição
O **AlugaCar** é um projeto em **Python** que simula um sistema de **aluguel de carros entre usuários**.  
Com ele, é possível:

- Cadastrar **usuários**;  
- Cadastrar **carros** e associar um dono;  
- **Listar carros disponíveis**;  
- **Alugar** e **devolver** carros;  
- Tudo isso através de um **menu interativo no terminal**.

O projeto foi feito de forma **clara e didática**, pensado para alunos que estão **começando em Orientação a Objetos (OO)**.

---

## 🧱 Estrutura do Projeto

```
AlugaCar/
│
├── usuario.py     # Classe Usuario
├── carro.py       # Classe Carro
├── sistema.py     # Classe Sistema (controla usuários e carros)
└── main.py        # Programa principal com menu interativo
```

---

## 🧩 Classes e responsabilidades

| Classe | Responsabilidade | Principais métodos |
|---------|------------------|--------------------|
| **Usuario** | Representa uma pessoa cadastrada no sistema | `__init__`, `__str__` |
| **Carro** | Representa um carro disponível ou alugado | `alugar()`, `devolver()`, `__str__()` |
| **Sistema** | Gerencia usuários, carros e aluguéis | `cadastrar_usuario()`, `cadastrar_carro()`, `listar_carros()`, `alugar_carro()`, `devolver_carro()` |

---

## 🧠 Conceitos de Orientação a Objetos usados

| Conceito | Explicação | Exemplo no código |
|-----------|-------------|------------------|
| **Classe** | Define um modelo de algo do mundo real | `class Carro:` |
| **Objeto** | Instância de uma classe | `carro1 = Carro("Gol", 2015, 100.0, dono)` |
| **Método** | Função dentro de uma classe | `alugar()`, `devolver()` |
| **Encapsulamento** | Mantém os dados organizados e seguros | Atributos dentro das classes |
| **Relacionamento** | Classes interagem entre si | `Sistema` usa `Usuario` e `Carro` |

---

## 💻 Como Executar

### 1. Requisitos
- Python 3.8 ou superior  
- Nenhuma biblioteca externa é necessária.

### 2. Executar o programa
Abra o terminal na pasta do projeto e digite:
```bash
python main.py
```

---

## 🧭 Menu do sistema

```
========== MENU ==========
1. Cadastrar Usuário
2. Cadastrar Carro
3. Listar Carros
4. Alugar Carro
5. Devolver Carro
6. Sair
==========================
```

---

## 🧪 Exemplo de execução

```
========== MENU ==========
1. Cadastrar Usuário
2. Cadastrar Carro
3. Listar Carros
4. Alugar Carro
5. Devolver Carro
6. Sair
==========================
Escolha uma opção: 1
Nome do usuário: Alice
Email do usuário: alice@email.com
✅ Usuário Alice cadastrado com sucesso!

Escolha uma opção: 2
Usuários cadastrados:
1. Alice
Escolha o dono do carro: 1
Modelo do carro: Gol
Ano: 2015
Preço por dia (R$): 100
🚗 Carro Gol cadastrado por Alice!

Escolha uma opção: 3
🚘 Carros disponíveis:
1. Gol (2015) - R$100.0/dia - Disponível

Escolha uma opção: 4
Escolha o número do carro para alugar: 1
✅ Você alugou o carro Gol com sucesso!

Escolha uma opção: 3
🚘 Carros disponíveis:
1. Gol (2015) - R$100.0/dia - Alugado
```

---

## 📘 Conclusão
Este projeto foi feito para **facilitar o aprendizado** dos conceitos fundamentais de **Programação Orientada a Objetos (POO)**:  
- Criação e uso de classes;  
- Relação entre objetos;  
- Encapsulamento e métodos;  
- Estrutura modular e clara.