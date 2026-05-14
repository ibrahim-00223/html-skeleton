from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup


def parse_html(request):
    if request.method == 'POST':
        html = request.POST.get('html')
        url = request.POST.get('url')

        if url:
            try:
                response = requests.get(url)
                html = response.text
            except requests.RequestException as e:
                return JsonResponse({'error': str(e)}, status=400)

        if not html:
            return JsonResponse({'error': 'No HTML provided'}, status=400)

        soup = BeautifulSoup(html, 'html.parser')
        tree = build_tree(soup)
        return JsonResponse({'tree': tree})


def build_tree(element):
    """Convert a BeautifulSoup element into a tree structure."""
    if not hasattr(element, 'children'):
        return {'tag': str(element), 'children': []}

    children = []
    for child in element.children:
        if child.name is None:  # Skip text nodes
            continue
        children.append(build_tree(child))

    return {
        'tag': element.name,
        'attrs': dict(element.attrs),
        'children': children,
    }