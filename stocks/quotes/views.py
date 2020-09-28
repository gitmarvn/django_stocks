from django.shortcuts import render


def home(request):
    import requests
    import json

    # pk_40b606f9a69843238ff515cf84143173
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_40b606f9a69843238ff515cf84143173")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
       api = "Error..."

    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})