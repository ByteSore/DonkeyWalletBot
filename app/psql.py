#!/usr/bin/python
import psycopg2
from config import dbconfig

def query(sql, data):
    conn = None
    try:
        params = dbconfig()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql,data)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        dc(conn)

def selectone(sql, data):
    conn = None
    results = None
    try:
        params = dbconfig()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(sql, data)
        results = cur.fetchone()
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        dc(conn)
        return results

def select(sql, data):
    conn = None
    results = None
    try:
        params = dbconfig()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(sql, data)
        results = cur.fetchall()
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        dc(conn)
        return results

def dc(conn):
    if conn is not None:
        conn.close()