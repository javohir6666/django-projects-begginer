from django.shortcuts import render
from .models import Editor
from .forms import EditorForm

def homeView(request):
    form=EditorForm()
    return render(request,'texteditorapp/index.html',{'form':form})