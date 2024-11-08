from django.shortcuts import render
from .models import Review
from .forms import ReviewForm

# Create your views here.
def ExtraView(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ReviewForm()

    obj1 = Review.objects.get(id=1)
    obj2 = Review.objects.get(id=2)
    context = {
        'row1' : obj1,
        'row2' : obj2
    }
    return render(request, 'extra.html', context)