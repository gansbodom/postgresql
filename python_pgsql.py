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
            "phone_number" BIGINT NOT NULL
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
    with conn.cursor() as cur:
        cur.execute("""
             INSERT INTO public."clients" (first_name, last_name, email) VALUES
             (%s, %s, %s) """, (first_name, last_name, email))
        conn.commit()


def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO public."phone" (phone_number) VALUES
            (%s) """, [phone])
        conn.commit()

        cur.execute("""
        SELECT id from public."phone" WHERE phone_number=%s
        """, [phone])
        phone_id = cur.fetchone()[0]

        cur.execute("""
            INSERT INTO public."client_phone" (client_id, phone_id) VALUES
            (%s, %s) """, (client_id, phone_id))
        conn.commit()


def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    with conn.cursor() as cur:
        if first_name:
            cur.execute("""
            UPDATE public."clients"
                SET first_name=%s
                WHERE id = %s;
            """, (first_name, client_id))
        if last_name:
            cur.execute("""
            UPDATE public."clients"
                SET last_name=%s
                WHERE id = %s;
            """, (last_name, client_id))
        if email:
            cur.execute("""
            UPDATE public."clients"
                SET first_name=%s
                WHERE id = %s;
            """, (email, client_id))
        conn.commit()

def delete_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT id from public."phone" WHERE phone_number=%s
        """, [phone])
        phone_id = cur.fetchone()[0]

        cur.execute("""
            DELETE FROM public."client_phone" WHERE client_id=%s and phone_id=%s;
        """, (client_id, phone_id))

        cur.execute("""
            DELETE FROM public."phone" WHERE id=%s;
        """, [phone_id])

        conn.commit()

def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT phone_id from public."client_phone" WHERE client_id=%s
        """, (client_id,))
        phone_ids = cur.fetchall()
        if phone_ids:
            for phone_id in phone_ids:
                cur.execute("""
                    DELETE FROM public."client_phone" WHERE client_id=%s and phone_id=%s;
                """,(client_id, phone_id))

                cur.execute("""
                    DELETE FROM public."phone" WHERE id=%s;
                """, [phone_id])

        cur.execute("""
            DELETE FROM public."clients" WHERE id=%s;
        """, [client_id])
        conn.commit()

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    with conn.cursor() as cur:
        if phone:
            cur.execute("""
                        SELECT id FROM public."phone" WHERE phone_number=%s;
                    """, [phone])
            phone_id = cur.fetchall()[0]

            cur.execute("""
                        SELECT client_id FROM public."client_phone" WHERE phone_id=%s;
                    """, [phone_id])
            client_phone_id = cur.fetchall()[0]

            cur.execute("""
                        SELECT * from public."clients" WHERE id=%s;
                    """, [client_phone_id])

            print(cur.fetchall())
            return
        else:
            cur.execute("""
                SELECT * FROM public."clients" WHERE first_name=%s OR last_name=%s OR email=%s;
            """, (first_name, last_name, email))
            print(cur.fetchall())
            return

if __name__ == "__main__":
    with psycopg2.connect(database="netology_db", user="postgres", password="postgres") as conn:
        create_db(conn)
        add_client(conn, 'Ivan', 'Ivanov', 'test@mail.ru')
        add_phone(conn, 1, "89122121282")
        change_client(conn, 1, first_name='Petr')
        delete_phone(conn, 1, "89122121282")
        delete_client(conn, 1)
        find_client(conn, email='test@mail.ru', phone=89122121282)
    conn.close()
