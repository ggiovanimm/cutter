import pandas as pd
import sqlite3

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Lendo o arquivo Excel
excel_file = 'cutter.xlsx'  # Altere para o nome do seu arquivo
df = pd.read_excel(excel_file)

# Iterando sobre as linhas do DataFrame e inserindo no banco de dados
for index, row in df.iterrows():
    autoria = row['Nome']  # Campo que corresponde à autoria
    titulo = row['Cutter']  # Campo que corresponde ao cutter

    # Comando SQL para inserir os dados na tabela Cutter
    cursor.execute('INSERT INTO cutter_cutter (autoria, titulo) VALUES (?, ?)', (autoria, titulo))

# Commit e fechamento da conexão
conn.commit()
conn.close()

print('Importação concluída com sucesso!')
