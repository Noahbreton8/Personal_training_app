# Team71_3005

Marco Toito, Noah Breton, Victor Sandru

## Prerequistes

-   Postgresql
-   Python 3

**OR**

-   Docker

## Steps to run:

#### Without Docker

-   `pip3 install -r requirements.txt` on \*nix systems or `pip install -r requirements.txt` on Windows
-   `createdb final`
-   `psql -d final -f src/SQL/db_creation.sql`
-   `psql -U postgres -d final -f src/SQL/01_db_schema_creation.sql`
-   `psql -U postgres -d final -f src/SQL/02_db_population.sql`
-   `python3 src/GUI/gymDbGUI.py`

#### With Docker

On \*nix systems

-   `./dockerSetup.sh`

On Windows

-   run the `windowsSetup.bat` executable
