import requests
import json
class main:
	"""docstring for main"""
	def __init__(self):
		self.url='http://127.0.0.1'
		self.port='8083'
		self.uri='api'
		self.endpoints=dict(
			book=f'{self.url}:{self.port}/{self.uri}/book', #All or Create, si es all=get si es create=post
			get_book='{}:{}/{}/book/'.format(self.url,self.port,self.uri),#Get Book(get) or Edit Book(put) or Delete book(delete) 
			comment=f'{self.url}:{self.port}/{self.uri}/comments',
			get_comment='{}:{}/{}/comments/'.format(self.url,self.port,self.uri),
			get_token=f'{self.url}:{self.port}/{self.uri}/v2/login'.format()
			)
		self.username='jesus'
		self.password='1234567890..'
		self.token=None
		print('Connection.....')
		
		print('------------\nGetToken\n------------\n')
		self.get_token()
		print('\n------------------------------------')

		print('------------\nAllBook\n------------\n')
		self.all_book()
		print('\n------------------------------------')
		
		print('------------\nCreateBook\n------------\n')
		self.create_book()
		self.create_book()
		print('\n------------------------------------')
		
		print('------------\nEditBook\n------------\n')
		self.edit_book(pk=1)
		print('\n------------------------------------')
		
		print('------------\nDeleteBook\n------------\n')
		self.delete_book(pk=1)
		print('\n------------------------------------')
		
		print('------------\nAllCommets\n------------\n')
		self.all_comment()
		print('\n------------------------------------')

		print('------------\nCreateCommets\n------------\n')
		self.create_comment(pk_book=2)
		self.create_comment(pk_book=2)
		print('\n------------------------------------')
		
		print('------------\nEditCommets\n------------\n')
		self.edit_comment(pk=1,pk_book=2)
		print('\n------------------------------------')
		
		print('------------\nDeleteCommets\n------------\n')
		self.delete_comment(pk=2)
		print('\n------------------------------------')
		
		
	#Este metodo devuelve un toke de auth
	def get_token(self):
		body={
			'username':self.username,
			'password':self.password,
		}
		try:
			if self.token==None:
				response=requests.post(self.endpoints['get_token'],body)
				if response.status_code == 200:
					print(response.json())
					self.token=response.json()
					return self.token
			else:
				# print(self.token)
				return self.token
		except Exception as e:
			print(e)
	

	#Este metodo muestra todos los libros creados
	def all_book(self):
		try:
			header={'Authorization':'Token {}'.format(self.get_token())}
			response=requests.get(self.endpoints['book'],headers=header)
			if response.status_code == 200:
				print(response.json())
		except Exception as e:
			print(e)

	#Este metodo crea libros
	def create_book(self):
		body={
			'title':'Titulo del libro a crear',
			'publication_date':'2021-10-10'
		}
		try:
			header={'Authorization':'Token {}'.format(self.get_token())}
			response=requests.post(self.endpoints['book'],body,headers=header)
			if response.status_code == 200:
				print(response.json())
		except Exception as e:
			print(e)

	def edit_book(self,pk):
		body={
			'title':'Titulo del libro a editar',
			'publication_date':'2020-10-11'
		}
		try:
			header={'Authorization':'Token {}'.format(self.get_token())}
			url='{}/{}'.format(self.endpoints['book'],pk)
			response=requests.put(url,body,headers=header)
			if response.status_code == 200:
				print(response.json())
		except Exception as e:
			print(e)

	def delete_book(self,pk):
		try:
			header={'Authorization':'Token {}'.format(self.get_token())}
			url='{}/{}'.format(self.endpoints['book'],pk)
			response=requests.delete(url,headers=header)
			if response.status_code == 200:
				print(response.json())
		except Exception as e:
			print(e)

	#Este metodo muestra todos los comentarios creados
	def all_comment(self):
		try:
			header={'Authorization':'Token {}'.format(self.get_token())}
			response=requests.get(self.endpoints['comment'],headers=header)
			if response.status_code == 200:
				print(response.json())
		except Exception as e:
			print(e)

	#Este metodo crea libros
	def create_comment(self,pk_book):
		body={
			'text':'Comentario',
			'books':pk_book
		}
		try:
			header={'Authorization':'Token {}'.format(self.get_token())}
			response=requests.post(self.endpoints['comment'],body,headers=header)
			if response.status_code == 200:
				print(response.json())
		except Exception as e:
			print(e)

	def edit_comment(self,pk,pk_book):
		body={
			'text':'Editar Comentario',
			'books':pk_book
		}
		try:
			header={'Authorization':'Token {}'.format(self.get_token())}
			url='{}/{}'.format(self.endpoints['comment'],pk)
			response=requests.put(url,body,headers=header)
			if response.status_code == 200:
				print(response.json())
		except Exception as e:
			print(e)

	def delete_comment(self,pk):
		try:
			header={'Authorization':'Token {}'.format(self.get_token())}
			url='{}/{}'.format(self.endpoints['comment'],pk)
			response=requests.delete(url,headers=header)
			if response.status_code == 200:
				print(response.json())
		except Exception as e:
			print(e)



main()