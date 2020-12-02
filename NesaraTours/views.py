from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .filters import EmployeeFilter,TourFilter,ClientFilter

# Create your views here.
from django.shortcuts import redirect, render
from . models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.
def TourDetails(request,pk):
    TD = Tour.objects.all().filter(id=pk)
    context={
        'TD':TD
    }
    return render(request,'tourdetails.html',context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Home')
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('Home')
            else:
                messages.info(request,'Incorrect Username or Password ')
                return render(request,'login.html')

    return render(request,'login.html')
        
        
def logoutUser(request):
    logout(request)
    return redirect('login')
    
        
def Home(request):
    pck = Package.objects.all()
    context = {'package':pck,}
    return render(request,'Home.html',context)

def Packages(request):
    pck = Package.objects.all()
    context={'package':pck}
    return render(request, 'packages.html', context)
    
def ViewPackage(request, pk):
    ViewPack = Package.objects.get(id=pk)
    context = {
        'VP': ViewPack
    }
    return render(request,'ViewPackage.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Employee','Manager'])
def Cust(request):
    # emp=Employee.objects.all()
    client=Client.objects.all()
    TotalClients = client.count()
    ActiveClients = client.filter(Status="Active").count()
    NotVerifiedClients = client.filter(Status="Not verified").count()
    NotV=client.filter(Status="Not verified")
    myFilter = ClientFilter(request.GET, queryset=client)
    Act=client.filter(Status="Active")
    client = myFilter.qs

    
    context={
        'TotalClients':TotalClients,
        'ActiveClients':ActiveClients,
        'NotVerifiedClients':NotVerifiedClients,
        'NotV':NotV,
        'Act':Act,
        'myFilter':myFilter,
        'client': client
    }
    return render(request, 'cust.html', context)
    
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager'])

def EMp(request):
    EMP = Employee.objects.all()
    TotalEmp = EMP.count()
    myFilter = EmployeeFilter(request.GET, queryset=EMP)
    EMP = myFilter.qs
    
    context={
        'Employee': EMP,
        'TotalEmployee': TotalEmp,
        'myFilter' : myFilter 
        
    }
    return render(request,'employee.html',context)
    


@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager'])

def emp(request,Pk):
    EMP=Employee.objects.get(id=Pk)
    context={
        'Employee':EMP
    }
    return render(request,'Emp.html',context)
 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Employee','Manager'])

def branch(request):
    branch = Branch.objects.all()
    context = {
        'branch':branch 
    }
    return render(request,'Branch.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Employee','Manager'])

def BRANCH(request,pk):
    branch = Branch.objects.get(id=pk)
    emp = Employee.objects.all()
    tour= Tour.objects.all()
    ListEmp = emp.filter(branch_id=pk)
    TotalEmp = ListEmp.count()
    ListTour = tour.filter(Branch_id=pk)
    TotalTour = ListTour.count()


    



    context = {
        'branch':branch,
        'List' : ListEmp,
        'Total' : TotalEmp,
        'ListTour':ListTour,
        'TotalTour':TotalTour,
        
    }
    return render(request,'BRANCH2.html',context)

def Tours(request):
    tourdetails = Tour.objects.all()
    TotalTours = tourdetails.count()
    Completed = tourdetails.filter(Status='Complete').count()
    NotCompleted = tourdetails.filter(Status='Not complete').count()
    Ongoing = tourdetails.filter(Status='Ongoing').count()
    Filter = TourFilter(request.GET, queryset=tourdetails)
    tourdetails = Filter.qs
    
    
    context = {
        
        'TD': tourdetails,
        'TotalTours': TotalTours,
        'Completed': Completed,
        'NotCompleted': NotCompleted,
        'Ongoing': Ongoing,
        'myFilter': Filter,
        
    }

    return render(request, 'tours.html', context)


    



def renderToPdf(template_src, context_dict=[]):
    tour = Tour.objects.all()
    client = Client.objects.all()
    Total = client.count()
    TotalTours = tour.count()
    emp = Employee.objects.all()
    TotalEmp = emp.count()
    branch = Branch.objects.all()
    branch = branch.count()
    
    
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='applcation/pdf')
    return None

data = {
    "Tour": Tour.objects.all(),
    "Client": Client.objects.all(),
    "Emp": Employee.objects.all(),
    "Branch":Branch.objects.all(),
    "TotalTours": Tour.objects.all().count(),
    "TotalBranch": Branch.objects.all().count(),
    "TotalClient": Client.objects.all().count(),
    "TotalEmployees": Employee.objects.all().count(),
        
         
    }


class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = renderToPdf('pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

#Automatically downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = renderToPdf('pdf_template.html',data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Report_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response

@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager'])
def Report(request):

    return render(request, 'report.html')

# def viewTours(template_src, context_dict=[]):
#         tour = Tour.objects.all()
#     client = Client.objects.all()
#     Total = client.count()
#     TotalTours = tour.count()
#     emp = Employee.objects.all()
#     TotalEmp = emp.count()
#     branch = Branch.objects.all()
#     branch = branch.count()
    
    
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='applcation/pdf')
#     return None

# data = {
#     "Tour": Tour.objects.all(),
#     "Client": Client.objects.all(),
#     "Emp": Employee.objects.all(),
#     "Branch":Branch.objects.all(),
#     "TotalTours": Tour.objects.all().count(),
#     "TotalBranch": Branch.objects.all().count(),
#     "TotalClient": Client.objects.all().count(),
#     "TotalEmployees": Employee.objects.all().count(),
        
         
#     }

