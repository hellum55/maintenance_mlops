import os

# Define the project structure
project_structure = {
    ".github/workflows": ["main.yml"],
    "data_schema": ["schema.yaml"],
    "final_model": ["model.pkl", "preprocessor.pkl"],
    "Machine_Predictive_Data": ["predictive_maintenance.csv"],
    "machine_predictive_maintenance": [
        "cloud/",
        "components/",
        "constant/",
        "entity/",
        "exception/",
        "logging/",
        "pipeline/",
        "utils/",
        "__init__.py"
    ],
    "my_venv": [],
    "notebooks": ["EDA.ipynb", "prediction_output/"],
    "templates": ["table.html"],
    "valid_data": ["test.csv"],
}

root_files = [
    ".env",
    ".gitignore",
    "app.py",
    "Dockerfile",
    "main.py",
    "push_data.py",
    "README.md",
    "requirements.txt",
    "setup.py",
    "test_mongodb.py",
]

def create_project_structure(base_path="project_root"):
    for folder, files in project_structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            if file.endswith("/"):
                os.makedirs(os.path.join(folder_path, file), exist_ok=True)
            else:
                open(os.path.join(folder_path, file), 'a').close()

    # Create root-level files
    for file in root_files:
        open(os.path.join(base_path, file), 'a').close()

    print(f"✅ Project structure created under: {base_path}")

if __name__ == "__main__":
    create_project_structure()