from distutils.core import setup

setup(
    name='ros',
    version='0.1',
    author='C Bates',
    author_email='chrsbats@gmail.com',
    packages=['ros'],
    scripts=[],
    url='https://github.com/chrsbats/ros',
    license='LICENSE.TXT',
    description='Regression on Order Statistics',
    long_description='Regression on Order Statistics for recovering a distribution on censored data.',
    install_requires=[
        "numpy>=1.9.0", "scipy>=0.14.0"
    ],
)
