import requests


def searchEtna(query):
    url = f'https://www.etnassoft.com/api/v1/get/?title="{query}"&num_items=1'
    response = requests.get(url)
    payload = response.json()

    results = payload[0]
    book = {
        'title': results.get('title'),
        'subtitle': '',
        'authors': results.get('author'),
        'categories': results.get('categories'),
        'published_date': results.get('publisher_date'),
        'publisher': results.get('publisher'),
        'description': results.get('content'),
        'image': results.get('thumbnail'),
        'source': 'EtnasSoft Book'
    }

    return book
