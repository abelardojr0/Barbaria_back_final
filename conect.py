
import psycopg2

host = "localhost"
database = "barbearia"
user = "postgres"
password = "123456"
port = "5432"

def fazerConexao():
  try:
     conn = psycopg2.connect(
       host=host,
       database=database,
       user=user,
       password=password,
       port=port
     )
     return conn
  except:
    return "Falha ao conectar no banco"