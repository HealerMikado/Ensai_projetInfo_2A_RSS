import psycopg2

# 
# Classe technique qui permet xde se conencter à une base de données
#
  
connection = psycopg2.connect(host="localhost", port="5432",
                              database="postgres", user="postgres", password="postgres")
