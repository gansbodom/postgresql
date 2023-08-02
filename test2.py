import psycopg2


client_id=2

with psycopg2.connect(database="netology_db", user="postgres", password="postgres") as conn:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT phone_id from public."client_phone" WHERE client_id=%s
        """, (client_id,))
        phone_id = cur.fetchall()
        #phone_id = cur.fetchone()[0]
        print(phone_id)

for i in phone_id:
    print(i)