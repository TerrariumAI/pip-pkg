from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='terrariumai',
      version='0.1.4',
      description='Utility package for using Terrarium.ai',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/terrariumai',
      author='Zac Holland',
      author_email='zacharyhollland@gmail.com',
      license='MIT',
      packages=['terrariumai'],
      install_requires=[
          'grpcio',
          'protobuf'
      ],
      zip_safe=False,
      classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
      ])
      