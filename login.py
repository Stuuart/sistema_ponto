//A alterar

#!/usr/bin/python3
IST_ID = 'istxxxxxx'
host = 'db.tecnico.ulisboa.pt'
port = 5432
password = ''
db_name = IST_ID
credentials = 'host={} port={} user={} password={} dbname={}'.format(host, port, IST_ID, password, db_name)
schema_path = 'set search_path = "{}"'.format('part3')
