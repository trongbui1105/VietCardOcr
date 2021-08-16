from distutils.core import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
  name = 'vietcardocr',         # How you named your package folder (MyLib)
  packages = ['vietcardocr'],   # Chose the same as "name"
  package_data={'vietcardocr': ['text/*.txt', 'checkpoints/CTPN.pth']},
  version = '0.3.1',      # Start with a small number and increase it with every change you make
  include_package_data=True,
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Extract Vietnamese Card',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'TrongBui',                   # Type in your name
  author_email = 'buiquoctrong110500@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/trongbui1105/vietcardocr.git',   # Provide either the link to your github or to your website
  keywords = ['extract'],   # Keywords that define your package best
  install_requires=['opencv-python', 'torch', 'torchvision', 'vietocr', 'Pillow', 'unidecode', 'numpy', 'pyyaml'],            # I get to this in a second
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which python versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9'
  ],
)