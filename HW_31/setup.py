from setuptools import setup, find_packages
setup(
    name="first_project",
    version="0.1",
    url="https://github.com/isamarskiy/otus_qa_course",
    author="Ivan",
    author_email="samarskyii@gmail.com",
    description="HW otus-qa-course",
    packages=find_packages(exclude=['otus-qa-course']),
    install_requires=['pytest>=4.6.4']
)
