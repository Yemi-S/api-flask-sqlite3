from sqlite3 import Error
import sqlite3;
from .connection import create_connection;

def insert_task(data):
    conn = create_connection();

    sql = """ INSERT INTO tasks (title, created_date) 
              VALUES (?, ?)
    """;
    try:
        cur = conn.cursor();
        cur.execute(sql, data);
        conn.commit();
        return cur.lastrowid;
    except Error as e:
        print("Error at insert_task(): ",str(e));
        return False;
    finally:
        if conn:
            cur.close();
            conn.close();

def select_task_by_id(_id):
    conn = create_connection();

    sql = f"SELECT * FROM tasks WHERE id = {_id}";

    try:
        conn.row_factory = sqlite3.Row;
        cur = conn.cursor();
        cur.execute(sql);
        task = dict(cur.fetchone());
        return task;
    except Error as e:
        print("Error at select_task_by_id(): ",str(e));
        return False;
    finally:
        if conn:
            cur.close();
            conn.close();

def select_all_tasks():
    conn = create_connection();

    sql = "SELECT * FROM tasks";
    try:
        conn.row_factory = sqlite3.Row;
        cur = conn.cursor();
        cur.execute(sql);
        tasks_rows = cur.fetchall();
        tasks = [dict(row) for row in tasks_rows];
        return tasks;
    except Error as e:
        print("Error at select_task_by_id(): ",str(e));
        return False;
    finally:
        if conn:
            cur.close();
            conn.close();

def update_task(_id, data):
    conn = create_connection();

    sql = f""" UPDATE tasks SET title = ?
              WHERE id = {_id} """;
    try:
        cur = conn.cursor();
        cur.execute(sql, data);
        conn.commit();
        return True;
    except Error as e:
        print("Error at update_task(): ",str(e));
        return False;
    finally:
        if conn:
            cur.close();
            conn.close();

def delete_task(_id):
    conn = create_connection();

    sql = f"DELETE FROM tasks WHERE id = {_id}";
    try:
        cur = conn.cursor();
        cur.execute(sql);
        conn.commit();
        return True;
    except Error as e:
        print("Error at delete_task(): ",str(e));
        return False;
    finally:
        if conn:
            cur.close();
            conn.close();
    
def complete_task(_id,completed):
    conn = create_connection();
    sql = f""" UPDATE tasks SET completed = {completed}
            WHERE id = {_id} """;
    try:
        cur = conn.cursor();
        cur.execute(sql);
        conn.commit();
        return True;
    except Error as e:
        print("Error at complete_task(): ",str(e));
        return False;
    finally:
        if conn:
            cur.close();
            conn.close();