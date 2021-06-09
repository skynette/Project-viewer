from django.shortcuts import render

# Create your views here.
def initiate_payment(request):
	return render(request, 'index.html')