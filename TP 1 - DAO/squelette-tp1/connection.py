import psycopg2

connection = psycopg2.connect(host="sgbd-eleves.domensai.ecole", port="5432",
                              database="MY_ID", user="MY_ID", password="MY_ID")
