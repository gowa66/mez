
Quick start guide
=================

Clone
-----


    $ git clone git@github.com:gowa66/mez.git
    $ cd mez


Install virtualenv
------------------


    $ virtualenv .env
    $ source .env/bin/activate
    (.env)$


Install packages
----------------


    (.env)$ pip install -r requirements.txt


Run project
----------------


    (.env)$ make migrate
    (.env)$ make createsuperuser
    (.env)$ make collectstatic
    (.env)$ make run


