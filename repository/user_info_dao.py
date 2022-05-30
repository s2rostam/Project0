import psycopg2
from repository.connection import init_db_connection

from models.user_info_dto import Userinfo

#CRUD

def create_user_info(id, firstname, lastname):
    conn = init_db_connection()
    cur = conn.cursor()

    insert_q = f"INSERT INTO user_info VALUES ({id}, '{firstname}', '{lastname}') RETURNING user_id;"

    try:
        cur.execute(insert_q)
        user_id = cur.fetchone()[0]
        conn.commit()
        return user_id
    except(psycopg2.DatabaseError) as err:
        print(err)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def get_user_info(id):
    conn = init_db_connection()
    cur = conn.cursor()

    read_q = f"SELECT * FROM user_info WHERE user_id={id};"

    try:
        cur.execute(read_q)
        user_info = cur.fetchone()
        if user_info is not None:
            return Userinfo(user_info[0], user_info[1], user_info[2])
        return None
    except(psycopg2.DatabaseError) as err:
        print(err)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def delete_user_info_by_id(id):
    conn = init_db_connection()
    cur = conn.cursor()

    try:
        cur.execute(f"DELETE FROM user_info WHERE user_id={id} RETURNING user_id;")
        id = cur.fetchone()[0]
        conn.commit()
        return id
    except psycopg2.DatabaseError as err:
        print(err)
        conn.rollback()
    finally:
        conn.close()