from django.shortcuts import render, redirect
from .models import Place
from .forms import NewPlaceForm

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


# If user presses the visited button beside the place name, set visited value to True and then save. Return to main 
def place_is_visited(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        place = get_object_or_404(Place, pk=pk) # if object is valid, get the object, if not, trigger 404 error
        place.visited = True
        place.save()

    return redirect('place_list')
