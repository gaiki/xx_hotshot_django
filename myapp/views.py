from django.shortcuts import render, render_to_response
#import mysql.connector
from .models import XkomDane
import sys
import mysql

# Create your views here.
def index(request):
	return render_to_response('index.html', {'name':'dupa'})

	

def add(request):
	data = XkomDane.objects.all()
	naglowek = 'Historia promocji "gorący strzał"  X-KOM.PL'

	return render_to_response('result.html', {'gaz': data, 'tekst': naglowek})
	
	

