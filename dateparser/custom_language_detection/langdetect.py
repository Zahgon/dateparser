import langdetect

# The below _Factory is set to prevent setting global state of the library
# but still get consistent results.
# Refer : https://github.com/Mimino666/langdetect


class _Factory:
    data = None


def _init_factory():
    pass


def _get_language_probablities(text):
    pass


def detect_languages(text, confidence_threshold):
    pass
