import os
import shutil
import time
from mcp.server.fastmcp import FastMCP

mcp=FastMCP("FileFlow")

@mcp.tool()
def create_file(path: str, filename: str) -> str:
    """
    Creates a new file at the specified directory path.

    This function checks if the given filename already exists in the directory 
    or is a substring of any existing file name. If not, it creates an empty file 
    with the given name at the specified path.

    Parameters:
        path (str): The directory where the file should be created.
        filename (str): The name of the file to be created.

    Returns:
        str: A message indicating whether the file was created successfully, 
             already exists (or is similar), or if the path is invalid.
    """

    if not os.path.exists(path):
        return "Path does not exist"

    for existing_file in os.listdir(path):
        if filename == existing_file or filename in existing_file:
            return "File already exists or is similar to an existing file"

    full_path = os.path.join(path, filename)
    try:
        with open(full_path, 'w') as f:
            pass
        return "File successfully created "
    except Exception as e:
        return f"Failed to create file: {e}"
    
@mcp.tool()
def write_file(path: str, filename: str, content: str) -> str:
    """
    Writes content to a specified file if it exists in the given directory.

    Parameters:
        path (str): The directory containing the file.
        filename (str): The name of the file to write to.
        content (str): The content to be written into the file.

    Returns:
        str: A message indicating the result of the write operation.
    """
    if not os.path.isdir(path):
        return "Path does not exist"

    full_path = os.path.join(path, filename)

    if not os.path.isfile(full_path):
        return "File does not exist"

    try:
        with open(full_path, 'w') as file:
            file.write(content)
        return "Successfully wrote to file"
    except Exception as e:
        return f"Failed to write to file: {e}"

@mcp.tool()
def delete_file(path: str, filename: str) -> str:
    """
    Deletes the specified file from the given directory.

    Parameters:
        path (str): The directory containing the file.
        filename (str): The name of the file to be deleted.

    Returns:
        str: A message indicating the result of the delete operation.
    """
    if not os.path.isdir(path):
        return "Path does not exist"

    full_path = os.path.join(path, filename)

    if not os.path.isfile(full_path):
        return "File does not exist"

    try:
        os.remove(full_path)
        return "File deleted successfully"
    except Exception as e:
        return f"Failed to delete file: {e}"

@mcp.tool()
def create_dir(path: str, name: str) -> str:
    """
    Creates a new directory with the specified name at the given path.

    Parameters:
        path (str): The base directory where the new folder should be created.
        name (str): The name of the folder to create.

    Returns:
        str: A message indicating the result of the directory creation operation.
    """
    
    if not os.path.isdir(path):
        return f"Invalid path: {path}"

    full_path = os.path.join(path, name)
    
    if os.path.exists(full_path):
        return f"Directory already exists at: {full_path}"

    try:
        os.makedirs(full_path)
        return f"Directory created successfully at: {full_path}"
    except OSError as e:
        return f"Error creating directory: {e}"
    
@mcp.tool()
def delete_dir(path: str, name: str) -> str:
    """
    Deletes a directory with the specified name from the given path.

    Parameters:
        path (str): The base directory where the target folder is located.
        name (str): The name of the directory to be deleted.

    Returns:
        str: A message indicating the result of the delete operation.
    """
    if not os.path.isdir(path):
        return f"Invalid base path: {path}"

    target_dir = os.path.join(path, name)

    if not os.path.exists(target_dir):
        return f"Directory '{name}' does not exist at: {path}"

    try:
        shutil.rmtree(target_dir)
        return f"Directory deleted successfully at: {target_dir}"
    except PermissionError:
        return f"Permission denied while deleting: {target_dir}"
    except OSError as e:
        return f"Error deleting directory: {e}"

@mcp.tool()
def search_file(path: str, name: str) -> str:
    """
    Searches for a file by name within the given directory and its subdirectories.

    Parameters:
        path (str): The base directory to start the search from.
        name (str): The name of the file to search for.

    Returns:
        str: The full path to the file if found, otherwise a message indicating it wasn't found.
    """
    if not os.path.isdir(path):
        return f"Invalid directory path: {path}"

    for root, dir, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

    return f"File '{name}' not found in: {path}"

@mcp.tool()

def meta_data(path:str,name:str)->str:

    """
    Retrieves metadata for a specified file within a given directory.

    Parameters:
        path (str): The directory path where the file is expected to be located.
        name (str): The name of the file for which metadata is to be retrieved.

    Returns:
        str: A formatted string containing metadata about the file such as its full path,
             size, creation date, last modification date, and last accessed date.
             Returns an error message if the path is invalid or the file doesn't exist.
    """

    if not os.path.isdir(path):
        return f"Invalid directory path: {path}"

    full_path=os.path.join(path,name)
    
    if not os.path.exists(full_path):
        return f"File does not exist: {name}"

    stats = os.stat(full_path)
    file_ext = os.path.splitext(name)[1]
    file_name = os.path.splitext(name)[0]

    result = (
        f"Full Path     : {full_path}\n"
        f"File Name     : {file_name}\n"
        f"Extension     : {file_ext}\n"
        f"Size          : {stats.st_size} bytes\n"
        f"Created       : {time.ctime(stats.st_ctime)}\n"
        f"Last Modified : {time.ctime(stats.st_mtime)}\n"
        f"Last Accessed : {time.ctime(stats.st_atime)}"
    )

    return result



    


