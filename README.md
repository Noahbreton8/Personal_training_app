# Team71_3005

Marco Toito, Noah Breton, Victor Sandru

## Prerequistes

-   Postgresql
-   Python 3

## Steps to run:

-   `pip3 install -r requirements.txt` on \*nix systems or `pip install -r requirements.txt` on Windows
-   `createdb final`
-   `psql -d final -f src/SQL/db_creation.sql`
-   `psql -U postgres -d final -f src/SQL/db_schema_creation.sql`
-   `psql -U postgres -d final -f src/SQL/db_population.sql`
-   `python3 src/GUI/gymDbGUI.py`
