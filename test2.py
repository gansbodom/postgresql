import psycopg2

client_id=1
phone=89122121282

with psycopg2.connect(database="netology_db", user="postgres", password="postgres") as conn:
    with conn.cursor() as cur:
        #cur.execute("""
        #     SELECT * FROM public."clients" WHERE first_name='Ivan' OR last_name='Ivanov' OR email='test@mail.ru';
        # """)

        cur.execute("""
            SELECT id FROM public."phone" WHERE phone_number=%s;
        """, [phone])
        phone_id = cur.fetchall()[0]
        print(f' phone_id {phone_id}')
        cur.execute("""
            SELECT client_id FROM public."client_phone" WHERE phone_id=%s;
        """, [phone_id])
        client_phone_id = cur.fetchall()[0]

        cur.execute("""
            SELECT * from public."clients" WHERE id=%s;
        """, [client_phone_id])

        print(cur.fetchall())