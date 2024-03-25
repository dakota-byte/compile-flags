## Compile flags

```
usage: debflags.py [-h] -f FILE [-k KEYWORD] [-v]

Python script for extracting Debian Sid compile flags.

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Input file
  -k KEYWORD, --keyword KEYWORD
                        Keyword used by the rules file to refer to flags.
  -v, --verbose         Print entire line and every single occurrence. Note: A $ means that the line contains a reference of the flags.
```

### Examples with output

Example 1:

`python .\debflags.py -f .\rules.txt -k CONFARGS`

```
Flags found: --prefix=/usr --openssldir=/usr/lib/ssl --libdir=lib/$(DEB_HOST_MULTIARCH) no-idea no-mdc2 no-rc5 no-zlib no-ssl3 enable-unit-test no-ssl3-method enable-rfc3779 enable-cms no-capieng no-rdrand enable-ec_nistp_64_gcc_128
```

Example 2:

`python .\debflags.py -f .\rules.txt -k CONFARGS -v`

```
Line 32: CONFARGS  = --prefix=/usr --openssldir=/usr/lib/ssl --libdir=lib/$(DEB_HOST_MULTIARCH) no-idea no-mdc2 no-rc5 no-zlib no-ssl3 enable-unit-test no-ssl3-method enable-rfc3779 enable-cms no-capieng no-rdrand
Line 44: CONFARGS += enable-ec_nistp_64_gcc_128
Line 56$: ../Configure shared $(CONFARGS) debian-$(DEB_HOST_ARCH)-$$opt; \
Line 60$: mkdir build_static; cd build_static; ../Configure no-shared $(CONFARGS) debian-$(DEB_HOST_ARCH) ;perl configdata.pm -d
Line 62$: mkdir build_shared; cd build_shared; HASHBANGPERL=/usr/bin/perl ../Configure shared $(CONFARGS) debian-$(DEB_HOST_ARCH) ;perl configdata.pm -d

Flags found: --prefix=/usr --openssldir=/usr/lib/ssl --libdir=lib/$(DEB_HOST_MULTIARCH) no-idea no-mdc2 no-rc5 no-zlib no-ssl3 enable-unit-test no-ssl3-method enable-rfc3779 enable-cms no-capieng no-rdrand enable-ec_nistp_64_gcc_128
```
