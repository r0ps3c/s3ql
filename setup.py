import os
from setuptools import setup, find_packages
from setuptools import Extension
from setuptools.command.build import build as build_orig
from setuptools.command.sdist import sdist as sdist_orig

class build(build_orig):
    def finalize_options(self):
        super().finalize_options()
        from Cython.Build import cythonize
        self.distribution.ext_modules = cythonize([Extension(name='s3ql.deltadump',
                  sources=["src/s3ql/deltadump.c"], libraries=["sqlite3"])], language_level=3)

class sdist(sdist_orig):
    def finalize_options(self):
        super().finalize_options()
        from Cython.Build import cythonize
        self.distribution.ext_modules = cythonize([Extension(name='s3ql.deltadump',
                  sources=["src/s3ql/deltadump.pyx"])], language_level=3)

setup(name='s3ql',
    setup_requires=["cython"],
    cmdclass={"build": build, "sdist":sdist}
)