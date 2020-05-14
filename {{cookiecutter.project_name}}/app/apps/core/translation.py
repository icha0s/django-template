from modeltranslation.translator import translator

from apps.core import models

translator.register(models.Tag, fields=["name"])
