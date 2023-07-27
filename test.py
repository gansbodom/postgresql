import psycopg2

conn = psycopg2.connect(database="netology_db", user="postgres", password="postgres")

with conn.cursor() as cur:
    cur.execute("""
    CREATE TABLE IF NOT EXISTS "clients" (
        "id" SERIAL PRIMARY KEY,
        "name" VARCHAR(40) NOT NULL,
        "surname" VARCHAR(80) NOT NULL,
        "email" VARCHAR(80) NOT NULL
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
        "number_id" INTEGER NOT NULL REFERENCES "phone" ("id"),
        CONSTRAINT pk PRIMARY KEY ("client_id", "number_id")
    ); 
    """)

    conn.commit()
    conn.close()
