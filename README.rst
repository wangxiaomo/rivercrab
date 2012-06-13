=====================
README for River Crab
=====================

:copyright: Copyright 2012, Philip Xu <pyx@xrefactor.com>
:license: BSD New, see LICENSE for details.

`River Crab`_ - a mythical creature that enforces censorship.

::

                 .___
           __==+"^--v;
        _>+~-      .v`
      <>`          _v` ..
     %>       C_= .v~ .WC    .__.
    <>       R.%+ :v: )}{;  .i8pm*==,.          _______=>=+~
   .v`      A :v   vs>~ =v.:v`.__aka+l,       .v^:_%pyx;+v>~"~         ._,.
   =l      B  +~   3}    v; "i>:.  :_%>       -{= -.  .=i>`      ..    =e~"i,
   =s       B.=.        _v`   -"{%"^~           -<=+^^^~      _%^{X'  _v+  :v.
   -l;       Y+`       =}`      :v.             _%^          %>  *l=+"~    <}
    -<=.       ..___=|v1_,.    __i_=,,         .%~     .___<=}`          _>+`
      -!++=+++^"^""!~:__>+<a/+"~-----"s,. _>=+"""^"^"nz+|_v}"+==_=_===++"~
                      --+I?"`          -""^          -{1~~-
                       :v~         :s,     .%;         v;
                .______)v.          -^^+==|"`         .v>++~""""+==,.
            ._>+~---..._vs,                         ._vi_______.___ul,,
          .=n|____===+^~_=v=.       Little       .<a><__:------~--+v,=s.
        _%^s:---- .  _>+~-<}"<,,  River Crab  __>"=>ns,-"<,        -l,<>
       <}.%~        :v` _%^   <I"< ~~~~~~~~ _a1=+<,:<|-=<vS(        -{vi
      :v_%+         3ov"`    =ns>^.%I1}~~+"~-{u;  -+|*_. -<s         -{s
      :dr          .vo`      )Y~   ""`        I`   .-.*`  -l
       -            ""        -


.. _River Crab: https://en.wikipedia.org/wiki/River_crab_(internet_slang)

Jokes aside,
this little program might help you in regular forum management tasks,
possibly posts moderating, and deleting offending post automatically, etc.

Requirements
============

- CPython >= 2.6
- BeautifulSoup 4
- argparse if using python 2.6

Download
========

Download the latest source from `bitbucket`_, `github`_, or `PyPI`_, then decompress it.

.. _bitbucket: https://bitbucket.org/pyx/rivercrab/get/tip.tar.bz2
.. _github: https://github.com/pyx/rivercrab/tarball/master
.. _PyPI: http://pypi.python.org/pypi/rivercrab/

Alternatively, you can check out the source from repository::

  hg clone https://bitbucket.org/pyx/rivercrab

If you prefer git::

  git clone git://github.com/pyx/rivercrab.git

Installation
============

Using ``setup.py``
------------------

The standard way, inside unpacked/checked-out project directory::

  python setup.py install


Using Pip and VirtualEnv
------------------------

However, I recommend installation with `pip`_ in a `virtualenv`_ environment.
It will make life much more easier.

.. _pip: http://www.pip-installer.org/
.. _virtualenv: http://www.virtualenv.org/

First, create an environment::

  mkdir test && virtualenv test

Activate the environment::

  cd test && source bin/activate

Install with ``pip``::

  pip install rivercrab

That's it, and you can goto `Configuration`_ .


If you choose to install from the source,
go get the source use any method mentioned above,
for example, cloning from https://bitbucket.org/pyx/rivercrab ::

  hg clone https://bitbucket.org/pyx/rivercrab

Install from local with ``pip``::

  pip install -e rivercrab

Configuration
=============

The default location of configuration file is ``~/.rivercrabrc``.

This file should be in `JSON <http://json.org/>`_ format.

An minimal working one might be something like this::

  [
      {
          "tieba": "TIEBANAME",
          "username": "USERNAME",
          "password": "PASSWORD",
          "loop": true,
          "interval": 600,
          "timeout": 10,
          "delete_filter": "default",
          "blacklist": "~/.blacklist"
      }
  ]

As for right now, RiverCrab supports one user account and a single forum only.
Also, the default ``delete_filter`` implementation only understand `Baidu Tieba`_ now.
Later versions may have support for broader usage.

Usage
=====

The default ``delete_filter`` will tell River Crab to delete any post with text in the title that matches any one of entries in ``blacklist`` file.

``blacklist`` file should contain python style regular expressions,
one rule per line. For example::

  BADWORD
  BAD.{,4}WORD
  BA+DWORD

You should alway test your rcfile and regexps in dry run mode first::

  rivercrab -p -c testing_rcfile

Run ``rivercrab --help`` for more information.

Caveats and Limitations
=======================

#. All configuration files,
   data file such as ``~/.blacklist`` included,
   should be saved with encoding "utf-8".

#. Because of the configuration file contains information about authentication credentials,
   it is necessary to restrict access to this file.

   For example, in ``POSIX`` system, the following should be enough::

     chmod go-rwx ~/.rivercrabrc

#. Only support `Baidu Tieba`_ for now.

#. This is a quick hack done over a weekend, thus,
   there is hardly any validation done on the content returned by server.
   e.g, This program does not even check if user login was successful.

Later version will be more robust,
provided that I have more free time.

.. _Baidu Tieba: http://tieba.baidu.com/

Testing
=======

To run tests,
use::

  make test

Changelog
=========

- 0.8

  - added support for new style tieba

- 0.7

  - Bugfix:

    - commented out catch-all exception handling

- 0.6

  - Added support for python 3

- 0.5

  - Bugfix:

    - format string compatibility with python 2.6

- 0.4

  - Added support for python 2.6

- 0.3

  - Bugfix:

    - Fixed typos.
    - Better error handling.

  - New features:

    - Command line switch '-p' for dry run.
    - new setting 'timeout' in config.

- 0.2

  - Bugfix:

   - decoding content with 'gbk' encoding.

- 0.1

  - Initial release.

Contributing
============

:Mercurial Repository: https://bitbucket.org/pyx/rivercrab
:Git           Mirror: https://github.com/pyx/rivercrab
:Issue       Tracking: https://bitbucket.org/pyx/rivercrab/issues
