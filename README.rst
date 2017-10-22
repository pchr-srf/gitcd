Continuous tool for working with git
====================================

.. image:: https://travis-ci.org/claudio-walser/gitcd.svg?branch=master
    :target: https://travis-ci.org/claudio-walser/gitcd

Description
-----------

**gitcd** is a little helper for continuous integration workflows using
git as scm.

Installation
------------

Since gitcd is using python3 by default, you better upgrade.

After successful installation of python3 and pip for pyhton3, run the following command to install and upgrade gitcd:

.. code:: console

    pip3 install gitcd --upgrade

Argument Completion
-------------------

Gitcd supports argument completion, to activate this feature in linux run:

.. code:: console

    sudo activate-global-python-argcomplete3

Under OSX it isn't that simple unfortunately. Global completion requires bash support for complete -D, which was introduced in bash 4.2. On OS X or older Linux systems, you will need to update bash to use this feature. Check the version of the running copy of bash with echo $BASH_VERSION. On OS X, install bash via Homebrew (brew install bash), add /usr/local/bin/bash to /etc/shells, and run chsh to change your shell.
Afterwards you might be able to also just run:

.. code:: console

    sudo activate-global-python-argcomplete3

Usage
-----

**Initialize a project**

cd into one of your local directories
representing a git repository and run the init command. Pass your configuration, for most cases the default values should be ok.

.. code:: console

    git cd init


**Pull request status**

You are able to see the status of a feature
branch including the pull request and if it has already been reviewed by
someone.

.. code:: console

    git cd status


**Clean up local branches**

The tool is able to cleanup all local
branches which doesent exist on the origins. This is done with the clean command.

.. code:: console

    git cd clean


**Start new feature**

Starts a new feature branch from your master branch. If you dont pass a branchname, you will be asked later.

.. code:: console

    git cd start <branchname>


**Test a feature branch**

Merges a feature branch into your development branch. If you dont pass a branchname, your current branch will be taken.

.. code:: console

    git cd test <branchname>


**Open a pull request for code review**

Opens a pull request to your master branch. If you dont pass a branchname, your current branch will be taken.

.. code:: console

    git cd review <branchname>


**Finish a feature branch**

Merges it into your master and asks for permission to delete your
feature branch. If you dont pass a branchname, your current branch will be taken.

.. code:: console

    git cd finish <branchname>


**Compare your current branch**

Compares your current branch against the given branchname or the latest
tag if none is given.

.. code:: console

    git cd compare <branchname>


**Tagging the master branch**

Creates a tag from your master branch and pushes it to remote.

.. code:: console

    git cd release


Known Issues
~~~~~~~~~~~~

If you discover any bugs, feel free to create an issue on GitHub fork
and send us a pull request.

`Issues List`_.


Authors
-------

-  Claudio Walser (https://github.com/claudio-walser)
-  Gianni Carafa (https://github.com/mms-gianni)


Contributing
------------

1. Fork it
2. Create your feature branch (``git cd start my-new-feature``)
3. Commit your changes (``git commit -am 'Add some feature'``)
4. Push to the branch (``git push origin feature/my-new-feature``)
5. Create new Pull Request (``git cd review my-new-feature``)


License
-------

Apache License 2.0 see
https://github.com/claudio-walser/gitcd/blob/master/LICENSE

.. _Issues List: https://github.com/claudio-walser/gitcd/issues