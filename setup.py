import re
from sys import argv

from setuptools import setup, find_packages

from compiler.api import compiler as api_compiler
from compiler.errors import compiler as errors_compiler

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

with open("pyrogram/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

if len(argv) > 1 and argv[1] in ["bdist_wheel", "install", "develop"]:
    api_compiler.start()
    errors_compiler.start()

setup(
    name="monkeygram",  # Изменено для избежания конфликтов с оригиналом
    version=version,
    description="Monkeygram - Custom Pyrogram fork with additional features",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/deadboizxc/pyrogram",
    download_url="https://github.com/deadboizxc/pyrogram/releases/latest",
    author="deadboizxc",  # Измени на свое имя
    author_email="deadboi.zxc@gmail.com",  # Измени на свой email
    license="LGPLv3",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks"
    ],
    keywords="telegram chat messenger mtproto api client library python monkeygram",
    project_urls={
        "Tracker": "https://github.com/deadboizxc/pyrogram/issues",
        "Community": "https://t.me/monkeygram_cht",
        "Source": "https://github.com/deadboizxc/pyrogram",
        "Documentation": "https://deadboizxc.org/monkeygram",
    },
    python_requires="~=3.8",
    package_data={
        "pyrogram": ["py.typed"],
    },
    packages=find_packages(exclude=["compiler*", "tests*"]),
    zip_safe=False,
    install_requires=requires,
    # Добавлены следующие параметры для обеспечения совместимости
    provides=["pyrogram"],
    package_dir={"pyrogram": "pyrogram"},
)