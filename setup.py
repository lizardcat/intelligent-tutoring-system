# setup.py
# from setuptools import setup, find_packages

# setup(
#     name="intelligent-tutoring-system",
#     version="0.1",
#     packages=find_packages(),
#     install_requires=[
#         "numpy",
#         "pandas",
#         "flask",
#         "streamlit",
#         "sqlite3",
#         "json",
#         "locust",
#         "scipy",
#         "matplotlib",
#         "seaborn",
#         "plotly",
#         "scikit-learn",
#         "tensorflow",
#         "torch",
#         "torchvision",
#         "transformers",
#         "nltk",
#         "spacy",
#         "beautifulsoup4",
#         "requests",
#         "pytest",
#         "pytest-cov",
#         "coverage",
#         "tox",
#         "black",
#         "flake8",

#         "mypy",
#         "isort",
#         "pylint",
#         "bandit",
#         "safety",
#         "pre-commit",
#         "pytest-xdist",
#         "pytest-html",
#         "pytest-mock",
#         "pytest-asyncio",
#         # List your dependencies here
#         # 'flask',
#         # 'numpy',
#     ],
# )



from setuptools import setup, find_packages

setup(
    name="intelligent_tutoring_system",
    version="0.1",
    packages=find_packages(include=['intelligent_tutoring_system*']),
    python_requires=">=3.6",
)