from setuptools import find_packages, setup

setup(
    name='django-politico-oembed-service',
    version='0.0.4',
    description='',
    url='https://github.com/The-Politico/django-politico-oembed-service',
    author='POLITICO interactive news',
    author_email='interactives@politico.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests', 'example']),
    include_package_data=True,
    install_requires=[
        'djangorestframework',
        'requests',
    ],
    extras_require={
        'test': ['crayons'],
    },
)
