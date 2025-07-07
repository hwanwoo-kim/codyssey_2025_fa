import sqlite3
import os

# ���� ����� 1: �ϵ��ڵ��� ��й�ȣ
DB_PASSWORD = "supersecret"  # Noncompliant - �ϵ��ڵ��� ��й�ȣ

def connect_to_db():
    # ���� ����� 2: SQL ������ ���ɼ�
    username = input("Enter username: ")
    query = f"SELECT * FROM users WHERE username = '{username}'"  # Noncompliant

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE TABLE users (username TEXT)")
        cursor.execute("INSERT INTO users VALUES ('admin')")
        cursor.execute(query)  # ������ SQL ����
        for row in cursor.fetchall():
            print(row)
    finally:
        conn.close()


def buggy_function():
    # ���� 1: 0���� ������ ���ɼ�
    divisor = 0
    result = 10 / divisor  # Noncompliant

    # ���� 2: �� ���� (None Ÿ�� ����)
    value = None
    print(value.strip())  # Noncompliant

    # ���� 3: ���� �ݱ� ���� (�ڿ� ����)
    file = open("temp.txt", "w")
    file.write("Temporary data")  # Noncompliant - with���� ��� ��


def code_smell_example():
    # �ڵ� ���� 1: ���ʿ��� ���ǹ�
    if True:  # Noncompliant
        print("This block always runs.")


if __name__ == "__main__":
    connect_to_db()
    buggy_function()
    code_smell_example()