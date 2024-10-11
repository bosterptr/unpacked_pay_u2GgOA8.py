import base64
import zlib
_ = lambda __: zlib.decompress(base64.b64decode(__[::-1]))

def trim_string(input_str):
    return input_str[13:-3]

def execute_nested_base64(encoded_str):
    decoded_str = encoded_str
    while True:
        try:
            not_trimmed_decoded_str = eval(f'print((_)("{decoded_str.decode()}"))')
            decoded_str = trim_string(not_trimmed_decoded_str)
            print(decoded_str)
        except Exception as e:
            print(f"end: {e}")
            break

base64_string = b'BASE64_HERE'
execute_nested_base64(base64_string)
