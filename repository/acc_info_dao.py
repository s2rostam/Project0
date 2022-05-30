import psycopg2
from repository.connection import init_db_connection

from models.account_info_dto import Account

#CRUD

def create_user_account_info(id):
    conn = init_db_connection()
    cur = conn.cursor()

    insert_q = f"INSERT INTO user_account_info VALUES ({id}, default, default) RETURNING user_id;"

    try:
        cur.execute(insert_q)
        acc_id = cur.fetchone()[0]
        conn.commit()
        return acc_id
    except(psycopg2.DatabaseError) as err:
        print(err)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def get_user_account_info(id):
    conn = init_db_connection()
    cur = conn.cursor()

    read_q = f"SELECT * FROM user_account_info WHERE user_id={id};"

    try:
        cur.execute(read_q)
        acc_info = cur.fetchone()
        if acc_info is not None:
            return Account(acc_info[0], acc_info[1], acc_info[2])
        return None
    except(psycopg2.DatabaseError) as err:
        print(err)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def update_user_account_info(id, acc, money_amount, curr_money):
    conn = init_db_connection()
    cur = conn.cursor()

    if acc == "chq":
        acc = "chequeing"
    else:
        acc == "saving"

    new_total = money_amount + curr_money
    update_q = f"UPDATE user_account_info SET {acc}_amount = {new_total} where user_id = {id} RETURNING user_id;"

    try:
        cur.execute(update_q)
        id = cur.fetchone()[0]
        conn.commit()
        return id
    except(psycopg2.DatabaseError) as err:
        print(err)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def delete_user_account_info(id):
    conn = init_db_connection()
    cur = conn.cursor()

    try:
        cur.execute(f"DELETE FROM user_account_info WHERE user_id={id} RETURNING user_id;")
        id = cur.fetchone()[0]
        conn.commit()
        return id
    except psycopg2.DatabaseError as err:
        print(err)
        conn.rollback()
    finally:
        conn.close()