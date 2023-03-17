from setuptools import setup, find_packages

setup(
    name="cohere-ai-pipeline",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "nltk",
        "cohere",
        "autocorrect",
        "pydantic",
        # ... any other required libraries
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
