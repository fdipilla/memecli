memecli
=======

Command line wrapper over http://memegenerator.net API.

Status
------
Work in progress.


Install
-------

.. code-block:: bash

    $ pip install memecli

Or, you can get the code

.. code-block:: bash

    git clone https://github.com/surrealists/memecli.git
    cd memecli
    python setup.py install


Usage
------

.. code-block:: bash

    memecli --help

::

    Usage: memecli [OPTIONS] COMMAND [ARGS]...

    Command line wrapper over http://memegenerator.net API

    Options:
    --version  Show the version and exit.
    --help     Show this message and exit.

    Commands:
    content-flag-create             Flag content for removal, for cases of...
    meme-create                     Creates a captioned image.
    meme-select                     Select an instance by its instance id.
    meme-select-by-new              Returns recently created instances, for a...
    meme-select-by-popular          Returns the most popular instances for a...
    new                             Convenient way of create a new meme
                                    instance.
    template-search                 Returns a list of search results filtered
                                    by...
    template-select-by-new          Returns the most recently created
                                    generators.
    template-select-by-popular      Returns the most popular generators for
                                    the...
    template-select-by-trending     Returns recently trending generators.
    template-select-by-url-name-or-generator-id
                                    Returns information about a specific...
    template-select-related-by-name
                                    Returns generators that are related to a...


License
-------

This work is under a MIT license.
