# [보안취약성 2개]: 하드코딩된 비밀번호, eval 사용

def authenticate():
    username = input("Enter username: ")
    password = "supersecret123"  # [취약성1] 하드코딩된 비밀번호
    if username == "admin" and input("Enter password: ") == password:
        print("Access granted")
    else:
        print("Access denied")

def execute_user_code():
    user_input = input("Enter some Python code: ")
    eval(user_input)  # [취약성2] 사용자 입력 eval 실행 (RCE 위험)

authenticate()
execute_user_code()
