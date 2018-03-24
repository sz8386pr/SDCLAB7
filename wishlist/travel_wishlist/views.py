from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm, VisitPlaceForm

# Create your views here.
def place_list(request):
    # if user posts the form and the form is valid, save the form data as Place object and 
    #   redirect to 'place_list', the index page again
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()
        if form.is_valid():
            place.save()
            return redirect('place_list')

    # if it's not post (default/initial loading screen for instance)
    #   render wishlist.html using the places and new_place_form values ordered by name value of the Place class object
    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})


# render visited.html using Place objects that have visited=True value, ordered by the name
def places_visited(request):
    visited = Place.objects.filter(visited=True).order_by('name')
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})


# place/place.pk is the rendered url.
# displays VisitPlaceForm if visited is false, otherwise, render the place information
def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if not place.visited:
        form = VisitPlaceForm(instance=place)
        if request.method == "POST":
            form = VisitPlaceForm(request.POST, instance=place)
            if form.is_valid():
                place = form.save(commit=False)
                place.visited = True
                place.save()

        return render(request, 'travel_wishlist/place_detail.html', {'place': place, 'form': form})

    return render(request, 'travel_wishlist/place_detail.html', {'place': place})
