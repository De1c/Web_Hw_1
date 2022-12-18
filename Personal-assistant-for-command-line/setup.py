from setuptools import setup, find_packages



setup(
    name="personal_helper",
    version="1",
    description="helper",
    url="https://github.com/ZatokaV/helper",
    author="GoIt Team Number 3",
    license="",
    packages=find_packages(),
    install_requires=["pyspellchecker"],
    entry_points={"console_scripts": ["helper = bot_cod.main:main"]},
)
