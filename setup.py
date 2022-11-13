from setuptools import Extension, setup, find_packages
import numpy as np


try:
    from Cython.Build import cythonize
    from Cython.Distutils import build_ext
except ImportError:
    USE_CYTHON = False
else:
    USE_CYTHON = True


cmdclass = {}

ext = ".pyx" if USE_CYTHON else ".c"

extensions = [
    Extension(
        "surprise.similarities",
        ["surprise/similarities" + ext],
        include_dirs=[np.get_include()],
    ),
    Extension(
        "surprise.prediction_algorithms.matrix_factorization",
        ["surprise/prediction_algorithms/matrix_factorization" + ext],
        include_dirs=[np.get_include()],
    ),
    Extension(
        "surprise.prediction_algorithms.optimize_baselines",
        ["surprise/prediction_algorithms/optimize_baselines" + ext],
        include_dirs=[np.get_include()],
    ),
    Extension(
        "surprise.prediction_algorithms.slope_one",
        ["surprise/prediction_algorithms/slope_one" + ext],
        include_dirs=[np.get_include()],
    ),
    Extension(
        "surprise.prediction_algorithms.co_clustering",
        ["surprise/prediction_algorithms/co_clustering" + ext],
        include_dirs=[np.get_include()],
    ),
]

if USE_CYTHON:
    extensions = cythonize(
        extensions,
        compiler_directives={
            "language_level": 3,
            "boundscheck": False,
            "wraparound": False,
            "initializedcheck": False,
            "nonecheck": False,
        },
    )
    cmdclass.update({"build_ext": build_ext})

setup(
    ext_modules=extensions,
    packages=find_packages(exclude=["tests*"]),
    cmdclass=cmdclass,
)
