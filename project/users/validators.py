from django.core.exceptions import ValidationError
import re

def validate_phone(val):
    # Валидатка для любого формата ввода

    # Удаляем все символы, кроме цифр
    val = re.sub(r'\D', '', val)
    
    # Проверяем, что номер содержит 10 цифр
    if len(val) != 10:
        return False
    
    # Проверяем, что номер начинается с 7 или 8
    if not re.match(r'[78]', val[0]):
        return False
    
    # Если все проверки прошли успешно, то номер валидный
    return True