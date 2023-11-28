import os
from collections.abc import Iterable


def error_log_generator(log_file_path) -> Iterable[str]:
    with open(log_file_path, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                yield line

with open('errors.txt', 'w') as error_file:
    for error in error_log_generator('logs.txt'):
        error_file.write(error)
