import requests


def hello_get(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    return 'Hello World!'


def get_nearby_gyms(request):
    URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    PARAMS = {
        'key': os.environ.get('API_KEY'),
        'location': '37.7576792,-122.5078119',
        'radius': 2000,
        'type': 'gym'
    }

    r = requests.get(url=URL, params=PARAMS)

    # extracting data in json format
    data = r.json()

    """HTTP Cloud Function.
        Args:
            request (flask.Request): The request object.
            <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
        Returns:
            The response text, or any set of values that can be turned into a
            Response object using `make_response`
            <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
        """
    return data
