import os
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
    


