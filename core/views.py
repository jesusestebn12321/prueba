from django.http.response import Http404
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from core.models import *
from core.serializers import BookSerializer, CommentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status

import xlsxwriter
import json
from pdb import set_trace
# Create your views here.

@api_view(['POST'])
def get_token(request):
	username=request.POST.get('username')
	password=request.POST.get('password')
	try:
		user=User.objects.get(username=username)
	except User.DoesNotExist:
		return Response('Error')
	pwd_valid=check_password(password,user.password)
	if not pwd_valid:
		return Response('Error')
	token, _ = Token.objects.get_or_create(user=user)	
	return Response(token.key)


class BookAPIView(APIView):
	permission_classes= [IsAuthenticated]
	def get_object(self, pk):
		try:
		    return Book.objects.get(id=pk)
		except Book.DoesNotExist:
		    return Response('Error book do es not exist.')

	def get(self, request, pk=None, format=None):
		if pk:
			data = self.get_object(pk)
			serializer = BookSerializer(data)
		else:
			data = Book.objects.all()
			serializer = BookSerializer(data, many=True)
		with xlsxwriter.Workbook('AllBook.xlsx') as fil:
			worksheet= fil.add_worksheet()
			worksheet.write(0,0,'ID')
			worksheet.write(0,1,'Title')
			worksheet.write(0,2,'Date')
			i=1
			for x in serializer.data:
				worksheet.write(i, 0, x.get('id'))
				worksheet.write(i, 1, x.get('title'))
				worksheet.write(i, 2, x.get('publication_date'))
				i=i+1
		return Response(serializer.data)

	def post(self, request, format=None):
		data = request.data
		serializer = BookSerializer(data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		
		response = Response()
		response.data = {
		    'message': 'Book Created Successfully',
		    'data': serializer.data
		}
		return response

	def put(self, request, pk=None, format=None):
	    book_to_update = Book.objects.get(pk=pk)
	    serializer = BookSerializer(instance=book_to_update,data=request.data, partial=True)
	    serializer.is_valid(raise_exception=True)
	    # set_trace()
	    serializer.save()
	    response = Response()
	    response.data = {
	        'message': 'Book Updated Successfully',
	        'data': serializer.data
	    }
	    return response

	def delete(self, request, pk, format=None):
	    book_to_delete =  Book.objects.get(pk=pk)
	    book_to_delete.delete()
	    return Response({
	        'message': 'Book Deleted Successfully'
	    })

class CommentAPIView(APIView):
	permission_classes= [IsAuthenticated]
	def get_object(self, pk):
		try:
		    return Comment.objects.get(id=pk)
		except comment.DoesNotExist:
		    return Response('Error comment do es not exist')

	def get(self, request, pk=None, format=None):
		if pk:
			data = self.get_object(pk)
			serializer = CommentSerializer(data)
		else:
			data = Comment.objects.all()
			serializer = CommentSerializer(data, many=True)

		with xlsxwriter.Workbook('AllComment.xlsx') as fil:
			worksheet= fil.add_worksheet()
			worksheet.write(0,0,'ID')
			worksheet.write(0,1,'Text')
			worksheet.write(0,2,'Book')
			worksheet.write(0,3,'User')
			i=1
			for x in serializer.data:
				worksheet.write(i, 0, x.get('id'))
				worksheet.write(i, 1, x.get('text'))	
				if x.get('books'):
					worksheet.write(i, 2, 'id:{} - title:{}'.format(Book.objects.get(id=x.get('books')).id,Book.objects.get(id=x.get('books')).title))
				else:
					worksheet.write(i, 2, 'NONE')
				if x.get('user'):
					worksheet.write(i, 3, 'id:{} - Username:{}'.format(User.objects.get(id=x.get('user')).id,User.objects.get(id=x.get('user')).username))
				else:
					worksheet.write(i, 3, 'None')
				i=i+1

		return Response(serializer.data)

	def post(self, request, format=None):
		token=request.headers.get('Authorization').split(' ')[1]
		user = request.user.pk
		data = request.data
		data_end=data.dict()
		data_end['user']=user
		serializer = CommentSerializer(data=data_end)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		response = Response()
		response.data = {
		    'message': 'Comment Created Successfully',
		    'data': serializer.data
		}
		return response

	def put(self, request, pk=None, format=None):
	    comment_to_update = Comment.objects.get(pk=pk)
	    user = request.user.pk
	    data = request.data
	    data_end=data.dict()
	    data_end['user']=user
	    serializer = CommentSerializer(instance=comment_to_update,data=data_end, partial=True)
	    serializer.is_valid(raise_exception=True)
	    serializer.save()
	    response = Response()
	    response.data = {
	        'message': 'Comment Updated Successfully',
	        'data': serializer.data
	    }
	    return response

	def delete(self, request, pk, format=None):
	    comment_to_delete =  comment.objects.get(pk=pk)
	    comment_to_delete.delete()
	    return Response({
	        'message': 'Comment Deleted Successfully'
	    })
		