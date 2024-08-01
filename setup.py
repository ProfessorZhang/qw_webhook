# setup.py

from setuptools import setup, find_packages

setup(
    name='qw_webhook',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'qw_webhook=qw_webhook.webhook:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A script to send messages to WeChat Work via webhook',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/qw_webhook',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)