"""A setuptools based setup module.

https://github.com/requests/requests/blob/master/setup.py
"""
import os
import sys
from codecs import open
from shutil import rmtree

from setuptools import setup, find_packages, Command

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

about = {}

with open(os.path.join(here, 'folderspy', '__version__.py')) as f:
    exec(f.read(), about)


class PublishCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def clean_up_builds():
        try:
            print('Removing any previous builds')
            rmtree(os.path.join(here, 'dist'))
            rmtree(os.path.join(here, 'build'))
            rmtree([os.path.join(here, dir) for dir in os.listdir(here) if dir.endswith('.egg-info')][0])
        except FileNotFoundError:
            pass

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.clean_up_builds()

        print('Building Source and Wheel (universal) distribution')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        print('Uploading the package to PyPI via Twine...')
        os.system('twine upload dist/*')

        print('Pushing git tags...')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()

setup(
    name='folderspy',
    version=about['__version__'],
    description='Watch folders for file/directory events with a simple API.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/rob-white/folderspy',
    author='Rob White',
    author_email='robathan4@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'pyinotify ; platform_system == "Linux"',
        'pypiwin32 ; platform_system == "Windows"',
        'MacFSEvents ; platform_system == "Darwin"'
    ],
    cmdclass={
        'publish': PublishCommand
    }
)
