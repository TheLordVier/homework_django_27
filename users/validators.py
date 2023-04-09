import datetime
from rest_framework.exceptions import ValidationError


def check_birth_date(birth_date):
    """
    Валидатор проверки даты рождения пользователя
    """
    today = datetime.date.today()
    age = (today.year - birth_date.year - 1) + ((today.month, today.day) >= (birth_date.month, birth_date.day))
    if age < 9:
        raise ValidationError(f"Возраст должен быть больше 9-ти лет. Ваш возраста составляет {age}.")


def check_email(email):
    """
    Валидатор проверки почты пользователя
    """
    if "rambler.ru" in email:
        raise ValidationError("Регистрация с почтового адреса в домене rambler.ru запрещена.")
