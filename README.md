### Setup virtual environment

    cd wishlist
    virtualenv venv
    venv/scripts/activate

### Install required modules
Install requirments

    pip install -r requirements.txt


Run server

    python manage.py runserver

Server should be at 127.0.0.1:8000  

For testing

    python manage.py test
    python manage.py test travel_wishlist/functional_tests
