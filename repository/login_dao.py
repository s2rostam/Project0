import psycopg2
from repository.connection import init_db_connection

from models.login_dto import Login

#CRUD

def create_user_login(username, password):
    conn = init_db_connection()
    cur = conn.cursor()

    insert_q = "INSERT INTO user_login VALUES (default, %s, %s) RETURNING user_id;"

    try:
        cur.execute(insert_q, (username, password))
        user_id = cur.fetchone()[0]
        conn.commit()
        return user_id
    except(psycopg2.DatabaseError) as err:
        print(err)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def get_user_login(username, password):
    conn = init_db_connection()
    cur = conn.cursor()

    read_q = f"SELECT * FROM user_login WHERE username='{username}' AND password='{password}';"

    try:
        cur.execute(read_q)
        user_info = cur.fetchone()
        if user_info is not None:
            return Login(user_info[0], user_info[1], user_info[2])
        return None
    except(psycopg2.DatabaseError) as err:
        print(err)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def get_user_login_by_id(id):
    conn = init_db_connection()
    cur = conn.cursor()

    read_q = f"SELECT username FROM user_login WHERE user_id={id};"

    try:
        cur.execute(read_q)
        user_info = cur.fetchone()[0]
        if user_info is not None:
            return user_info
        return None
    except(psycopg2.DatabaseError) as err:
        print(err)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def get_user_id_by_username(username):
    conn = init_db_connection()
    cur = conn.cursor()

    read_q = f"SELECT user_id FROM user_login WHERE username='{username}';"

    try:
        cur.execute(read_q)
        id = cur.fetchone()
        if (id is not None):
            return id[0]
    except(psycopg2.DatabaseError) as err:
        print(err)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def delete_user_login_by_id(id):
    conn = init_db_connection()
    cur = conn.cursor()

    try:
        cur.execute(f"DELETE FROM user_login WHERE user_id={id} RETURNING user_id;")
        id = cur.fetchone()[0]
        conn.commit()
        return id
    except psycopg2.DatabaseError as err:
        print(err)
        conn.rollback()
    finally:
        conn.close()