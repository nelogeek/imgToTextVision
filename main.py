import pytesseract
from PIL import Image

# Название файла
# file = 'phone_num.png'
# file = 'eng_text.png'
# file = 'ru_text_2.png'
file = 'ru_text.png'

# Путь до файла
path = f"img/{file}"

# открыть картинку
img = Image.open(path)

# конфиг обработки
# custom_config = r'--oem 3 --psm 13' # конфиг для номера: oem-3 - английский язык, psm-13 - вывод необработанной строки
custom_config = r'--oem 3 --psm 6' # конфиг для текста: oem-3 - английский язык, psm-6 - вывод унифицированного блока текста (подойдет и для номера)

# метод преобразования из картинки в текст
text = pytesseract.image_to_string(img, lang='rus', config=custom_config) # lang='eng' или lang='rus'

# вывод текста в консоль
print(text)

# вывод текста в файл .txt
file_name = file.split('.')[0]
with open(f"txt/{file_name}.txt", "w") as text_file:
    text_file.write(text)

