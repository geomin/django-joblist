from setuptools import setup, find_packages

setup(
    name='joblist',
    version='1.0',
    url='http://github.com/geomin/django-joblist',
    maintainer='Georg Kasmin',
    maintainer_email='georg@aquarianhouse.com',
    description='A full collection of jobs',
    classifiers=['License :: OSI Approved :: BSD License',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python',
                 'Topic :: Global :: Countries'],
    license='BSD',
    platforms=['any'],
    install_requires=[],#pip
    packages=find_packages(),
)
