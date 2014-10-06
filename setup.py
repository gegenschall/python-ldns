from setuptools import setup, Extension
from distutils.command.build import build
from distutils.command.install import install

version = '1.6.17'


class SWIGBuild(build):
    def run(self):
        self.run_command('build_ext')
        build.run(self)


class SWIGInstall(install):
    def run(self):
        self.run_command('build_ext')
        install.run(self)

ldns_module = Extension('_ldns',
                        sources=['ldns.i'],
                        include_dirs=['/usr/include/ldns', '/usr/local/include/ldns'],
                        swig_opts=['-I/usr/include/', '-I/usr/local/include', '-O'],
                        libraries=['ldns'])

setup(name='ldns',
      version=version,
      description="",
      long_description="""The goal of ldns is to simplify DNS programming, it supports recent RFCs like the DNSSEC documents, and allows developers to easily create software conforming to current RFCs, and experimental software for current Internet Drafts. A secondary benefit of using ldns is speed; ldns is written in C it should be a lot faster than Perl.

The first major tool to use ldns is Drill, from which part of the library was derived. From version 1.0.0 on, drill is be included in the ldns release and will not be distributed separately anymore. Its version number will follow that of ldns. The library also includes some other examples and tools to show how it can be used.

ldns depends on OpenSSL for its crypto functions. It can be compiled without OpenSSL, but of course you'll lose the ability to perform any cryptographic functions.
""",
      classifiers=[
            'Development Status :: 6 - Mature',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Topic :: Internet :: Name Service (DNS)'
      ],
      keywords='ldns network dns dnssec nameserver',
      author='Zdenek Vasicek, Karel Slany',
      author_email='vasicek AT fit.vutbr.cz, slany AT fit.vutbr.cz',
      url='http://www.nlnetlabs.nl/projects/ldns/',
      license='BSD',
      cmdclass={'build': SWIGBuild, 'install': SWIGInstall},
      py_modules=['ldns'],
      ext_modules=[ldns_module],
      zip_safe=False,
      )
