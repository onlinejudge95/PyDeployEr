import pathlib
import setuptools


BASE_DIR = pathlib.Path.cwd()
README_PATH = BASE_DIR / "README.md"

setuptools.setup(
    name="deploymaadi",
    version="0.1.0",
    description="Module for automated deployments",
    long_description=README_PATH.read_text(),
    long_description_content_type="text/markdown",
    author="onlinejudge95",
    author_email="onlinejudge95@gmail.com",
    maintainer="onlinejudge95",
    maintainer_email="onlinejudge95@gmail.com",
    download_url="http://github.com/onlinejudge95/pydeployer",
    url="http://github.com/onlinejudge95/pydeployer",
    packages=setuptools.find_packages(exclude=("tests",)),
    license="MIT",
    classifiers=[
        "Topic :: Artistic Software",
        "Topic :: Other/Nonlisted Topic",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Installation/Setup",
        "Topic :: Utilities",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
    ],
    include_package_data=True,
    install_requires=["click", "paramiko"],
    zip_safe=False,
    entry_points={"console_scripts": ["deploymaadi=deploymaadi.__main__:main"]},
)
