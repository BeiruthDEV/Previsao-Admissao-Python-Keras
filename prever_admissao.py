#!/usr/bin/env python3
# prever_admissao.py
# Script simples para carregar um modelo Keras e prever "Chance of Admit".
# Executar: python prever_admissao.py

import sys
import numpy as np
import pandas as pd
from keras.models import load_model

COLUNAS = ["GRE Score", "TOEFL Score", "University Rating", "SOP", "LOR", "CGPA", "Research"]

def pedir_valor(nome, inteiro=False, minimo=None, maximo=None, escolhas=None):
    """Pede valor no console e valida conforme parâmetros."""
    while True:
        entrada = input(f"{nome} -> ").strip()
        try:
            if inteiro:
                valor = int(entrada)
            else:
                valor = float(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número.")
            continue
        if escolhas is not None and valor not in escolhas:
            print(f"Valor inválido. Deve ser um de: {escolhas}")
            continue
        if minimo is not None and valor < minimo:
            print(f"Valor deve ser >= {minimo}.")
            continue
        if maximo is not None and valor > maximo:
            print(f"Valor deve ser <= {maximo}.")
            continue
        return valor

def prever_unico(modelo):
    valores = []
    for col in COLUNAS:
        if col == "GRE Score":
            v = pedir_valor(col, inteiro=True, minimo=260, maximo=340)
        elif col == "TOEFL Score":
            v = pedir_valor(col, inteiro=True, minimo=0, maximo=120)
        elif col == "University Rating":
            v = pedir_valor(col, inteiro=True, minimo=1, maximo=5)
        elif col == "SOP":
            v = pedir_valor(col, inteiro=False, minimo=1, maximo=5)
        elif col == "LOR":
            v = pedir_valor(col, inteiro=False, minimo=1, maximo=5)
        elif col == "CGPA":
            v = pedir_valor(col, inteiro=False, minimo=0.0, maximo=10.0)
        elif col == "Research":
            v = pedir_valor(col, inteiro=True, escolhas=[0, 1])
        valores.append(v)

    entrada = np.array([valores], dtype=float)  # formato (1, n_features)
    pred = modelo.predict(entrada, verbose=0)
    chance = float(np.ravel(pred)[0])
    print(f"\nChance prevista de admissão: {chance*100:.2f}%\n")

def prever_lote_csv(modelo):
    caminho = input("Caminho do CSV (colunas devem ser exatamente):\n" + ", ".join(COLUNAS) + "\n-> ").strip()
    try:
        df = pd.read_csv(caminho)
    except Exception as e:
        print("Erro ao ler CSV:", e)
        return
    faltando = [c for c in COLUNAS if c not in df.columns]
    if faltando:
        print("CSV inválido. Faltam colunas:", faltando)
        return
    entrada = df[COLUNAS].astype(float).values
    preds = modelo.predict(entrada, verbose=0).ravel()
    df['Chance_of_Admit'] = preds
    df['Chance_of_Admit_%'] = (df['Chance_of_Admit'] * 100).round(2)
    saida = 'predicoes_saida.csv'
    df.to_csv(saida, index=False)
    print(f"Predições gravadas em '{saida}'. Primeiras 5 linhas com chance (%):")
    print(df[COLUNAS + ['Chance_of_Admit_%']].head())

def main():
    # carregar modelo
    try:
        modelo = load_model('modelo_treinado.keras')
    except Exception as e:
        print("Não foi possível carregar 'modelo_treinado.keras'.")
        print("Coloque o arquivo 'modelo_treinado.keras' no mesmo diretório deste script.")
        print("Erro:", e)
        sys.exit(1)

    modo = input("Modo: 1 = único candidato, 2 = CSV em lote [1/2]: ").strip()
    if modo == '2':
        prever_lote_csv(modelo)
    else:
        prever_unico(modelo)

if __name__ == "__main__":
    main()
