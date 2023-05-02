#!/usr/bin/python3
IST_ID = 'ist196196'
host = 'db.tecnico.ulisboa.pt'
port = 5432
password = 'mypass1718'
db_name = IST_ID
credentials = 'host={} port={} user={} password={} dbname={}'.format(host, port, IST_ID, password, db_name)
schema_path = 'set search_path = "{}"'.format('ponto')
