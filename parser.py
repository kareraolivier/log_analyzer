from exceptions import InvalidLogFormatError


def parse_log(line):
    if ":" not in line:
        raise InvalidLogFormatError(f"Invalid format: {line}")

    level, message = line.split(":", 1)
    return {"level": level, "message": message}