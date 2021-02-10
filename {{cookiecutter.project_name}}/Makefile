MANAGE := pipenv run python app/manage.py

nope:
	$(error Not a valid target)

check-env-%:
	@ if [ "${${*}}" = "" ]; then \
		echo "Environment variable $* not set"; \
		exit 1; \
	fi

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

req-dev:
	pipenv sync --dev

deploy:
	sh scripts/deploy.sh

lint:
	sh scripts/lint.sh

format:
	sh scripts/format.sh

test:
	sh scripts/test.sh

test-cov:
	sh scripts/test-cov.sh


codecov:
	sh scripts/codecov.sh
