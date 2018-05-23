from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def wind(request):
	return render(request, 'wind.html')

def items(request):
	items = item.objects.all()
	return render(request, 'items.html', {'items'})

def item_view(request, title):
	the_item = item.objects.filter(title=title)
	return render(request, 'item.html', {'items':the_item})

def index(request):
	if request.method == 'POST':
		contactform = Form(request.POST)
		if form.is_valid():
			name = request.POST.get('name', None)
			email = request.POST.get('email', None)
			comments = request.POST.get('comments', None)
			rsvp1 = contact.objects.update_or_create(
                            name = name,
                            email = email,
                            comments = comments,
                            )
			message = 'Thank you! Xtyozen liu!'
			return render(request, 'index.html', { 'message':message })

	else:
		form = rsvpForm()
		return render(request, 'index.html', { 'form':form })