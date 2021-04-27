from django.shortcuts import render, redirect 
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Contact, PlasmaDonorForm, Oxygen, Bed, Plasma, Medicine, Helpline, Other

def home(request):
    if request.method =='POST':
        Name = request.POST.get('name')  
        Message = request.POST.get('message')
        Subject = request.POST.get('subject') 
        Email = request.POST.get('email')
        contact = Contact(name=Name, message=Message, subject=Subject, email=Email)
        contact.save()
        messages.success(request,'Message received! Thank you for contacting us.')
        return redirect ('home')
    return render(request,'index.html')

def donate_plasma(request):
    if request.method =='POST':
        try:
            Name = request.POST.get('name')  
            Age = request.POST.get('age')
            Email = request.POST.get('email')
            Contact = request.POST.get('contact')
            BloodGroup = request.POST.get('bloodGroup')
            Address = request.POST.get('address')
            City = request.POST.get('city')
            Date = request.POST.get('date')
            PrevDonation = request.POST.get('prevDonation')
            Antibodies = request.POST.get('antibodies')
            MedIssues = request.POST.get('medIssues')
            cntc = PlasmaDonorForm.objects.filter(contact = Contact)
            if (len(cntc)):
                messages.error(request,"This entry already exists.")
                return redirect ('donate_plasma')
            plasmaDonorForm = PlasmaDonorForm(name=Name, age= Age, email=Email, contact= Contact, bloodGroup = BloodGroup, address= Address, city=City, date= Date, prevDonation = PrevDonation, antibodies = Antibodies, medIssues = MedIssues)
            plasmaDonorForm.save()
            messages.success(request,'Details Received! We will contact you soon.')
            return redirect ('home')
        except:
            messages.error(request,"Error Occured! Kindly contact the team.")
            return redirect ('home')
    return render(request,'donor.html')  

def loc(request,the_slug):
    if(the_slug == "Beds"):
        locs = Bed.objects.order_by().values('city').distinct()
        print(locs)
        context={'locs':locs, 'val':'Beds'}
    if(the_slug == "Oxygen"):
        locs = Oxygen.objects.order_by().values('city').distinct()
        print(locs)
        context={'locs':locs, 'val':'Oxygen'}
    if(the_slug == "Plasma"):
        locs = Plasma.objects.order_by().values('city').distinct()
        print(locs)
        context={'locs':locs, 'val':'Plasma'}
    if(the_slug == "Medicines"):
        locs = Medicine.objects.order_by().values('city').distinct()
        print(locs)
        context={'locs':locs, 'val':'Medicines'}
    return render(request,'locations.html', context)   
    

def oxygen(request, the_slug):
    oxygens = Oxygen.objects.order_by('-currDate').filter(city=the_slug, verified= True)
    notoxygens = Oxygen.objects.order_by('-currDate').filter(city=the_slug, verified= False)
    context= {'oxygens':oxygens, 'notoxygens': notoxygens, 'city': the_slug}
    return render(request,'oxygen.html', context)      

def bed(request, the_slug):
    beds = Bed.objects.order_by('-currDate').filter(city=the_slug, verified= True)
    notbeds = Bed.objects.order_by('-currDate').filter(city=the_slug, verified= False)
    context= {'beds':beds, 'notbeds': notbeds, 'city': the_slug}
    return render(request,'bed.html', context)  

def plasma(request, the_slug):
    plasmas = Plasma.objects.order_by('-currDate').filter(city=the_slug, verified= True)
    notplasmas = Plasma.objects.order_by('-currDate').filter(city=the_slug, verified= False)
    context= {'plasmas':plasmas, 'notplasmas': notplasmas, 'city': the_slug}
    return render(request,'plasma.html', context)  

def medicine(request, the_slug):
    medicines = Medicine.objects.order_by('-currDate').filter(city=the_slug, verified= True)
    notmedicines = Medicine.objects.order_by('-currDate').filter(city=the_slug, verified= False)
    context= {'medicines':medicines, 'notmedicines': notmedicines, 'city': the_slug}
    return render(request,'medicine.html', context)  

def helplines(request):
    helplines = Helpline.objects.order_by('state').filter()
    context={'helplines' : helplines}
    return render(request,'helplines.html', context)  

def others(request):
    ots = Other.objects.order_by('-currDate').filter(active=True)[:7]
    context = {'ots':ots}
    print(context)
    return render(request,'others.html', context)                           