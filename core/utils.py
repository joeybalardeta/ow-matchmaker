import os, sys

# directory/folder utils
def remove_one_level(relative_path: str) -> str:
    """
    Removes one level from a relative path (e.g. "a/b/c" -> "a/b").

    Args:
        relative_path (str): The relative path to remove one level from.

    Returns:
        str: The relative path with one level removed.
    """
    return os.path.dirname(relative_path)


def get_project_root_dir() -> str:
    """
    Returns the root directory of the project.

    Returns:
        str: The root directory of the project.
    """
    abspath = os.path.abspath(sys.argv[0]).replace("\\", "/")  # Get the absolute path of the script and replace backslashes with forward slashes
    return remove_one_level(abspath)


def read_first_line(relative_file_path) -> str:
    """
    Reads the first line from a text file and returns it as a string.

    Args:
        relative_file_path (str): The relative path to the file to be read (from root directory of project).

    Returns:
        str: The content of the first line (stripped of leading/trailing whitespace).
            If the file is not found, returns None.
    """
    file_path = get_project_root_dir() + "/" + relative_file_path
    try:
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()  # Read the first line and remove any leading/trailing whitespace
            return first_line
        
    except FileNotFoundError:
        return None