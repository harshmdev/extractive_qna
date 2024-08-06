import setuptools

with open("Readme.md","r",encoding="utf-8") as f:
    long_description=f.read()

__version__="0.0.1"

REPO_NAME = "Extractive Question Answering"
AUTHOR_USER_NAME= "harshmdev"
SRC_REPO= "extractive_qna"
AUTHOR_EMAIL= "hmohandev@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for NLP app",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)