from setuptools import setup, find_packages
import os

version = '1.0.0'
name = 'leocornus.py.sandbox'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name=name,
    version=version,
    description="Play ground for learning Python language",
    long_description= (
      read('README.rst')
      + '\n' +
      'Detailed Documentation\n'
      '**********************\n'
      + '\n' +
      read('leocornus','py','sandbox','README.rst')
      + '\n' +
      read('CHANGES.txt')
      + '\n' +
      'Download\n'
      '***********************\n'
      ),
    classifiers=[
     'Framework :: Python',
     'Intended Audience :: Developers',
     'License :: OSI Approved :: GNU General Public License (GPL)',
     'Topic :: Software Development :: Learning Sandbox',
     'Topic :: Software Development :: Libraries :: Python Modules',
      ],

    keywords='development sandbox learning',

    author='Sean Chen',
    author_email='sean.chen@leocorn.com',
    url='http://github.com/leocornus/%s' % name,
    license='GPLv2',

    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['leocornus', 'leocornus.py'],
    include_package_data = True,

    zip_safe=False,
    install_requires = [
      'setuptools',],
    extras_require={
      'test' : ['zope.testing'],
    },
    tests_require = ['zope.testing'],
    test_suite = '%s.tests.test_suite' % name,

    entry_points = { 'zc.buildout' : ['default = leocornus.py.sandbox:Dist',
                                      ] },
)
