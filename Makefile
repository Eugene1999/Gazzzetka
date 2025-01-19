createsuperuser:
	docker exec -it -e python gazzzetka ./DjangoGazzzetka/manage.py createsuperuser

migrate:
	docker compose exec web python DjangoGazzzetka/manage.py migrate

makemigrations:
	python3 DjangoGazzzetka/manage.py makemigrations

build:
	docker compose up --build -d
