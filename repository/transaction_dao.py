import psycopg2
from repository.connection import init_db_connection

from models.transaction_dto import Transaction

#CRUD

def create_transaction_log(id, name, amount, transaction_type, location):
    conn = init_db_connection()
    cur = conn.cursor()

    insert_q = f"INSERT INTO user_transaction_info VALUES (default, {id}, '{name}', {amount}, '{transaction_type}', '{location}') RETURNING transaction_id;"

    try:
        cur.execute(insert_q)
        id = cur.fetchone()[0]
        conn.commit()
        return id
    except(psycopg2.DatabaseError) as err:
        print(err)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def get_transaction_log(id, acc):
    conn = init_db_connection()
    cur = conn.cursor()

    if acc == "chequeing":
        acc = 'chq'
    if acc == "saving":
        acc = 'sav'

    print(acc)

    read_q = f"SELECT * FROM user_transaction_info WHERE user_id={id} AND transaction_location='{acc}';"

    try:
        cur.execute(read_q)
        transactions_list = cur.fetchall()
        if len(transactions_list) > 0:
            print(transactions_list)
            all_transac = list()
            for t in transactions_list:
                all_transac.append(Transaction(t[0], t[1], t[2], t[3], t[4], t[5]))
            print(all_transac)
            return all_transac
        return "Nothing here yet..."
    except(psycopg2.DatabaseError) as err:
        print(err)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def delete_transaction_logs(id):
    conn = init_db_connection()
    cur = conn.cursor()

    try:
        cur.execute(f"DELETE FROM user_transaction_info WHERE user_id={id};")
        conn.commit()
    except psycopg2.DatabaseError as err:
        print(err)
        conn.rollback()
    finally:
        conn.close()