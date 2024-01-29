from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Bookstore
from .form import MemberForm

def book(request):
  book_list= Bookstore.objects.all().values()
  context ={
    'book_list':book_list
  }
  template = loader.get_template('book.html')
  return HttpResponse(template.render(context,request))

def detail(request,id):
  mybook= Bookstore.objects.get(id=id)
  template=loader.get_template('detail.html')
  context={
    'mybook':mybook
  }
  return HttpResponse(template.render(context,request))

@csrf_exempt
def add_newbook(request):
  if request.method =='POST':
    bookname = request.POST.get('bookname',)
    description = request.POST.get('description',)
    price = request.POST.get('price',)
    available = request.POST.get('available',)
    image = request.FILES['image']
    bookstore=Bookstore(bookname=bookname,description=description,price=price,available=available,image=image)
    bookstore.save()
  template = loader.get_template('add_newbook.html')
  return HttpResponse(template.render())

@csrf_exempt
def delete(request,id):
  if request.method == 'POST':
    mybook =Bookstore.objects.get(id=id)
    mybook.delete()
    t1= loader.get_template('book.html')
    return HttpResponse(t1.render())
  return render(request,'delete.html')

def update(request,id):
  mybook= Bookstore.objects.get(id=id)
  form = MemberForm(request.POST,instance=mybook)
  if form.is_valid():
    form.save()
    t1= loader.get_template('add_newbook.html')
    return HttpResponse(t1.render())
  return render(request,'update.html',{'form':form,'mybook':mybook})

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
