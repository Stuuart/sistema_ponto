#!/usr/bin/python3
import psycopg2
import login
print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Entradas</title>')
print('</head>')
print('<body>')
print('<h3>Entradas</h3>')
connection = None
try:
	# Creating connection
	connection = psycopg2.connect(login.credentials)
	cursor = connection.cursor()
	cursor.execute(login.schema_path)
	print(
		"""
		<table cellspacing="5">
			<tr>
				<td>
					<form action="create_sailor.cgi" method="post">
					<p><input type="submit" value="Ver Attendance"/></p>
					</form>
				</td>
				<td>
					<form action="home.html" method="post">
					<p><input type="submit" value="Home"/></p>
					</form>
				</td>
			</tr>
		</table>
		""")
	# Making query

	sql = """
		SELECT * FROM punching;
		"""
	cursor.execute(sql)
	result = cursor.fetchall()
	num = len(result)

	# Displaying results
	print('<table border="5" cellspacing="5">')
	print('<tr><td><b>Card</b></td><td><b>Time</b></td><td><b>In/Out</b></td></tr>')
	for row in result:
		print('<tr>')
		for value in row:
			# The string has the {}, the variables inside format() will replace the {}
			print('<td>{}</td>'.format(value))
		print('<td><a href="remove_sailor.cgi?name={}&email={}&type={}">Remove</a></td>'.format(row[0], row[2], row[1]))
		print('</tr>')
	print('</table>')

	# Closing connection
	cursor.close()

except Exception as e:
	# Print errors on the webpage if they occur
	print('<h1>An error occurred.</h1>')
	print('<p>{}</p>'.format(e))

finally:
	if connection is not None:
		connection.close()
print('</body>')
print('</html>')