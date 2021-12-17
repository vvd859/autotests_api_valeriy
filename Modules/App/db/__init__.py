import psycopg2

conn = psycopg2.connect(
    host="db",
    dbname="nvgr",
    user="vvd",
    password="qweasdzxc")
conn.set_client_encoding('UTF8')