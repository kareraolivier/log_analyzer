from reader import read_logs
from parser import parse_log
from processor import filter_errors, count_by_level, total_errors
from exceptions import InvalidLogFormatError


def main():
    parsed_logs = []

    for line in read_logs("sample.log"):
        try:
            log = parse_log(line)
            parsed_logs.append(log)
        except InvalidLogFormatError as e:
            print(f"Skipping invalid line: {e}")

    print("\n--- Error Logs ---")
    errors = list(filter_errors(parsed_logs))
    for e in errors:
        print(e)

    print("\n--- Count By Level ---")
    print(count_by_level(parsed_logs))

    print("\n--- Total Errors ---")
    print(total_errors(parsed_logs))


if __name__ == "__main__":
    main()