import psycopg2

def init_db_connection():
    conn = psycopg2.connect(
        host="testinstance.cdcrdkperkzv.us-east-2.rds.amazonaws.com",
        database="postgres",
        #change later?
        user="postgres",
        password="uhux5nrz"
    )
    return conn