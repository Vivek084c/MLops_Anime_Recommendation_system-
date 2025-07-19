from setuptools import setup, find_packages

with open("requirements.txt") as f:
    req = f.read().splitlines()


setup(
    name = "MLOPS-ANIME-RECOMENDATION-1",
    version = "0.1",
    author = "Vviek",
    packages = find_packages(),
    install_requires = req
)
