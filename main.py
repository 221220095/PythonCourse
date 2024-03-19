# test.py

import module

char = 'A'
print(f"'{char}' bir harf mi? {module.is_character(char)}")

lowercase_char = module.convert_to_lowercase(char)
print(f"Küçük harfe çevrilmiş hali: {lowercase_char}")

text = "Hello World"
frequency = module.calculate_frequency(text)
print("Harf frekansları:")
for char, freq in frequency.items():
    print(f"'{char}': {freq:.2f}%")

module.show_info()
