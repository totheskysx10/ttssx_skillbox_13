import os
import linecache

def count_lines_in_python_files(directory='.'):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                line_count = sum(1 for line in linecache.getlines(file_path) if line.strip() and not line.strip().startswith('#'))
                yield f"{line_count}"


for result in count_lines_in_python_files():
    print(result)
