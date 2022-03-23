from django.shortcuts import redirect, render,HttpResponse
from home.models import Contact,Author
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,login,logout
# Create your views here.

def home(request):
    post=Post.objects.filter(author='AR Rony').first()
    context = {'post':post}
    return render(request,'home/home.html',context)

def contact(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']

        if len(name)<3 or len(email)<4 or len(phone)<4 or len(content)<5:
            messages.error(request,"Enter your data correctly")
        else: 
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"Your message has been successfully sent")

    return render(request,'home/contact.html')

def about(request):
    allauthors=Author.objects.all()
    params={'allauthors':allauthors}
    return render(request,'home/about.html',params)

def search(request):
    query=request.GET['query']
    if len(query)>50:
        allposts=Post.objects.none()
    else:
        allpostsTitle = Post.objects.filter(title__icontains=query)
        allpostsContent = Post.objects.filter(content__icontains=query)
        allpostsAuthor=Post.objects.filter(author__icontains=query)
        allposts=allpostsTitle.union(allpostsContent,allpostsAuthor)
    if allposts.count()==0:
        messages.warning(request,"No search result found")
    params={'allposts':allposts,'query':query}
    return render(request,'home/search.html',params)

def handleSignup(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        password1=request.POST['password1']
        password2=request.POST['password2']

        # check for errorneous input
        if len(username)<10:
            messages.error(request,"Username must be less then 10 words")
            redirect('home')
        if (password1 != password2):
            messages.error(request,"Password do not match")
            redirect('home')
        if not username.isalnum():
            messages.error(request,"username contains only alphabets and numbers")
            redirect('home')
        #username.isalnum(): We are allowing only alphanumeric username. Here, we are using the isalnum() function of python to make sure that the username contains only alphabets and numbers.

        #create the user
        myuser=User.objects.create_user(username,email,password1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your saveNature account has been successfully created")
        return redirect('home')
    else:
        return HttpResponse("404 - Not found")

def handleLogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials! please try again")
            return redirect('home')
    return HttpResponse("404- Not found")

def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect('home')