from django.shortcuts import render, redirect
from .models import TeamMember, Milestone, WardrobeItem, Lookbook
from .recommendations import get_recommendations
from .fashion_trends import fetch_trends


# Create your views here.
def home(request):
    return render(request, trends/home.html)

def team(request):
    members = TeamMember.objects.all()
    return render(request, 'trends/team.html', {'members': members})

def milestones(request):
    milestones = Milestone.objects.all()
    return render(request, 'trends/milestones.html', {'milestones': milestones})

def wardrobe(request):
    if request.method =='POST':
        item_name = request.POST('item_name')
        item_image = request.FILES('item_image')
        WardrobeItem.objects.create(user=request.user, item_name=item_name, item_image=item_image)
        return redirect('wardrobe')
    
    items = WardrobeItem.objects.filter(user=request.user)
    return render(request, 'trends/wardrobe.html', {'items': items})

def recommendations(request, user_id):
    recommended_items = get_recommendations(user_id)
    return render(request, 'trends/recommendations.html', {'recommended_items': recommended_items})

def trends(request):
    trends = fetch_trends()
    return render(request, 'trends/trends.html', {'trends': trends})

def lookbooks(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        Lookbook.objects.create(user=request.user, title=title, description=description, image=image)
        return redirect('lookbooks')
    
    lookbooks = Lookbook.objects.all()
    return render(request, 'trends/lookbooks.html', {'lookbooks': lookbooks})
