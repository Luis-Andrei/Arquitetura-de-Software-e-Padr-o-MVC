from setuptools import setup, find_packages

setup(
    name="sistema-bancario",
    version="0.1.0",
    description="Um sistema bancário simples implementado em Python",
    author="Seu Nome",
    author_email="seu.email@example.com",
    packages=find_packages(),
    install_requires=[
        "pytest==7.4.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
) 