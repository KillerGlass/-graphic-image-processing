import setuptools


def parse_requirements_file(filename):
    with open(filename) as fid:
        requires = [l.strip() for l in fid.readlines() if l]

    return requires


INSTALL_REQUIRES = parse_requirements_file('requirements.txt')

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cambir",
    version="0.4.4.3",
    author="Romuere Silva, Flavio Araujo, Daniela Ushizima",
    author_email="romuere@ufpi.edu.br",
    description="Search for scientific images using deep learning with camBIR, the last packaging of pyCBIR.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xdatacnn/imagesearch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=INSTALL_REQUIRES,
    python_requires='>=3.6',
)
