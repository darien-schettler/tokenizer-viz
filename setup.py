from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tokenizer-viz",
    version="0.1.0",
    author="Darien Schettler",
    author_email="ds08tf@gmail.com",
    description="A package to visualize tokenization of text using HTML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/tokenizer-visualizer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=[
        "matplotlib",
    ],
    python_requires='>=3.7',
)
