# Consult your village people if you still mess this up
# install.py

import subprocess

def install_requirements(requirements_file):
    try:
        with open(requirements_file, 'r') as file:
            requirements = file.readlines()
            for requirement in requirements:
                requirement = requirement.strip()
                subprocess.check_call(["pip", "install", "--upgrade", requirement])
        print("All requirements installed and upgraded successfully.")
    except Exception as e:
        print(f"Error installing or upgrading requirements: {e}")

if __name__ == "__main__":
    requirements_file = "requirements.txt"
    install_requirements(requirements_file)