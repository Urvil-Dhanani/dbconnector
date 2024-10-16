from setuptools import setup, find_packages

setup(
    name="dbconsmart",
    version="0.0.3",
    author="Urvil Dhanani",
    author_email="urvild@gmail.com",    
    description="A package to connect to different databases",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    entry_points={"console_scripts": ["cloudquicklabs1 = src.main:main"]},
)