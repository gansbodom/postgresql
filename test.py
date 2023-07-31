import psycopg2

# def select_phone_id(conn, phone):
#     with conn.cursor() as cur:
#         cur.execute("""
#         SELECT id from public."phone" WHERE phone_number=%s
#         """, [phone])
#         phone_i = cur.fetchone()[0]
#         print(type(phone_i))
#         return

def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO public."phone" (id, phone_number) VALUES
            (%s) """, (phone))
        conn.commit()

        cur.execute("""
        SELECT id from public."phone" WHERE phone_number=%s
        """, [phone])
        phone_id = cur.fetchone()[0]

        cur.execute("""
            INSERT INTO public."client_phone" (client_id, phone_id) VALUES
            (%s, %s) """, (client_id, phone_id))
        conn.commit()
    pass



with psycopg2.connect(database="netology_db", user="postgres", password="postgres") as conn:
    add_phone(conn, 1, 89122121282)