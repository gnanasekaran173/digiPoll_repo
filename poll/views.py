from django.forms.forms import Form
from django.shortcuts import redirect, render,HttpResponse
from django.template import loader
from django.template import loader
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse

from .forms import CreatePollForm
from .models import Poll 

def home(request):
    polls=Poll.objects.all()
    context={
        'Polls': polls
    }
    return render(request,'home.html',context)

@csrf_exempt
def create(request):
    if request.method=='POST':
        form=CreatePollForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data['question'])
            form.save()
            return redirect(home)
    else:
        form= CreatePollForm()
    context={
        'form': form

    }
    return render(request,'create.html',context)

@csrf_exempt
def vote(request,poll_id):
    poll= Poll.objects.get(pk=poll_id)
    if request.method=='POST':
        selected_option=request.POST['poll']
        if selected_option=='option1':
            poll.option_one_count += 1
        elif selected_option=='option2':
            poll.option_two_count += 1 
        elif selected_option=='option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')
        
        poll.save()
        return redirect('results',poll.id)          

    context={
        'Poll' : poll
    }
    return render(request,'vote.html',context)

def results(request,poll_id):
    poll= Poll.objects.get(pk=poll_id)
    context={
        'Poll' : poll
    }
    return render(request,'results.html',context)

#def delete(request,poll_id):
#    poll= Poll.objects.filter(id=poll_id).delete()
#    context={
#        'Poll' : poll
#    }
#    return render(request,'home.html',context)
    

