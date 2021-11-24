from django.shortcuts import render
from blog.models import Post

def home_page(request):
    post = Post.objects.filter(is_draft=False).order_by('-pub_date')[:3]
    context = {'post': post}
    return render(request, 'home.html', context)

def about_page(request):
    return render(request, 'about.html')

def service_page(request):
    return render(request, 'services.html')

#def contact_page(request):
#    return render(request, 'contact.html')



def contact_page(request):
	if request.method == 'POST':
		name = f"{request.POST.get('fname')} {request.POST.get('lname')}"
		email = request.POST.get('email')
		mob = request.POST.get('mob')
		mess = request.POST.get('mess','default')

		contact_page(name=name,email=email,mob=mob,mess=mess).save()
	return render(request, 'contact.html')




def web_dev(request):
    return render(request, 'web_dev2.html')    




def app_dev(request):
    return render(request, 'app_dev.html')        





def soc_med_mar(request):
    return render(request, 'soc_med_mar.html')    