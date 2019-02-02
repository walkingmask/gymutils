from setuptools import find_packages, setup


with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='gymutils',
    version='0.0.1',
    description='Tools for OpenAI gym',
    url='https://github.com/walkingmask/gymutils',
    author='walkingmask',
    author_email='walkingmask@gmail.com',
    long_description=long_description,
    license='MIT',
    install_requires=['opencv-python', 'numpy', 'Pillow', 'scikit-image'],
    packages=find_packages()
)
