from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='InputPowertools',
    version='1.0.2',
    description='Kind of like a non intrusive addon for the standard input()',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MAA28/InputPowertools',
    author='MAA28',
    author_email='malteaschenbach@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: User Interfaces',
        'Environment :: Console',

        'License :: OSI Approved :: MIT License',
        'Intended Audience :: System Administrators',

        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords='cli, command line',
    package_dir={'': 'src'},
    requires=[
        "colorama~=0.4.4",
        "typical==2.8.0",
        "setuptools==60.10.0"
        "wheel",
        "docstring_parser",
        "typing"
    ],
    install_requires=[
        "setuptools>=42",
        "wheel",
        "colorama",
        "docstring_parser",
        "typing"
    ],
    python_requires='>=3.6, <4',
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/MAA28/InputPowertools/issues',
        'Source': 'https://github.com/MAA28/InputPowertools/'
    },
)
