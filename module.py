# module.py dosyası

# Verilen karakterin bir harf olup olmadığını kontrol eden fonksiyon.
def is_character(char):
    if char.isalpha():
        return True
    else:
        return False

def convert_to_lowercase(char):
    """
    Verilen harfi küçük harfe çeviren fonksiyon.
    """
    return char.lower()

# Verilen metinde harflerin kullanım sıklığını yüzdelik oranını bulan fonksiyon. Boşluklar atlanıyor.
def calculate_frequency(text):
    text = ''.join(char for char in text if char.isalpha() and not char.isspace())
    text = text.lower()
    frequency = {}
    total_chars = len(text)

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    for char, count in frequency.items():
        frequency[char] = (count / total_chars) * 100

    return frequency

#Yazar bilgisini ve notu ekrana yazdıran fonksiyon.
def show_info():
    author_name = "Hasan Kaan"
    author_surname = "Kahraman"
    student_number = "221220095"
    note = "Eğer bir gün benim sözlerim bilimle ters düşerse bilimi seçin. -Atatürk"
    print(f"Yazar: {author_name} {author_surname}")
    print(f"Öğrenci Numarası: {student_number}")
    print(f"Not: {note}")
