from modeltranslation.translator import translator, TranslationOptions
from . import models


class TourTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'excerpt',
        'description',
    )


class TourTagTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


class TourCategoryTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


class WeekDayTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


class FAQTranslationOptions(TranslationOptions):
    fields = (
        'question',
        'answer'
    )


translator.register(models.Tour, TourTranslationOptions)
translator.register(models.TourTag, TourTagTranslationOptions)
translator.register(models.TourCategory, TourCategoryTranslationOptions) # noqa
