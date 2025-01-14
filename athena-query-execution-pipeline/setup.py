import setuptools

with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="ddk-constructs",
    version="0.6.1",
    description="An empty DDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="author",
    package_dir={"": "ddk-constructs"},
    packages=setuptools.find_packages(where="ddk-constructs"),
    install_requires=open("requirements.txt").read().strip().split("\n"),
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
