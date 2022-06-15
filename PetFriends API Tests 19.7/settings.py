# Валидные данные для авторизации
valid_email = 'kristia_k@bk.ru'
valid_password = '123456'

# Не валидные данные для авторизации
invalid_email = 'kristia_k@bk.ru'
invalid_password = '654321'
invalid_auth_key = {
  "key": "ea738148a1f19838e1c5d1413877f3691a3731380e733e877b0ae729"
}
rotten_auth_key = {
  "key": "ea738148a1f19838e1c5d1413877f3691a3731380e733e877b0ae72"
}
# Данные для создания нового питомца
add_name = 'Булочка'
add_age = '2'
add_animal_type = 'корги'
add_pet_photo = 'images/dog_1.jpg'

# Данные для обновления информации о питомце
update_name = 'Батон'
update_age = '3'
update_animal_type = 'корги'
update_pet_photo = 'images/dog_2.jpeg'

def generate_string(num):
    return "x" * num


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

