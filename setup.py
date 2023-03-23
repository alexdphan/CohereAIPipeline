from setuptools import setup, find_packages

setup(
    name="cohereguard",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "nltk",
        "cohere",
        "autocorrect",
        "pydantic",
        "uvicorn",
        "spacy",
        "pandas",
        "numpy",
        "scikit-learn",
        "scipy",
        "python-dotenv",
        "python-multipart",
        "requests",
        "tqdm",
        "pydantic",
        "pytest",
        "guardrails-ai",
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
