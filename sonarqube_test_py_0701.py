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



# [버그 2개]: Division by zero 가능성, 잘못된 리스트 인덱스 사용

def divide(a, b):
    return a / b  # [버그1] b가 0일 때 ZeroDivisionError

def get_item(lst, index):
    return lst[index + 1]  # [버그2] 범위를 벗어난 인덱스 접근 가능성

divide(10, 0)
get_item([1, 2, 3], 2)




# [코드 스멜 2개]: 중복된 조건문, 의미 없는 변수명 사용

def process(data):
    if data == "yes":
        print("You said yes")
    elif data == "yes":  # [스멜1] 중복된 조건
        print("Still yes")

def calc():
    x = 1
    y = 2
    z = x + y  # [스멜2] 의미 없는 변수명 사용
    print(z)

process("yes")
calc()

