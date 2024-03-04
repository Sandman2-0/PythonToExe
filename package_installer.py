import os

def install_packages(packages):
    for package in packages:
        os.system(f"pip install {package}")

if __name__ == "__main__":
    packages_to_install = ["tk", "pyinstaller"]
    install_packages(packages_to_install)
    os.system("pause")