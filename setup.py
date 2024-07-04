import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.1.0"

REPO_NAME = "House-Price-Prediction"
AUTHOR_USERNAME = "GautamaShastry"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "gautamashastry@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="a small ml project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
        "Documentation": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/wiki",
        "Source Code": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)