from setuptools import setup, find_packages

tests_require = [
    'nose'
    ]

setup(
    name='wikiphilosophy',
    version='1.0.0',
    description='Play the Wikipedia philosophy game',
    author='Daniel Shen',
    author_email='dshen109@gmail.com',
    packages=find_packages(exclude=['test', 'test_*', 'fixtures']),
    install_requires=[
        'bs4',
        ],
    test_suite='nose.collector',
    tests_require=tests_require,
    extras_require={'test': tests_require},
    entry_points={}
)
