import json
from setuptools import setup
from pathlib import Path

here = Path(__file__).parent
with open('package.json') as f:
    package = json.load(f)
long_description = (here / 'README.md').read_text()

package_name = package["name"].replace(" ", "_").replace("-", "_")

setup(
    name=package_name,
    version=package["version"],
    author=package['author'],
    author_email="vishal.biyani@biyani.xyz",
    packages=[package_name],
    include_package_data=True,
    license=package['license'],
    description=package.get('description', package_name),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://dash-copilotkit.biyani.xyz",
    project_urls={
        "Bug Reports": "https://github.com/dash-copilotkit/dash-copilotkit/issues",
        "Source": "https://github.com/dash-copilotkit/dash-copilotkit",
        "Documentation": "https://dash-copilotkit.biyani.xyz",
    },
    install_requires=[
        "dash>=2.0.0",
        "dash-bootstrap-components>=1.0.0",
    ],
    python_requires=">=3.7",
    keywords=["dash", "plotly", "react", "copilotkit", "ai", "chat", "assistant", "llm", "openai"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Framework :: Dash",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
