# coding=utf-8
from setuptools import setup, find_packages

filepath = 'README.md'

setup(
    name='py-log',
    version="2.5",
    description=(
        'a simple logging tool(support file,email,dingtalk) ,Multithreading and Multi process safe'
    ),
    keywords=("logging", "logger", "multiprocess file handler", "color handler"),
    long_description_content_type="text/markdown",
    long_description=open(filepath, 'r', encoding='utf8').read(),
    author='bfzs',
    author_email='ydf0509@sohu.com',
    maintainer='abo123456',
    maintainer_email='abcdef123456chen@sohu.com',
    license='BSD License',
    packages=find_packages(),
    include_package_data=True,
    platforms=["all"],
    url='https://github.com/abo123456789/py-log',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'pymongo==3.5.1',
        'tomorrow3==1.1.0',
        'concurrent-log-handler==0.9.9',
        'elasticsearch',
        'kafka-python==1.4.6',
        'requests',
        'pika',
    ]
)
