eszone\_haproxy
==============

Introduction
------

This Django project covers build, generation, validation and deployment processes of a HAProxy configuration file lifecycle 
with common API calls. Project is developed as part of a Bachelor's thesis about NFV (Network Functions Virtualization)
and divided into two main parts, first being called [api\_core](https://github.com/erigones/api_core ) and second 
[api\_haproxy](https://github.com/erigones/api_haproxy ). Submodule api\_core provides common functionality like an 
authentication and various exceptions and submodule api\_haproxy covers all of the earlier mentioned functionality needed
to deploy HAProxy configuration.  

A typical use case may include this Django project placed within a HAProxy virtual machine template  labeling it a 
'loadbalancer'. With the created template you can spawn virtual machines for your customers and then provide them with 
ways to configure it as they demand later on without need to access a virtual machine using ssh.

If you intend to use only specific submodule, visit its repository for more information.

Running API
------

For testing and development purposes, running API with a web server shipped in Django is fine enough. For production 
though, you may want to consider a production-ready web server like uwsgi or gunicorn. Deploying a Django application 
within one of these web servers is a matter of pointing to a wsgi.py file, which should be contained in your project's 
directory. In order how to configure these servers you can start reading Django documentation on how to deploy a Django
project using [uwsgi](https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/uwsgi/) or 
[gunicorn](https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/gunicorn/).

Interacting with API
------

API is intended to be used by a custom API client incorporated into your dashboard. For testing purposes, python httpie 
package can help a bit. Install it with a command:

`pip install httpie`

After installation, you can, for example, interact with an API using following commands:

`http POST http://${IP}:${PORT}/v1/haproxy/section/ section='global' configuration='{"daemon": ""}'`

`http POST http://${IP}:${PORT}/v1/haproxy/configuration/generate/`

`http GET http://${IP}:${PORT}/v1/haproxy/configuration/validate/`

Deploying with authentication
------

Currently, authentication from the api\_core application is not integrated into api\_haproxy. If you plan to
use api\_haproxy in a private network behind NAT and firewalls, there is probably no need to have an authentication 
enabled at all. On the other hand, if you plan to have some kind of authentication, here are steps to integrate the 
simple token authentication from api_core application:

- submodule api\_core into your Django project

`git submodule add *repository-link*`

- import permissions and authentication modules by adding following lines to the top of a views.py file

```python
    from rest_framework.permissions import IsAuthenticated
    from api_core.authentication import SimpleTokenAuthentication
```

- add permissions and authentication classes as attributes to each APIView you want to authenticate. For example:

```python
    class TestAuthView(APIView):
        authentication_classes = (SimpleTokenAuthentication, )
        permission_classes = (IsAuthenticated, )
```

From now on, you can make HTTP requests with an authentication.token field in them, assuming you have created first token 
by hand.

- generation of a master token is accessible after running `python manage.py migrate` and submoduling an api\_core app.

`python manage.py shell`

then, enter below listed commands in a sequence

```python
    > from api_core.models import SimpleTokenAuthModel
    > token = SimpleTokenAuthModel()
    > token.save()
    > print token.token_uuid
```
