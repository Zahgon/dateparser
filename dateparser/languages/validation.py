import regex as re

from dateparser.utils import get_logger


class LanguageValidator:
    logger = None

    VALID_KEYS = [
        "name",
        "skip",
        "pertain",
        "simplifications",
        "no_word_spacing",
        "ago",
        "in",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
        "year",
        "month",
        "week",
        "day",
        "hour",
        "minute",
        "second",
        "sentence_splitter_group",
    ]

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger = get_logger()
        return cls.logger

    @classmethod
    def validate_info(cls, language_id, info):
        pass

    @classmethod
    def _validate_type(cls, language_id, info):
        pass

    @classmethod
    def _validate_name(cls, language_id, info):
        pass

    @classmethod
    def _validate_word_spacing(cls, language_id, info):
        pass

    @classmethod
    def _validate_sentence_splitter_group(cls, language_id, info):
        pass

    @classmethod
    def _validate_skip_list(cls, language_id, info):
        pass

    @classmethod
    def _validate_pertain_list(cls, language_id, info):
        pass

    @classmethod
    def _validate_weekdays(cls, language_id, info):
        pass

    @classmethod
    def _validate_months(cls, language_id, info):
        pass

    @classmethod
    def _validate_units(cls, language_id, info):
        pass

    @classmethod
    def _validate_other_words(cls, language_id, info):
        pass

    @classmethod
    def _validate_simplifications(cls, language_id, info):
        pass

    @classmethod
    def _validate_extra_keys(cls, language_id, info):
        pass
