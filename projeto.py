# Importar a base de dados para o Python 
import pandas as pd
import numpy as np
import openpyxl
# Criação de gráficos
import matplotlib.pyplot as plt
import seaborn as sns
# Criação dos modelos
from sklearn.model_selection import train_test_split # Scikit-learn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
 
# Visualizar a base e fazer os ajustes na base de dados
tabela = pd.read_csv("Brasileirao2024 - Página1.csv")
print(tabela.head())

# Análise Exploratória
# Visualizar como as informações de cada item estão distribuídas e ver a correlação entre cada um dos itens. Existe correlação negativa também.

# Colunas úteis
tabela_interesse = tabela[[
    "Classificação",
    "Vitórias",
    "Empates",
    "Derrotas",
    "Gols Marcados",
    "Gols Sofridos",
    "Saldo de Gols"
]]

# Calcular correlações
correlacoes = tabela_interesse.corr(numeric_only=True)

#Criar o gráfico
plt.figure(figsize=(10, 6))
sns.heatmap(correlacoes, annot=True, cmap="coolwarm", fmt=".2f") #annot = notações/valores, cmap = cores
plt.title("Correlação entre Estatísticas do Brasileirão")
# Salva o gráfico
plt.savefig("grafico_correlacao.png")

# Modelo de Machine Learning
# O que eu quero prever é Y, o que está sendo usado para o aprendizado da previsão é o X

# X = dados de entrada | Remove a coluna Classificação da tabela
x = tabela_interesse.drop("Classificação", axis=1)

# Y = classificação (alvo) | Pega apenas a coluna "Classificação"
y = tabela_interesse["Classificação"]

# Divisão treino e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.5) # Pega 50% dos dados para fazer testes

# Cria e treina o modelo escolhido
modelo = LinearRegression()
modelo.fit(x_treino, y_treino)

# Previsão
previsoes = modelo.predict(x_teste)

#Avalia
print("r² (quanto o modelo explica):", r2_score(y_teste, previsoes))

# Cria uma nova tabela de resultados para mostrar a classificação real e o que o modelo previu
tabela_resultado = pd.DataFrame()
tabela_resultado["Real"] = y_teste.values
tabela_resultado["Previsto"] = np.round(previsoes, 1) # Arredonda os valores previstos para 1, facilitando a visualização

# Organiza os dados
tabela_resultado = tabela_resultado.sort_values(by="Real").reset_index(drop=True)

# Visualiza os coeficientes do modelo, o peso que cada variável teve para influenciar a classificação do modelo
coeficientes = pd.DataFrame(modelo.coef_, index=x.columns, columns=["Coeficiente"])
print(coeficientes)

#Cria o gráfico com duas linhas para comparar os dados reais com os dados previstos.
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))
sns.lineplot(data=tabela_resultado)
plt.title("Classificação Real vs Prevista (Regressão Linear)")
plt.ylabel("Classificação")
plt.xlabel("Times")
plt.xticks(rotation=45)
plt.savefig("grafico_resultado.png", dpi=300)
