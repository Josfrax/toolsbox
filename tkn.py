from secrets import token_hex

def generate():
    token = token_hex(16)
    return token

