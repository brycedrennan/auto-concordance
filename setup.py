import subprocess
from functools import lru_cache

from setuptools import find_packages, setup


@lru_cache
def get_git_revision_hash() -> str:
    try:
        return (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode("ascii")
            .strip()
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return "no-git"


revision_hash = get_git_revision_hash()

with open("README.md", encoding="utf-8") as f:
    readme = f.read()
    readme = readme.replace(
        '<img src="',
        f'<img src="https://raw.githubusercontent.com/brycedrennan/auto-concordance/{revision_hash}/',
    )

setup(
    name="Auto-Concordance",
    author="Bryce Drennan",
    version="0.0.1",
    description="Automatically generate a concordance for a set of books. Uses text embeddings to find relationships between texts.",
    long_description=readme,
    long_description_content_type="text/markdown",
    project_urls={
        "Documentation": "https://github.com/brycedrennan/auto-concordance",
        "Source": "https://github.com/brycedrennan/auto-concordance",
    },
    packages=find_packages(include=("auto_concordance", "auto_concordance.*")),
    scripts=[],
    entry_points={},
    package_data={"auto_concordance": []},
    install_requires=[
        "numpy",
        "tensorflow",
    ],
    # don't specify maximum python versions as it can cause very long dependency resolution issues as the resolver
    # goes back to older versions of packages that didn't specify a maximum
    # https://discuss.python.org/t/requires-python-upper-limits/12663/75
    python_requires=">=3.8",
)
