# Overview
This is a Python wrapper for the ldns C library. It has basically been ripped out of the original ldns distribution (contrib/python/) and packaged using distutils. That way you can simply use `pip` or `easy_install` to install it. 

This wrapper will be dynamically linked against your already installed ldns. It might or might not work according to the version you have installed, see below.

# Installation

## Requirements
* You need the ldns (tested with 1.6.17) library and its header files installed. See below for instructions to do just that.
* You need the python development headers
* You need swig. It might just already be installed on your system

### Debian/Ubuntu
Disclaimer: Debian Wheezy includes ldns 1.6.13. I did not test that version, it will probably not work. You might have to compile ldns yourself. See the ldns documentation for that. Debian Sid however is fine.

```
sudo apt-get install libldns1 libldns-dev python-dev
sudo apt-get install swig
```

### Arch Linux
```
pacman -S ldns
pacman -S swig
```

## Downloading
To be written

## Installation
If you downloaded this whole thing: `python setup.py install`

Or use pip for great easyness: `pip install ldns`

# TODO
* Test with other distributions
* Test with Python3