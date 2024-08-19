from distutils.core import setup
import setuptools

setup(
    name='phpipamapi',
    version='1.1.2',
    author="Christian Rahl",
    author_email="contact@christianrahl.com",
    description="phpIPAM API implementation",
    packages=['phpipamapi'],
    install_requires=[
        "requests>=2.25.1",
        "python-dateutil>=2.8.1"
    ],
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

