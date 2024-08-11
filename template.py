import os

project_name = "scraper"  # Replace with your desired project name

# Define the subfolders and their corresponding .py files
subfolders_and_files = {
    "data_access": ["data_access.py"],
    "entity": ["entity.py"],
    "exception": ["exception.py"],
    "logging": ["logging.py"],
    "logic": ["business_logic.py"],
    "tests": ["tests.py"],
    "utils": ["__init__.py"],  # Include __init__.py for utils
}

# Create the main project directory
os.makedirs(project_name, exist_ok=True)  # Creates directory if it doesn't exist

# Create all subfolders and .py files
for folder, files in subfolders_and_files.items():
    folder_path = os.path.join(project_name, folder)
    os.makedirs(folder_path, exist_ok=True)
    for file in files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, "w") as f:
            pass  # Create empty .py file

print(f"Project folder structure created for: {project_name}")
