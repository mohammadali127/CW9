import re
def pass_val(password):
    return re.fullmatch(r'(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])[A-Za-z\d]{8,}', password)