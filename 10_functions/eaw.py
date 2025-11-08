import os

def create_py_files(base_name="string", count=10, path="."):
    """
    Create empty Python files like string_01.py, string_02.py... in the given path.

    :param base_name: Base file name
    :param count: Number of files to create
    :param path: Directory where files will be created (default: current directory)
    """
    for i in range(1, count + 1):
        file_name = f"{base_name}_{i:02d}.py"  # Adds leading 0 (01, 02...)
        file_path = os.path.join(path, file_name)

        try:
            with open(file_path, "w") as f:   # "w" = create empty file
                pass
            print(f"Created: {file_path}")
        except Exception as e:
            print(f"Error creating {file_path}: {e}")


if __name__ == "__main__":
    create_py_files(base_name="Functions", count=15, path=".")
