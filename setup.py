from setuptools import setup

with open("requirements.txt") as requirements_file:
    requirements = [line for line in requirements_file]

with open("readme.rst", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="picassosr",
    version="0.4.5",
    author="Joerg Schnitzbauer, Maximilian T. Strauss",
    author_email=("joschnitzbauer@gmail.com, straussmaximilian@gmail.com"),
    url="https://github.com/jungmannlab/picasso",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=["picasso", "picasso.gui", "picasso.server"],
    entry_points={
        "console_scripts": ["picasso=picasso.__main__:main"],
    },
    install_requires=requirements + ["PyImarisWriter==0.7.0; sys_platform=='win32'"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        "picasso": [
            "gui/icons/*.ico",
            "gui/icons/*.png",
            "config_template.yaml",
        ]
    },
)
