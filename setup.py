import setuptools


def parse_requirements_file(filename):
    with open(filename) as fid:
        requires = [l.strip() for l in fid.readlines() if l]

    return requires


INSTALL_REQUIRES = parse_requirements_file('requirements.txt')

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Grafic Imagem Processig",
    version="1.0.0",
    author="Francisco Jose, Mateus Assis",
    author_email="franciscojose17@ufpi.edu.br",
    description="Gip is a library that aims to simplify the functionality of other existing libraries for image processing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KillerGlass/-graphic-image-processing.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=INSTALL_REQUIRES,
    python_requires='>=3.8',
)
