from setuptools import setup, find_packages

setup(
    name="cortexflow",
    version="0.1.0",
    description="Integrated cognitive agent system combining hierarchical management, memory systems, and cognitive processing",
    author="DefRecord Team",
    author_email="info@defrecord.com",
    url="https://github.com/defrecord/cortexflow",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "torch",
        "transformers",
        "pydantic",
        "fastapi",
        "uvicorn",
        "python-dotenv",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "black",
            "isort",
            "mypy",
            "flake8",
        ],
    },
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