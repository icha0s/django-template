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
		--access-logfile - \
		--bind 0.0.0.0:8000 \
		--backlog 100 \
		--chdir /app \
		--error-logfile - \
		--reload \
		--workers 4 \
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
