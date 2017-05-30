.. Set default highlighting language for this document:

.. highlight:: bash

.. _cli:

Command Line Interface
======================

The command line interface is deployed as a docker (called *authorization*) in
our :term:`docker engines <docker engine>`.  The command itself is called
``authz`` and can be executed *from outside the docker* using the
``docker exec`` command on the docker engine.  You'll need to be root::

    # From your local machine:
    ssh dc01.datapunt.amsterdam.nl

    # Then, on dc01:
    sudo su -
    docker exec -t authorization authz

Without options, this command will return some usage info:

.. code-block:: text

    Usage: authz [OPTIONS] COMMAND [ARGS]...

    Options:
      --debug
      --psql-host TEXT
      --psql-port INTEGER
      --psql-db TEXT
      --psql-user TEXT
      --psql-password TEXT
      --help                Show this message and exit.

    Commands:
      user

Checking the authorization level of a user
------------------------------------------

::

    docker exec -t authorization authz <email> info

Setting the authorization level of a user
-----------------------------------------

::

    docker exec -t authorization authz <email> assign <level>

where `<level>` must be one of `DEFAULT`, `EMPLOYEE`, or `EMPLOYEE_PLUS`.

.. note::

    -   Setting the authorization level to `DEFAULT` will *remove* the user from
        the authorization database (if present).
    -   Setting the authorization level to anything else will *add* the user to
        the authorization database if not already present.

Setting the password of a user
------------------------------

Currently, the CLI doesn't automatically create passwords for new users. You'll
have to create these yourself, using a cryptographically strong Pseudo-Random
Number Generator (PRNG). When you have a sufficiently strong password::

    docker exec -t authorization authz <email> password <password>

.. warning::

    Make sure the password is properly escaped, especially if it contains
    characters that are interpreted by the shell, such as ``$?`"'|&(){}``
    etcetera.
