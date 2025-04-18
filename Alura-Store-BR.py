# -*- coding: utf-8 -*-
"""AluraStoreBr.ipynb

### Importação dos dados
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

loja = pd.read_csv(url)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)

loja.head()

# Categoria do Produto

from matplotlib import pyplot as plt

loja.groupby('Categoria do Produto').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

""" 1. Análise do faturamento """
# Soma os valores da coluna Preço de cada loja para estimar o faturamento.

# Calcula o faturamento para cada loja
revenue_loja1 = loja['Preço'].sum()
revenue_loja2 = loja2['Preço'].sum()
revenue_loja3 = loja3['Preço'].sum()
revenue_loja4 = loja4['Preço'].sum()

# Imprime o faturamento para cada loja
print(f"Loja 1 Revenue: {revenue_loja1}")
print(f"Loja 2 Revenue: {revenue_loja2}")
print(f"Loja 3 Revenue: {revenue_loja3}")
print(f"Loja 4 Revenue: {revenue_loja4}")

# Cria um gráfico de barras
revenue_data = {
    'Loja': ['Loja 1', 'Loja 2', 'Loja 3', 'Loja 4'],
    'Faturamento': [revenue_loja1, revenue_loja2, revenue_loja3, revenue_loja4]
}
revenue_df = pd.DataFrame(revenue_data)

plt.figure(figsize=(8, 6))
sns.barplot(x='Loja', y='Faturamento', data=revenue_df, palette="viridis")
plt.title('Faturamento por Loja')
plt.xlabel('Loja')
plt.ylabel('Faturamento')
plt.show()

""" 2. Vendas por Categoria """
# Calcula as vendas por Categoria de Produto.
all_stores = pd.concat([loja, loja2, loja3, loja4])

# Calcula as vendas por categoria
sales_by_category = all_stores.groupby('Categoria do Produto')['Preço'].sum()

# Cria um gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(sales_by_category, labels=sales_by_category.index, autopct='%1.1f%%', startangle=90)
plt.title('Vendas por Categoria (Todas as Lojas)')
plt.axis('equal')
plt.show()

""" 3. Média de Avaliação das Lojas """
# Faz a média de avaliação da compra de todas as lojas.

# Calcula a média por cada loja
average_rating_loja1 = loja['Avaliação da compra'].mean()
average_rating_loja2 = loja2['Avaliação da compra'].mean()
average_rating_loja3 = loja3['Avaliação da compra'].mean()
average_rating_loja4 = loja4['Avaliação da compra'].mean()

# Imprime a média
print(f"Loja 1 Average Rating: {average_rating_loja1}")
print(f"Loja 2 Average Rating: {average_rating_loja2}")
print(f"Loja 3 Average Rating: {average_rating_loja3}")
print(f"Loja 4 Average Rating: {average_rating_loja4}")

# Calcula a avalialçao geral de todas as lojas
overall_average_rating = (average_rating_loja1 + average_rating_loja2 + average_rating_loja3 + average_rating_loja4) / 4

print(f"Overall Average Rating: {overall_average_rating}")

overall_average_rating_alt = all_stores['Avaliação da compra'].mean()
print(f"Overall Average Rating (Alternative): {overall_average_rating_alt}")

""" 4. Produtos Mais e Menos Vendidos """
# Mostra quais foram os produtos mais e menos vendidos
all_stores = pd.concat([loja, loja2, loja3, loja4])

# Conta a ocorrência de cada produto
product_counts = all_stores['Produto'].value_counts()

# Seleciona os 10 produtos mais vendidos
top_products = product_counts.head(10)

print("Top 10 Produtos mais vendidos:")
top_products

""" 5. Frete Médio por Loja """
# Calcula o valor médio dos fretes por loja, e gera um gráfico de barras.

# Calcula o preço médio do frete para cada loja.
average_freight_loja1 = loja['Frete'].mean()
average_freight_loja2 = loja2['Frete'].mean()
average_freight_loja3 = loja3['Frete'].mean()
average_freight_loja4 = loja4['Frete'].mean()

# Cria um gráfico de barras com o custo médio do frete para cada loja.
freight_data = {
    'Loja': ['Loja 1', 'Loja 2', 'Loja 3', 'Loja 4'],
    'Frete Médio': [average_freight_loja1, average_freight_loja2, average_freight_loja3, average_freight_loja4]
}
freight_df = pd.DataFrame(freight_data)

plt.figure(figsize=(8, 6))
sns.barplot(x='Loja', y='Frete Médio', data=freight_df, palette="viridis")
plt.title('Frete Médio por Loja')
plt.xlabel('Loja')
plt.ylabel('Frete Médio')
plt.show()
