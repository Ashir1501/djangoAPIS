import json
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .forms import ValidateForm, JokesCountForm, GreetingsForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import requests
# Create your views here.
class Dashboard(View):
    def get(self,request):
        form = GreetingsForm()
        return render(request,'home.html',{'form':form})

class Greetings(View):
    def get(self, request, *args, **kwargs):
        form = GreetingsForm(request.GET)
        if form.is_valid():
            return JsonResponse(form.cleaned_data)
        else:
            return JsonResponse({'errors':form.errors},status=404)

# @method_decorator(csrf_exempt, name='dispatch')
class ValidateAPI(View):
    def get(self,request):
        form= ValidateForm()
        return render(request,'validatePage.html',{'form':form})
    
    def post(self,request):
        form = ValidateForm(request.POST)
        if form.is_valid():
            return JsonResponse(form.cleaned_data)
        else:
            return JsonResponse({'errors': form.errors}, status=404)
            
    
# @method_decorator(csrf_exempt, name='dispatch')
class JokesAPI(View):
    def get(self,request):
        form = JokesCountForm()
        return render(request,'jokesPage.html',{'form':form})
    
    def post(self,request):
        # limit parameter is only for premium subscribers
        count = int(request.POST.get('count'))
        #url for premium users
        # api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(count)
        #non-premium users can use the below url
        api_url = 'https://api.api-ninjas.com/v1/jokes?'
        response = requests.get(api_url, headers={'X-Api-Key': 'Y7dFXMfYJEDyswnZCts1Eg==McevFlJBTXrsbUCd'})

        if response.status_code == requests.codes.ok:
            return JsonResponse(response.json(),safe=False)
        else:
            try:
                error_response = json.loads(response.text)
                error_message = error_response.get('error')
            except json.JSONDecodeError:
                error_message = 'An unknown error occurred.'
            return JsonResponse({'errors': error_message}, status=404)

