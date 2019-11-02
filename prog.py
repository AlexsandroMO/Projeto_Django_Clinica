import pandas as pd
import pandasql as pdsql
import sqlite3

def read_sql(coluna):
  conn = sqlite3.connect('db.sqlite3')

  qsl_datas = f"""
                  SELECT * FROM {coluna};
  """

  read_db = pd.read_sql_query(qsl_datas, conn)
  conn.close()

  return read_db


def query_sql():
  coluna0 = 'clinica_exame'
  df = read_sql(coluna0)

  coluna1 = 'clinica_paciente'
  df2 = read_sql(coluna1)

  coluna2 = 'clinica_cliente'
  df3 = read_sql(coluna2)

  coluna3 = 'clinica_NomeExame'
  df4 = read_sql(coluna3)

  lista_exames = []

  for i in df.index:
    nomes_exames = df['lista_exames'][i]
    id_nome = df['nome_paciente_id'][i]
    lista = nomes_exames.split('\r\n')
    lista_empresa = df2[df2['id'] == id_nome]['empresa_id']
    for a in lista_empresa:
      l = df3[df3['id'] == a]['nome_empresa']
      for b in l:
        id_empresa = b
    lista_exames.append([id_empresa, lista])

  df_controle = pd.DataFrame(data=lista_exames, columns=['EMPRESA','LISTA_EXAMES'])

  cotation = []

  for i in df3['nome_empresa']:
    for a in range(len(df_controle['EMPRESA'])):
      company = df_controle['EMPRESA'][a]
      if company == i:
        lista_cliente = df_controle['LISTA_EXAMES'][a]
        for b in lista_cliente:
          valor = df4[df4['nome_exame'] == b]['valor_exame']
          for c in valor:
            cotation.append([company, b, c])

  #new_df = pd.DataFrame(data=cotation,columns=['EMPRESA','VALOR','EXAMES'])
  a = []
  for i in cotation:
    a.append(i[2])

  new_df = [cotation, sum(a)]

  return new_df
