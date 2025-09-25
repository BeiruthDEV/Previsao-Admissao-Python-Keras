<p align="center">
  <img src="assets/logo-vassouras.png" alt="Universidade de Vassouras" width="400"/>
</p>

<h3 align="center">
  Universidade de Vassouras  
</h3>

---

### 📚 Curso: **Engenharia de Software**  
### 🖥️ Disciplina: **Inteligência Artificial e Machine Learning**  
### 👨‍🎓 Autor: **Matheus Beiruth**

---






# 🎓 Previsão de Admissão com Modelo Keras

Este projeto foi desenvolvido para a disciplina de **Inteligência Artificial e Machine Learning**, com o objetivo de utilizar um **modelo Keras pré-treinado** para prever a **Chance of Admit** de candidatos com base em características fornecidas pelo usuário.

O sistema também implementa o **desafio opcional**: previsão em lote via arquivo CSV. 🚀

---

## 📌 Funcionalidades

✅ Carrega o modelo pré-treinado `modelo_treinado.keras`  
✅ Solicita as características ao usuário pelo terminal  
✅ Valida os valores conforme as regras de negócio  
✅ Gera a previsão e exibe em **percentual**  
✅ **Desafio Opcional:** permite previsão de múltiplos candidatos via CSV  
✅ Gera automaticamente um arquivo `predicoes_saida.csv` com as probabilidades  

---

## 🧠 Tecnologias Utilizadas

- **Python 3.9**
- **TensorFlow / Keras**
- **NumPy**
- **Pandas**

---

## 📂 Estrutura do Projeto
```bash
📦 PrevisaoAdmissao
┣ 📜 prever_admissao.py # Script principal
┣ 📜 modelo_treinado.keras # Modelo pré-treinado (fornecido pelo professor)
┣ 📜 entrada_teste.csv # CSV de exemplo para previsão em lote
┗ 📜 README.md # Este arquivo
```
---

## 🖥️ Como Executar

1. **Clone o repositório**
```bash
git clone https://github.com/BeiruthDEV/Previsao-Admissao-Keras.git
cd Previsao-Admissao-Keras
Instale as dependências
```

```bash

pip install tensorflow pandas numpy
Garanta que o modelo está na pasta
Baixe modelo_treinado.keras do AVA e coloque na raiz do projeto.
```

Execute o script

```bash

python prever_admissao.py
Escolha o modo

Digite 1 para previsão de um único candidato

Digite 2 para previsão via arquivo CSV (modo desafio opcional)
```

📊 Exemplo de Entrada (modo único)
```bash

text
Copiar código
GRE Score -> 312
TOEFL Score -> 109
University Rating -> 3
SOP -> 3
LOR -> 3
CGPA -> 8.69
Research -> 0
```

Saída esperada:
```bash

matlab
Chance prevista de admissão: 78.52%
```
📑 Exemplo de CSV (modo lote)

```bash

GRE Score,TOEFL Score,University Rating,SOP,LOR,CGPA,Research
312,109,3,3,3,8.69,0
330,115,5,5,5,9.5,1
280,90,2,2.5,2,7.0,0
300,100,3,4,4,8.2,1
340,120,5,5,5,9.9,1
```
Rodando no modo 2, será gerado um arquivo predicoes_saida.csv com o resultado de cada linha.

Matheus Beiruth
💼 Engenharia de Software | Backend Developer

Este projeto foi desenvolvido para fins acadêmicos, como parte do trabalho da disciplina.