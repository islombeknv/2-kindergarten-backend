from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


def clean_picture(image):
    w, h = get_image_dimensions(image)
    if w != 720:
        raise ValidationError("Bu rasmni uzunligi %i piksel. Rasmni uzunligi 720px bo'lishi kerak.(720x480)" % w)
    if h != 480:
        raise ValidationError("Bu rasmni bo\'yi %i piksel rasmni bo'yi 480px bo'lishi kerak.(720x480)" % h)


def news_picture(image):
    w, h = get_image_dimensions(image)
    if w != 720:
        raise ValidationError("Bu rasmni uzunligi %i piksel. Rasmni uzunligi 720px bo'lishi kerak.(720x480)" % w)
    if h != 480:
        raise ValidationError("Bu rasmni bo\'yi %i piksel rasmni bo'yi 480px bo'lishi kerak.(720x480)" % h)


def staff_picture(image):
    w, h = get_image_dimensions(image)
    if w != 400:
        raise ValidationError("Bu rasmni uzunligi %i piksel. Rasmni uzunligi 400px bo'lishi kerak.(400x300)" % w)
    if h != 300:
        raise ValidationError("Bu rasmni bo\'yi %i piksel rasmni bo'yi 300px bo'lishi kerak.(400x300)" % h)
