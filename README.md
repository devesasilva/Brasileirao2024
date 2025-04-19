# Análise Estatística do Brasileirão 2024

Este projeto é uma análise exploratória e um experimento bem simples de machine learning baseado em dados estatísticos do Campeonato Brasileiro (Brasileirão). Tem como objetivo principal observar correlações entre variáveis como gols, vitórias, derrotas, empates e a classificação final dos clubes. Além disso, foi aplicado um modelo de Regressão Linear para prever a classificação dos times com base nesses dados.

---

## Sobre a Base de Dados

A base utilizada contém informações finais da temporada de 2024, incluindo:

- Classificação final
- Pontos
- Partidas disputadas
- Vitórias, empates e derrotas
- Gols marcados e sofridos
- Saldo de gols

---

## O que foi feito

- Importação e limpeza da base de dados
- Seleção de variáveis relevantes para análise
- Cálculo de correlação entre as variáveis
- Visualização com heatmap
- Criação de um modelo de Regressão Linear para prever a classificação
- Comparação entre valores reais e previstos
- Visualização dos resultados com gráficos

---

## Ferramentas Utilizadas

- **Python 3.13.2**
- **Pandas** para manipulação de dados
- **Seaborn e Matplotlib** para visualizações
- **Scikit-learn** para modelagem estatística (regressão linear)
- **VSCode** (ambiente de desenvolvimento)

---

## Mini Experimento com Machine Learning

Aplicamos um modelo de Regressão Linear simples, com divisão entre dados de treino e teste. Embora o modelo não tenha objetivo de ser altamente preciso (já que estamos lidando com dados de uma temporada já encerrada e uma base de dados relativamente pequena), ele oferece insights interessantes sobre o quanto as variáveis influenciam a classificação dos times.

Resultado do modelo (R²): 0.8318618834202244 ou 83% 

