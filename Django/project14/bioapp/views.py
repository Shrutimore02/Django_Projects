from django.shortcuts import render

# Create your views here.
def display_biodata(request):
	
	return render(request=request, template_name='bioapp/bio.html')


def display_sslc(request):

	return render(request=request, template_name='bioapp/sslc.html')


def display_puc(request):

	return render(request=request, template_name='bioapp/puc.html')


def display_degree(request):


	return render(request=request, template_name='bioapp/degree.html')

