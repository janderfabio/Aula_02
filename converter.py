import pandas as pd

# Lê o arquivo XLS
df = pd.read_excel('estimativa2025.xls')

# Salva no formato CSV
df.to_csv('estimativa2025.csv', index=False, encoding='utf-8')

print('Conversão concluída com sucesso!')
