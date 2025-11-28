PLAIN = "plain"
JSON = "json"

SUPPORTED = [PLAIN, JSON]


def plain_text_upper_case(*texts):
    combined = " ".join(texts)
    return combined.upper()


def get_formatted(msg, name, output):
    output = output.lower()
    if output == JSON:
        return f'{{"imie":"{name}", "msg":"{msg}"}}'
    if output == PLAIN:
        return plain_text_upper_case(msg)
        raise ValueError(f"Unsupported output format: {output}")  # noqa