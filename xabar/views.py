from django.shortcuts import render,redirect

from .models import Yangilik
from .forms import YangilikForm, UserForm


def register(request):
    register = UserForm()

    if request.POST:
        register = UserForm(request.POST)
        if register.is_valid():
            register.save()
            return redirect('uy')
    return render(request, 'register.html', {'register': register})



def all_newss(request):
    all_new = Yangilik.objects.all()
    print(request.GET.get('Qidiruv'))
    search = request.GET.get('Qidiruv')


    if search:
        all_new = Yangilik.objects.filter(sarlavha__contains=search)
    context = {
        'all_news':all_new
    }
    return render(request,'home.html',context)

def all_news(request):

    a={
        'all_news' : Yangilik.objects.all().order_by('sarlavha'),
        'all_news' : Yangilik.objects.all().order_by('-matn'),
        'all_news' : Yangilik.objects.all().order_by('-id'),
        
        "all_news" : Yangilik.objects.all()
        }
    return render(request,"home.html",a)

def news_create(request):
    form = YangilikForm()
    if request.POST:
        form = YangilikForm(request.POST,files=request.FIELS)
        if form.is_valid():
            form.save()
    return render(request,"create.html",{"form" : form})

   
    # if request.POST:
       
        
        # Yangilik.objects.create(
        #     sarlavha = request.POST.get('sarlavha'),
        #     matn = request.POST.get('matn'),
        #     rasm=request.FILES.get('rasm')
        # )
        # return redirect('uy')

        
    # return render(request,'create.html')
def edit(request, id):
    news = Yangilik.objects.get(id=id)


    if request.POST:
        sarlavha = request.POST['sarlavha']
        matn = request.POST['matn']
        news.sarlavha = sarlavha
        news.matn = matn
        news.save()
        return redirect('detail',news.id)
    return render(request, 'edit.html', {'edit_news':news})

def detail(request, a):
    one = Yangilik.objects.get(id=a)
    return render(request,'detail.html',{'one': one})