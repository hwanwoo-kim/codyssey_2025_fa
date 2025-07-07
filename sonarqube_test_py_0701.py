import sqlite3
import os

# 보안 취약점 1: 하드코딩된 비밀번호
DB_PASSWORD = "supersecret"  # Noncompliant - 하드코딩된 비밀번호

def connect_to_db():
    # 보안 취약점 2: SQL 인젝션 가능성
    username = input("Enter username: ")
    query = f"SELECT * FROM users WHERE username = '{username}'"  # Noncompliant

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE TABLE users (username TEXT)")
        cursor.execute("INSERT INTO users VALUES ('admin')")
        cursor.execute(query)  # 위험한 SQL 실행
        for row in cursor.fetchall():
            print(row)
    finally:
        conn.close()


def buggy_function():
    # 버그 1: 0으로 나누기 가능성
    divisor = 0
    result = 10 / divisor  # Noncompliant

    # 버그 2: 널 참조 (None 타입 접근)
    value = None
    print(value.strip())  # Noncompliant

    # 버그 3: 파일 닫기 누락 (자원 누수)
    file = open("temp.txt", "w")
    file.write("Temporary data")  # Noncompliant - with문을 써야 함


def code_smell_example():
    # 코드 스멜 1: 불필요한 조건문
    if True:  # Noncompliant
        print("This block always runs.")


if __name__ == "__main__":
    connect_to_db()
    buggy_function()
    code_smell_example()