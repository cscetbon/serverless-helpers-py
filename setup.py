from setuptools import setup

def read_requirements(path):
    requirements = []
    validate = lambda req: req and not req.startswith('-')
    with open(path, 'rb') as fd:
        requirements = [req.strip() for req in fd.readlines() if validate(req)]
    return requirements

install_requires = read_requirements('requirements.txt')

setup(
    name='serverless-env',
    version='0.1',
    url='http://github.com/cscetbon/serverless-helpers-py',
    license='BSD',
    description='Adds SQLAlchemy support to your Flask application',
    packages=['serverless_env'],
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
