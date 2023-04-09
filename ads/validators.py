from rest_framework.exceptions import ValidationError


def ad_not_published(value):
    """
    Валидатор проверки опубликованности объявления
    """
    if value:
        raise ValidationError("Нельзя создать опубликованное объявление.")
