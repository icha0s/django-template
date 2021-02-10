MANAGE := pipenv run python manage.py

nope:
	$(error Not a valid target)

check-env-%:
	@ if [ "${${*}}" = "" ]; then \
		echo "Environment variable $* not set"; \
		exit 1; \
	fi


app: migrate gunicorn

.PHONY: uvicorn
uvicorn:
	pipenv run uvicorn \
		--access-log \
		--host 0.0.0.0 \
		--port 8000 \
		--backlog 100 \
		--log-level info \
		--workers 4 \
		--lifespan off \
		asgi:application

.PHONY: gunicorn
gunicorn:
	pipenv run gunicorn \
		--access-logfile - \
		--bind 0.0.0.0:8000 \
		--backlog 100 \
		--chdir /app \
		--error-logfile - \
		--preload \
		--workers 4 \
		wsgi:application

shell:
	$(MANAGE) shell

makemigrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

createsuperuser:
	$(MANAGE) createsuperuser

collectstatic:
	$(MANAGE) collectstatic

makemessages:
	$(MANAGE) makemessages -l en -l uk -l ru

compilemessages:
	$(MANAGE) compilemessages -l en -l uk -l ru

req:
	pipenv sync
	$(MAKE) patch

celery:
	pipenv run celery -A apps worker -l INFO -c 4 -X finance

celery-finance:
	pipenv run celery -A apps worker -l INFO -c 1 --pool=solo -Q finance

celery-health-check:
	pipenv run celery -A apps inspect ping -d celery@`hostname`

beat:
	pipenv run celery -A apps beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
