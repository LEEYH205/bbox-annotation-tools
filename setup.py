from setuptools import setup, find_packages
import os

# README 파일 읽기
def read_readme():
    if os.path.exists("README.md"):
        with open("README.md", "r", encoding="utf-8") as fh:
            return fh.read()
    return "Bounding Box Annotation Editing and Analysis Tools"

setup(
    name="bbox-annotation-tools",
    version="1.0.0",
    author="LEEYH205",
    author_email="ejrdkachry@gmail.com",
    description="Bounding Box Annotation Editing and Analysis Tools",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/LEEYH205/bbox-annotation-tools",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Processing",
    ],
    python_requires=">=3.7",
    install_requires=[
        "opencv-python>=4.5.0",
        "numpy>=1.19.0",
        "matplotlib>=3.3.0",
        "Pillow>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "bbox-editor=bbox_tools.bbox_gui_editor:main",
            "drug-viewer=bbox_tools.drug_code_viewer:main",
        ],
    },
    include_package_data=True,
    package_data={
        "bbox_tools": ["*.py"],
    },
    keywords="bbox annotation computer-vision image-processing drug-detection",
    project_urls={
        "Bug Reports": "https://github.com/LEEYH205/bbox-annotation-tools/issues",
        "Source": "https://github.com/LEEYH205/bbox-annotation-tools",
    },
) 