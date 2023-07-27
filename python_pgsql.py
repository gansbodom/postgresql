import psycopg2

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS "clients" (
            "id" SERIAL PRIMARY KEY,
            "first_name" VARCHAR(40) NOT NULL,
            "last_name" VARCHAR(80) NOT NULL,
            "email" VARCHAR(80) NOT NULL UNIQUE
            );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS "phone" (
            "id" SERIAL PRIMARY KEY,
            "phone_number" INTEGER NOT NULL
        ); 
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS "client_phone" (
            "client_id" INTEGER NOT NULL REFERENCES "clients" ("id"),
            "phone_id" INTEGER NOT NULL REFERENCES "phone" ("id"),
            CONSTRAINT pk PRIMARY KEY ("client_id", "phone_id")
        ); 
        """)
        conn.commit()

def add_client(conn, first_name, last_name, email, phones=None):
    pass

def add_phone(conn, client_id, phone):
    pass

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    pass

def delete_phone(conn, client_id, phone):
    pass

def delete_client(conn, client_id):
    pass

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    pass


with psycopg2.connect(database="netology_db", user="postgres", password="postgres") as conn:
    create_db(conn)# вызывайте функции здесь

conn.close()