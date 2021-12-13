import psycopg2

tconn = psycopg2.connect(
    host="172.17.0.3",
    database="syslog",
    user="vvd1",
    password="qweasdzxc")