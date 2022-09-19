from setuptools import setup

setup(name='clean_folder',
      version='1.1',
      description='Distributes files by type, changes filenames',
      url='https://github.com/flatline-code/goIt-python-06',
      author='flatline_code',
      author_email='keysneuro@gmail.com',
      license='MIT',
      packages=['clean_folder'],
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:sort_files']}
      )
