import csv
import psycopg2

# Estabelece a conexão com o banco de dados 
con = psycopg2.connect(
    host="localhost",
    database="labbanco",
    user="postgree",
    password="root",
)

# Cria o cursor
cur = con.cursor()

# Acessa o arquivo .csv
with open('tusss.csv', newline='', encoding='latin1') as csvFile:

    reader = csv.reader(csvFile, delimiter=';')  # Especificando o delimitador ';'
    skipHeader = next(reader)  # Pula o cabeçalho
    for row in reader:
        if len(row) < 5:  # Se a linha tiver menos de 5 colunas, pula a linha
            continue
        
        cod_tuss = row[0]
        nom_termo_tuss = row[1]  # A coluna nom_termo_tuss é a segunda (index 1)
        num_grau_equivalencia = row[2]
        num_codigo_sus = row[3]
        nom_procedimento_sus = row[4]

        # Insere os dados na tabela do banco
        cur.execute('''INSERT INTO HOSPITAL.TUSS_SIGTAP(cod_tuss, nom_termo_tuss, num_grau_equivalencia, num_codigo_sus, nom_procedimento_sus)
            VALUES (%s, %s, %s, %s, %s)''', (cod_tuss, nom_termo_tuss, num_grau_equivalencia, num_codigo_sus, nom_procedimento_sus))


con.commit()

con.close()
