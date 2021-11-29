import requests


def search(query):
    url = f'https://www.googleapis.com/books/v1/volumes?q="{query}"&maxResults=2'
    response = requests.get(url)
    payload = response.json()
    results = payload.get('items')[0].get('volumeInfo')
    book = {
        'title': results.get('title'),
        'subtitle': '',
        'authors': results.get('authors'),
        'categories': results.get('categories'),
        'published_date': results.get('publishedDate'),
        'publisher': results.get('publisher'),
        'description': results.get('description'),
        'image': results.get('imageLinks').get('thumbnail'),
        'source': 'Google Book'
    }

    return book
