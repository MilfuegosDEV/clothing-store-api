def checkRequiredFields(**kwargs) -> str | None:
    """Check required fields
    :param kwargs: Dictionary of required fields
    :return: Error message or None
    """
    missing_fields = [
        field.title().replace("_", " ")
        for field, value in kwargs.items()
        if value is None or value == ""
    ]

    if missing_fields:
        return f"Missing required fields: {', '.join(missing_fields)}"
    pass


def mustBeAlpha(**kwargs) -> str | None:
    """
    Check if all fields are alphabetic
    :param kwargs: Dictionary of fields
    :return: Error message or None
    """
    non_alpha_fields = [
        field.title().replace("_", " ")
        for field, value in kwargs.items()
        if not value.isalpha()
    ]

    if non_alpha_fields:
        return f"These must fields must be alphabetic: {', '.join(non_alpha_fields)}"
    pass


def mustBeBetween(value, field, min_len, max_len) -> str | None:
    """
    Check if value is between min_len and max_len
    :param value: Value to check
    :param field: Field name
    :param min_len: Minimum length
    :param max_len: Maximum length
    :return: Error message or None
    """
    if not (min_len <= len(value) <= max_len):
        return f"Invalid {field}: Must be between {min_len} and {max_len} characters"


def handleErrors(*args) -> list | None:
    """
    Handle errors
    :param args: List of errors
    :return: Dictionary of errors or None
    """
    errors = [arg for arg in args if not arg is None]
    if errors:
        return errors
    return None
