import os.path

from setuptools import setup, find_packages

setup(
    name='copy-windows-10-lock-screen-wallpaper',
    description='Copy Windows 10 Lock Screen Wallpaper',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown',
    version='1.1.4',
    packages=find_packages(),
    platforms='windows',
    url='https://github.com/seehait/copy-windows-10-lock-screen-wallpaper',
    entry_points={
        'console_scripts': ['copy-lock-screen-wallpaper=script.script:main'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
        'Operating System :: Microsoft :: Windows :: Windows 10'
    ],
    license='MIT'
)
