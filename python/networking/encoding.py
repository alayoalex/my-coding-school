input_bytes = b'\xff\xfe4\x001\x003\x00 \x00i\x00s\x00 \x00i\x00n\x00.\x00'
input_characters = input_bytes.decode('utf-16')
print(repr(input_characters))