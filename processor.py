from functools import reduce


def filter_errors(logs):
    return filter(lambda log: log["level"] == "ERROR", logs)


def count_by_level(logs):
    levels = [log["level"] for log in logs]  # list comprehension

    return {
        level: levels.count(level)
        for level in set(levels)  # dictionary comprehension
    }


def total_errors(logs):
    return reduce(lambda acc, log: acc + (1 if log["level"] == "ERROR" else 0), logs, 0)