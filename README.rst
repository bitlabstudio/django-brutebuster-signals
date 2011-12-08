Django BruteBuster Signals
===============================

If you are using the BruteBuster App to log failed login attempts, you may want to be notified via email. 

**Features:**

If someone tries to login using the wrong credentials, BruteBuster creates a new model instance, which includes all significant information about this attempt. After save() the signal handler sends a notification email to settings.MANAGERS, which includes the basic model information.


How to use
==========

Get und implement BruteBuster:

* `django-brutebuster <http://code.google.com/p/django-brutebuster/>`_

Make sure it is working perfect.

* Install this package::

    pip install -e git://github.com/bitmazk/django-brutebuster-signals#egg=brutebuster_signals

* Add ``brutebuster_signals`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        [...]
        'brutebuster_signals',
    }

* Add ``MANAGERS`` to your ``settings.py``::

    MANAGERS = (
        ('Foo Bar', 'foobar@example.com'),
    )

