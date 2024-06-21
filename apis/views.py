from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .forms import ValidateForm, JokesCountForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import requests
# Create your views here.

class Greetings(View):
    def get(self, request, *args, **kwargs):
        name = kwargs.get('name')
    
        return JsonResponse({'name':name})

@method_decorator(csrf_exempt, name='dispatch')
class ValidateAPI(View):
    def get(self,request):
        f= ValidateForm()
        return render(request,'validatePage.html',{'form':f})
    
    def post(self,request):
        form = ValidateForm(request.POST)
        if form.is_valid():
            return JsonResponse(form.cleaned_data)
            
    
@method_decorator(csrf_exempt, name='dispatch')
class JokesAPI(View):
    def get(self,request):
        f = JokesCountForm()
        return render(request,'jokesPage.html',{'form':f})
    
    def post(self,request):
        # limit parameter is only for premium subscribers
        # count = int(request.POST.get('count'))
        # api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(count)
        api_url = 'https://api.api-ninjas.com/v1/jokes?'
        response = requests.get(api_url, headers={'X-Api-Key': 'Y7dFXMfYJEDyswnZCts1Eg==McevFlJBTXrsbUCd'})

        if response.status_code == requests.codes.ok:
            return JsonResponse(response.json(),safe=False)
        else:
            print("Error:", response.status_code, response.text)

