from django.shortcuts import render
from django.http import JsonResponse

# Hardcoded JSON data
PLACES_DATA = {
    "Japan": {
        "temples": [
            {"name": "Kyoto Temple", "image":"https://local-api-backends-6.onrender.com/static/istockphoto-508628776-612x612.jpg", "description": "Historic temple in Kyoto", "rating": 4.7},
            {"name": "Senso-ji Temple", "description": "Ancient temple in Tokyo", "rating": 4.6 , "image": "https://local-api-backends-6.onrender.com/static/visit_img07_l.jpg"}
        ],
                "collegs": [
            {"name": "keiou university", "description": "University of Science", "image": "https://local-api-backends-6.onrender.com/static/images.jpg"},
            {"name": "Hokkaido university", "description": "Applied Science", "image": "https://local-api-backends-6.onrender.com/static/hokkaido_university-cropped.jpg"}
        ],
        "Entertaiment": [
            {"name": "Bar Kyu", "description": "Cozy bar in Tokyo", "rating": 4.3, "image": "https://local-api-backends-6.onrender.com/static/659-kue-bar-at-westin-hotel-in-pune-maharashtra--food-drinks-image-Kue_bar_110711_MD_16.jpg"},
            {"name": "The SG club", "description": "club", "rating": 4.1, "image": "https://local-api-backends-6.onrender.com/static/a0000782_main.jpg"}
        ],
     
    },
    "America": {
        "Temples": [
             {"name":"Shiva Temple","description":"first Hindu temple in USA’s ","image":"https://local-api-backends-6.onrender.com/static/sri-rama-temple-hindu-temple-greater-chicago-lemont-illinois.jpg"},
             {"name":"Ganesh Temple","description":"Malibu Hindu Temple, Calabasas, California ","image":" https://local-api-backends-6.onrender.com/static/Malibu-Hindu-Temple-California.jpg"},
            {"name":"Iraivan Temple","description":"Iraivan Temple, Hawaii","image":" https://local-api-backends-6.onrender.com/static/Iraivan-Temple-Iraivan-Temple-Hawaii-1024x618.jpg"},
           
             ],
           
        "pubs and Liquor": [
            {"name": "Barrel & Brews.", "description": "Cozy bar", "rating": 4.3, "image": "https://local-api-backends-6.onrender.com/static/659-kue-bar-at-westin-hotel-in-pune-maharashtra--food-drinks-image-Kue_bar_110711_MD_16.jpg"},
            {"name": "Whiskey Dreams", "description": "club", "rating": 4.1, "image":"https://local-api-backends-6.onrender.com/static/1464214000-best-bars-lead.jpg"}
        ],
       
        "Entertainments": [
            {"name": "Houston", "description": "The City With No Limits", "rating": 4.8, "image": "https://local-api-backends-6.onrender.com/static/HOUSTON.jpg"},
         {"name": "Disney Animal", "description": "Disney Animal kingdome park", "rating": 4.8, "image": "https://local-api-backends-6.onrender.com/static/Tree_of_Life,_Disney's_Animal_Kingdom.jpg"},
            {"name": "Time square", "description": "Heart of Newyork city", "rating": 4.9, "image": "https://local-api-backends-6.onrender.com/static/Times-Square-andreas-m-unsplash-scaled.jpg"}
        ]
    }
}


def index(request):
    return render(request, 'home.html')

def places_view(request):
    country = request.GET.get('country')
    country = str(country).capitalize()
    if country in PLACES_DATA:
        return JsonResponse(PLACES_DATA[country])
    else:
        #  return JsonResponse({}, status=404)
          return JsonResponse({'error':'not found'}, status=404)
       