from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title><h1>To-Do</h1><input id="id_new_item" placeholder="Enter a to-do item"></html>')
