#from distutils.core import setup
from setuptools import setup
import os
import logging
from os import path
this_directory = path.abspath(path.dirname('__file__'))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

#from setuptools import setup, find_packages
setup(
  name = 'pyserv',         # How you named your package folder (MyLib)
  packages = ['pyserv'],   # Chose the same as "name"
  version = '1.1.0',      # 
  long_description=long_description,
  long_description_content_type='text/markdown',

  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Python HTTPD Server to test GET and POST requests',   # Give a short description about your library
  author = 'Dheeraj M Pai',                   # Type in your name
  author_email = 'contact@advaitlabs.com',      # Type in your E-Mail
  url = 'https://github.com/dheerajmpai/pyserv/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/dheerajmpai/pyserv/',  
  keywords = ['HTTPD SERVER', 'PYTHON HTTPD', 'SERVER', 'GET', 'REQUESTS', 'HTTPD'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
      
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)

try:
    cwd = os.getcwd()
    python_file_path = os.popen('which python').read()
    python_dir = os.path.dirname(python_file_path)
    out = os.popen('cp '+cwd+'/pyserv/server.py ' + python_dir + '/serv').read()
    print (out)
    os.chmod(python_dir + '/serv', 0o775)
    logging.info('Created command serv')
    print ('Created Command')
except:
    print  ("No Command Made")
    pass
