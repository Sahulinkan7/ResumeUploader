from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.base import TemplateView
from .forms import ResumeForm
from .models import Resume
from django.contrib import messages
# Create your views here.

class ResumeView(View):
    def get(self,request):
        form=ResumeForm()
        candidates=Resume.objects.all()
        return render(request,"resume/home.html",{'form':form,'candidates':candidates})
    
    def post(self,request):
        form=ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data['name'])
            form.save()
            messages.success(request,"Data saved Successfully ! ")
            form=ResumeForm()
            candidates=Resume.objects.all()
            return render(request,"resume/home.html",{'form':form,'candidates':candidates})
        candidates=Resume.objects.all()
        return render(request,"resume/home.html",{'form':form,'candidates':candidates})
    
class CandidateView(View):
    def get(self,request,pk):
        candidate=Resume.objects.get(pk=pk)
        return render(request,"resume/profile.html",{'candidate':candidate})