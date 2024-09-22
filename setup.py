from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_uiryan",
    version="0.0.1",
    author="I'm using this code as a trainee under Karine. Uiryan",
    description="image Processing Package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/uiryam/image-processing-package",
    packages=find_packages(),
)