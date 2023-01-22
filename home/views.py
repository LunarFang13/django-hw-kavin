from django.shortcuts import render
import requests



TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR,"templates"),'
)

# Create your views here.
def index(request):
    URL = "https://www.boredapi.com/api/activity"
    act = requests.get(url = URL).json()['activity']
    return render(request,"index.html", {"act": act})