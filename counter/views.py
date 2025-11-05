import requests
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def home(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        logger.info(f"Searching for: {query}")

        api_url = f'https://api.api-ninjas.com/v1/nutrition?query={query}'
        headers = {
            'X-Api-Key': 'XQliKJR1UqkVJji/c4H78g==GIiS63GxZgByFL2i'  # Replace if invalid
        }

        try:
            response = requests.get(api_url, headers=headers)  # ✅ fixed
            response.raise_for_status()
            
            api_data = response.json()
            logger.info(f"API Response: {api_data}")

            return render(request, 'index.html', {
                'api': api_data,
                'query': query
            })
            
        except requests.RequestException as e:
            logger.error(f"API Error: {str(e)}")
            return render(request, 'index.html', {
                'api': "oops! There was an error",
                'error': str(e)
            })
    
    return render(request, 'index.html')


#curl -X GET "https://api.api-ninjas.com/v1/nutrition?query=idli" \
 # -H "X-Api-Key: XQliKJR1UqkVJji/c4H78g==GIiS63GxZgByFL2i"
#home