from setuptools import setup, find_packages

setup(
    name="image_effects_library",
    version="0.1",
    packages=find_packages(),
    install_requires=["Pillow"],
    include_package_data=True,
    description="A Python library to add blur and grayscale effects to images.",
    author="Aneesh-G7",
    author_email="gsaneesh65gmail.com",
    url="https://github.com/Aneesh-G7/image_effect_library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
