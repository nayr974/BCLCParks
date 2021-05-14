Alembic Migrations:

run these from project root. 

Migrate: `docker-compose run app alembic revision --autogenerate -m "<your message here>"`
Upgrade: `docker-compose run app alembic upgrade head`


CLI ACCESS TO DB: 

`docker exec -it bclcparks_db_1 psql -U postgres`