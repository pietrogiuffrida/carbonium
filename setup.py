from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
      name='clogger',
      version='0.12.41',
      url='https://github.com/pietrogiuffrida/customlogger/',
      author='Pietro Giuffrida',
      author_email='pietro.giuffri@gmail.com',
      license='MIT',
      packages=['clogger'],
      zip_safe=False,
      install_requires=[],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      description='python logger configuration, my way',
      long_description=long_description,
      long_description_content_type='text/markdown',
)
