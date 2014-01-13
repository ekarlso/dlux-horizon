Setup
=====

This is a quick guide to setting up dlux.

Prerequisites
-------------

dlux is a web UI for talking to Tuskar. It is an extension of the
existing Horizon web interface.

Installation prerequisites are:

1. A functional OpenStack installation. Horizon and dlux will
   connect to the Keystone service here. Keystone does *not* need to be
   on the same machine as your dlux interface, but its HTTP API
   must be accessible.
2. A functional Tuskar installation. dlux talks to Tuskar via an
   HTTP interface. It may, but does not have to, reside on the same
   machine as dlux, but it must be network accessible.

Installing the packages
-----------------------

dlux is a Django app written in Python and has a few installation
dependencies:

On a RHEL 6 system, you should install the following:

::

    yum install git python-devel swig openssl-devel mysql-devel libxml2-devel libxslt-devel gcc gcc-c++

The above should work well for similar RPM-based distributions. For
other distros or platforms, you will obviously need to convert as
appropriate.

Then, you'll want to use the ``easy_install`` utility to set up a few
other tools:

::

    easy_install pip
    easy_install nose

Install the Management UI
-------------------------

Begin by cloning the horizon and dlux repositories:

::

    git clone git://github.com/openstack/horizon.git
    git clone git://github.com/ekarlso/dlux-horizon.git dlux

Go into ``horizon`` and install a virtual environment for your setup::

    cd horizon
    python tools/install_venv.py


Next, run ``run_tests.sh`` to have pip install Horizon dependencies:

::

    ./run_tests.sh

Set up your ``local_settings.py`` file:

::

    cp ../dlux/local_settings.py.example openstack_dashboard/local/local_settings.py

Open up the copied ``local_settings.py`` file in your preferred text
editor. You will want to customize several settings:

-  ``CONTROLLER_URL`` should point to the ODL Controller you
   configured. It normally runs on port http://x.x.x.x/8080/v2.

Install Tuskar-UI with all dependencies in your virtual environment::

    tools/with_venv.sh pip install -r ../dlux/requirements.txt
    tools/with_venv.sh pip install -e ../dlux/

And enable it in Horizon::

    cp ../dlux/_50_dlux.py.example openstack_dashboard/local/enabled/_50_dlux.py

Starting the app
----------------

If everything has gone according to plan, you should be able to run:

::

    tools/with_venv.sh ./manage.py runserver

and have the application start on port 8080. The DLUX dashboard will
be located at http://localhost:8080/networking

If you wish to access it remotely (i.e., not just from localhost), you
need to open port 8080 in iptables:

::

    iptables -I INPUT -p tcp --dport 8080 -j ACCEPT

and launch the server with ``0.0.0.0:8080`` on the end:

::

    tools/with_venv.sh ./manage.py runserver 0.0.0.0:8080
