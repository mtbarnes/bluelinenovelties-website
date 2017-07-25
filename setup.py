from setuptools import setup

setup(
    name='blueapp',
    packages=['blueapp'],
    include_package_data=True,
    install_requires=[
        'flask',
        'nose',
        'wheel',
        'Flask-Navigation'
    ]
)
