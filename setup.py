from setuptools import setup



setup(
    name='mail_room_madness',
    description='A package for building and running the mail_room_madness function',
    package_dir={'':'src'},
    author='Mark and Kavdi',
    author_email='kavdyjh@gmail.com mreynoso@spu.edu',
    py_modules=['mail_room_madness'],
    install_requires=['tabulate'],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython', 'faker']
    },
    entry_points={
        'console_scripts': [
            'mail_room_madness=mail_room_madness:main'
        ]
    }
)