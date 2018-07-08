password = 'xxxyyyZZZ220'
test_password(password)

def test_password(password):
    lowercase = [l for l in password if l.islower() == True]
    uppercase = [l for l in password if l.isupper() == True]
    digits =    [l for l in password if l.isnumeric() == True]
    ten_plus =  len(password) >= 10
    ascii_only  = len(password) == len(password.encode())
    return True if lowercase and uppercase and digits and ascii_only and ten_plus else False

def test_password(pw: str) -> bool:
    #replace this for solution
    return any(i.isdigit() for i in pw) and any(i.isupper() for i in pw) and any(i.islower() for i in pw) and len(pw) >= 10 if pw else False
#Some hints
#Just check all conditions
