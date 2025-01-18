createsuperuser:
	docker exec -it -e python gazzzetka ./DjangoGazzzetka/manage.py createsuperuser

migrate:
	python3 ./DjangoGazzzetka/manage.py migrate

migrations:
	python3 DjangoGazzzetka/manage.py makemigrations