from setuptools import setup, find_packages

setup(
    version='0.1',
    name='class_social',
    author='DCI Python 2022 Class',
    author_email='franz.bandelin@dci.education',
    description='Class Social is a social network for students',
    url='https://github.com/dci-python-backend-assignments/tdd-class-social',
    license='MIT',
    keywords=['social networks', 'education'],
    requires=[
        'fastapi',
        'uvicorn'
    ],
    test_suite='pytest',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['class-social=class_social.main:main']
    }
)
