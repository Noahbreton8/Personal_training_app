FROM postgres:latest

ENV POSTGRES_PASSWORD=student
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=finalProject
ENV PGUSER=postgres

COPY src/SQL/01_db_schema_creation.sql /docker-entrypoint-initdb.d/
COPY src/SQL/02_db_population.sql /docker-entrypoint-initdb.d/

EXPOSE 5432

WORKDIR /app