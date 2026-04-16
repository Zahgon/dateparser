from functools import wraps


def _restore_languages_on_generator_exit(method):
    @wraps(method)
    pass


class BaseLanguageDetector:
    def __init__(self, languages):
        self.languages = languages[:]

    @_restore_languages_on_generator_exit
    def iterate_applicable_languages(self, date_string, settings=None, modify=False):
        pass

    @staticmethod
    def _filter_languages(date_string, languages, settings=None):
        pass


class AutoDetectLanguage(BaseLanguageDetector):
    def __init__(self, languages, allow_redetection=False):
        super().__init__(languages=languages[:])
        self.language_pool = languages[:]
        self.allow_redetection = allow_redetection

    @_restore_languages_on_generator_exit
    def iterate_applicable_languages(self, date_string, modify=False, settings=None):
        pass


class ExactLanguages(BaseLanguageDetector):
    def __init__(self, languages):
        if languages is None:
            raise ValueError("language cannot be None for ExactLanguages")
        super().__init__(languages=languages)

    @_restore_languages_on_generator_exit
    def iterate_applicable_languages(self, date_string, modify=False, settings=None):
        pass
