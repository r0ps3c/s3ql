import os

from setuptools import Extension, find_packages, setup
from setuptools.command.build import build as build_orig
from setuptools.command.sdist import sdist as sdist_orig


class build(build_orig):
    def finalize_options(self):
        super().finalize_options()
        from Cython.Build import cythonize
        self.distribution.ext_modules = cythonize([Extension(name='s3ql.sqlite3ext',
                  sources=["src/s3ql/sqlite3ext.cpp"], libraries=["sqlite3"])], language_level=3)

class sdist(sdist_orig):
    def finalize_options(self):
        super().finalize_options()
        from Cython.Build import cythonize
        self.distribution.ext_modules = cythonize([Extension(name='s3ql.sqlite3ext',
                  sources=["src/s3ql/sqlite3ext.pyx"])], language_level=3)

setup(name='s3ql',
    setup_requires=["cython"],
    cmdclass={"build": build, "sdist": sdist}
)