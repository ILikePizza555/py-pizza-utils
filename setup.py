from setuptools import setup, find_packages

setup(
    name="pizza-utils",
    version="0.0.1",
    url="https://github.com/ILikePizza555/py-pizza-utils",
    description="My personal python utilities",
    author="Isaac Avram",
    author_email="avrisaac555@gmail.com",
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=["tests"])
)