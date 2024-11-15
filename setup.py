from setuptools import setup, find_packages

setup(
    name="nerveboard",
    version="0.1.0",
    author="Tatum Deadon",
    description="Developer productivity dashboard and team analytics",
    packages=find_packages(),
    python_requires=">=3.9",
    extras_require={"dev": ["pytest>=7.0"]},
    entry_points={"console_scripts": ["nerveboard=nerveboard.__main__:main"]},
)
