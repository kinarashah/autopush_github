from setuptools import setup

setup(name='autopush_github',
      version='0.1',
      description='Automatically push Leetcode solutions to Github',
      url='http://github.com/kinarashah/autopush-github',
      author='Kinara Shah',
      author_email='kinarahs@usc.edu',
      license='MIT',
      packages=['autopush_github'],
      install_requires = [
      'requests'
      ],
      zip_safe=False)
