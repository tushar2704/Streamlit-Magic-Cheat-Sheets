import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "1.0.0"

REPO_NAME = "Streamlit_Magic_Cheat_Sheets"
AUTHOR_USER_NAME = "tushar2704"
SRC_REPO = "Streamlit-Magic-Cheat-Sheet"
AUTHOR_EMAIL = "tushar.27041994@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Streamlit_Magic_Cheat_Sheets - ST App",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
