# Prueba
<p align="center">
  Prueba de crear una apiRest con los modelos book y comments, cada uno con su crud, y creae un script que esta en el archivo conexion.py que ya hace la simulacion de cosumir la api rest. En la creacion de la apiRest utilice Django
</p>

# INSTALACIÓN
```bash
$ pip3 instal -r requerements.txt
```
# Configurar el archivo settings.py

# Migrar DB
```bash
$ python3 manage.py makemigrations && python3 manage.py migrate
```
# CrearSuperUser
```bash
$ python3 manage.py createsuperuser
```
# Levantar apiRest
```bash
$ python3 manage.py runserver
```
# Correr Conexion.py
```bash
$ python3 conexion.py
```
# Archivo Conexion.py
<p align="center">
	ojo ese archivo, posee la conexion a todos los endpoints de la apirest, lo unico que tiene que colocar la direcion localhost de donde va a levantar la aplicacion y el port en donde esta la apirest, colocar el usuario y la password que creo, y lo puede correr sin ningun tipo de errores
</p>

# EndPoints

##GetToken
<ul>
	<li>
		<p>endpoints: GET 127.0.0.1:8000/api/v2</p>
		<p>Data: <br>username='username', password='pass' </p>
		<p>retorna: '12312312n3in12j3bn123hb'</p>
	</li>
</ul>

##Books
<ul>
	<li>
		<p>All</p>
		<p>endpoints: GET 127.0.0.1:8000/api/book</p>
		<p>Header: <br>headers='Authorization: Token GenerarToken'</p>
		<p>retorna: archivo.xlsx</p>
	</li>
	<li>
		<p>Get only book</p>
		<p>endpoints: GET 127.0.0.1:8000/api/book/1 </p>
		<p>Header: <br>headers='Authorization: Token GenerarToken'</p>
		<p>retorna: archivo.xlsx</p>
	</li>
	<li>
		<p>Crear</p>
		<p>endpoints: POST 127.0.0.1:8000/api/book</p>
		<p>Data: <br>title='title', publication_date='YY-MM-DD'</p>
		<p>Header: <br>headers='Authorization: Token GenerarToken'</p>
		<p>retorna: archivo.xlsx</p>
	</li>
	<li>
		<p>Update</p>
		<p>endpoints: PUT 127.0.0.1:8000/api/book/1</p>
		<p>Data: <br>title='title', publication_date='YY-MM-DD'</p>
		<p>Header: <br>headers='Authorization: Token GenerarToken'</p>
		<p>retorna: archivo.xlsx</p>
	</li>
	<li>
		<p>DELETE</p>
		<p>endpoints: DELETE 127.0.0.1:8000/api/book/1</p>
		<p>Header: <br>headers='Authorization: Token GenerarToken'</p>
		<p>retorna: {'message':'Book Deleted Successfully'}</p>
	</li>
</ul>

##Comments
<ul>
	<li>
		<p>ALL</p>
		<p>endpoint: GET 127.0.0.1:8000/api/comments</p>
		<p>Header: <br>headers='Authorization: Token GenerarToken'</p>
		<p>retorna: archivo.xlsx</p>
	</li>
	<li>
		<p>Get only Comments</p>
		<p>endpoint: GET 127.0.0.1:8000/api/comments/1</p>
		<p>Header: <br>headers='Authorization: Token GenerarToken'</p>
		<p>retorna: archivo.xlsx</p>
	</li>
	<li>
		<p>Create</p>
		<p>endpoint: POST 127.0.0.1:8000/api/comments</p>
		<p>Header: <br>headers='Authorization: Token GenerarToken'</p>
		<p>Data: 'text'='Comentario', 'books'=2</p>
		<p>retorna: archivo.xlsx</p>
	</li>
	<li>
		<p>Update</p>
		<p>endpoint: PUT 127.0.0.1:8000/api/comments/1</p>
		<p>Header: <br>headers='Authorization: Token GenerarToken'</p>
		<p>Data: 'text'='Comentario', 'books'=2</p>
		<p>retorna: archivo.xlsx</p>
	</li>
	<li>
		<p>DELETE</p>
		<p>endpoint: 127.0.0.1:8000/api/comments/1</p>
		<p>Header: <br>headers='Authorization: Token GenerarToken'</p>
		<p>retorna: archivo.xlsx</p>
	</li>
</ul>
