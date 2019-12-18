from distutils.core import setup
#from setuptools import setup, find_packages
setup(
  name = 'pyserv',         # How you named your package folder (MyLib)
  packages = ['saenews'],   # Chose the same as "name"
  version = '0.3.0',      # 
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'required code for saenews',   # Give a short description about your library
  author = 'saenews',                   # Type in your name
  author_email = 'contact@advaitlabs.com',      # Type in your E-Mail
  url = 'https://github.com/dheerajmpai/saenews/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/dheerajmpai/saenews/archive/v_033.tar.gz',  
  keywords = ['OPENCV', 'IMAGE PROCESSING', 'NEWS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'beautifulsoup4',
          'opencv-contrib-python',
          'Pillow',
          'matplotlib'
          
      
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
