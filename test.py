import psycopg2

def add_client(conn, first_name, last_name, email, phones=None):
    with conn.cursor() as cur:
        cur.execute ("""
        INSERT INTO public."clients" (first_name, last_name, email) VALUES
        (%s, %s, %s), ON CONFLICT (email) DO NOTHING;
        """, (first_name, last_name, email))
        cur.execute ("""
        INSERT INTO public."phone" (phone_number) VALUES
        (%s);
        """, (phones))
        cur.execute("""
        INSERT INTO public."client_phone" (client_id, number_id)
        """)
        #conn.commit()
        #print(cur.fetchall())


with psycopg2.connect(database="netology_db", user="postgres", password="postgres") as conn:
    add_client(conn, first_name='Сидор', last_name='Пидорович', email='zaebalsya@mail.ru', phones='123456789')
    conn.close()