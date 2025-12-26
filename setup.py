from setuptools import setup, find_packages

setup(
    name="app-data", 
    version="0.1.0",
    packages=find_packages(), 
    install_requires=[
        "customtkinter",
        "ttkbootstrap",
        "ctkdlib",
        "CTkMessagebox",
        "CTkTable",
        "ctktablerowselector",
        "matplotlib",
        "mysql-connector-python",
        "seaborn",
        "yfinance",
<<<<<<< HEAD
=======
        "threading",
        "numpy"
>>>>>>> 1fcd123 (edit graph)


    ],
    entry_points={
        "console_scripts": [
            "app_data_run = App_Data.call_app_data:main", 
        ],
    },
    include_package_data=True,
    description="GUI using Customtkinter, API yfinance",
    author="Marcela_AC",
)
