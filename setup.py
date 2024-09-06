from setuptools import setup

with open("README.md", "r", encoding= "utf-8") as f :
    long_description = f.read()


## edit below variables as per your requirements -
REPO_NAME = "DVC_DL_TENSORFLOW_DEMO"
AUTHOR_USER_NAME = "jotiroy01"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="JotiRoy01",
    description="A small package for DVC-TENSORFLOW",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/JotiRoy01/DVC_DL-TENSORFLOW_DEMO.git",
    author_email="jotiroygit@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.10",
    install_requires=[
        "dvc",
        "tensorflow",
        "matplotlib",
        "numpy", 
        "pandas",
        "tqdm",
        "PyYAML",
        "boto3"
    ]
)