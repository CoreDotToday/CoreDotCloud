from setuptools import setup, find_packages

setup(
    name="coredotcloud",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["psutil", "requests"],
    entry_points={
        "console_scripts": [
            "coredotcloud=coredotcloud.main:main"
        ]
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple system monitoring tool for CoreDotCloud",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/coredotcloud",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
