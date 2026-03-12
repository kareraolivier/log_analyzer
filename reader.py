def read_logs(file_path):
    try:
        with open(file_path, "r") as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        raise FileNotFoundError("Log file not found")