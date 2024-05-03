from django.shortcuts import render

from django.http import HttpResponse #ประกาศดึง ฟังชั้น มาใช้งาน,

from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def home2(request):
    return render(request, 'Page2.html')

def home3(request):
    return render(request, 'Page3.html')

def home4(request):
    return render(request, 'Page4.html')




#def hello(request):
#   return HttpResponse('Hello World') # เอาข้อความคำว่า Hello ไปเก็บในตัวแปร hello 

#def hello(request, id):
    #return HttpResponse('Hello World ID=' + str(id)) # ที่ต้องบวก str เพราะ  int ไม่สามารถรวมกับ str  

def detail(request):
    id = '001'
    name = 'Ronachai'
    email = 'sddfsds@gmail.com'
    return render(request, 'index.html', {

    'id':id,
    'name':name,
    'email':email,

    })




    return render(request, 'Index.html')

