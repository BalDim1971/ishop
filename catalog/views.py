from django.shortcuts import render


def product(request):
	return render(request, 'catalog/product.html')


def index(request):
	return render(request, 'catalog/index.html')


def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')
		print(f'You have new message from {name}({email}): {message}')
	return render(request, 'catalog/contacts.html')
