import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="Flask Adventure Game"
    version="0.0.1",
    author="Ethan Kubistek",
    author_email="ekubistek@email.com",
    url="https://github.com/EthanKubistek/A-knock-at-the-window-flask-game",
    description="Flask Adventure Game OOP game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
