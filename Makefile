.PHONY: d-homework-i-run
# Make all actions needed for run homework from zero.
d-homework-i-run:
	@make init-configs-i-dev && \
	make d-run

.PHONY: d-homework-i-purge
# Make all actions needed for purge homework related data.
d-homework-i-purge:
	@make d-purge


.PHONY: d-run
# Just run
d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		COMPOSE_PROFILES=full_dev \
		docker-compose up --build


.PHONY: d-run-i-local-dev
# Just run services for local-dev
d-run-i-local-dev:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		COMPOSE_PROFILES=local_dev \
		docker-compose up --build postgres

.PHONY: d-run-i-extended
# Shutdown previous, run in detached mode, follow logs
d-run-i-extended:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down --timeout 0 && \
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		COMPOSE_PROFILES=full_dev \
		docker-compose up --build --detach && \
	make d-logs-follow

.PHONY: d-stop
# Stop services
d-stop:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down


.PHONY: d-logs-follow
# Follow logs
d-logs-follow:
	@docker-compose logs --follow


.PHONY: d-purge
# Purge all data related with services
d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down --volumes --remove-orphans --rmi local --timeout 0


.PHONY: migrate
# Shortcut
migrate:
	@python manage.py migrate

.PHONY: migrations
# Shortcut
migrations:
	@python manage.py makemigrations


.PHONY: init-configs-i-dev
# Make some initialization steps. For example, copy configs.
init-configs-i-dev:
	@cp docker-compose.override.dev.yml docker-compose.override.yml
	@cp .env.example .env


.PHONY: init-dev-i-create-superuser
init-dev-i-create-superuser:
	@DJANGO_SUPERUSER_PASSWORD=admin123 python manage.py createsuperuser --user admin --email admin@gmail.com --no-input

.PHONY: util-i-kill-by-port
util-i-kill-by-port:
	@sudo lsof -i:8000 -Fp | head -n 1 | sed 's/^p//' | xargs sudo kill

.PHONY: django-i-create-humans-i-2
django-i-create-humans-i-2:
	@python manage.py create_humans 2

.PHONY: d-i-django-i-create-humans-i-2
d-i-django-i-create-humans-i-2:
	@docker-compose run --rm app make django-i-create-humans-i-2

