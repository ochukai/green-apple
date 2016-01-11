```shell

ssh tester@42.121.106.244

cd /var/django/kkhservice/green

```


```shell

python manage.py collectstatic --noinput

uwsgi --reload /tmp/green.pid

```