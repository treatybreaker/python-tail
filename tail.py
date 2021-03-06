import os
import time


def tail(file_path, poll_rate: float = 1, start_position: int = 2) -> str:
    """
    Implements tail -F in python with log rotation handling.

    Log rotation is handled by comparing the size of the file to the last known size, if the current size
    is less than the last known size it's likely the file was rotated so it begins to read from the start of the file
    to handle the rotation.

    Example:
        Tail is a generator so it must be iterated over to the get the output from whatever file that is being read::

            for line in tail('somelog.log'):
                print(line)

    Args:
        file_path (str): The path to the file, absolute or relative, (inclusive) to read from
        poll_rate (float): How often the file should be checked for new data (default is 1)
        start_position (int): Where to start the file with os.seek(0, start_position), 0 would be from the start of
            the file and 2 would be a normal tail (default is 2)
    Yields:
        str: A single string representing any new data per line. If a previously read line has data appended to it, e.g.
            "hello" is a line and on the same line " world" is added making the line "hello world" as a whole then
            only the new data on that line " world" will be returned.
    """
    path = os.path.abspath(file_path)
    with open(path, 'r', encoding='utf-8') as file:
        file_size = 0
        file.seek(0, start_position)
        while True:
            location = file.tell()
            line = file.readline()
            current_file_size = os.stat(path).st_size
            if file_size > current_file_size:
                file.seek(0)
                file_size = current_file_size
                continue
            file_size = current_file_size
            if not line:
                time.sleep(poll_rate)
                file.seek(location)
                continue
            yield line
