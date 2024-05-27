from django.shortcuts import render, redirect
from .models import TeamMember, Milestone, WardrobeItem
from .recommendations import get_recommendations
from .fashion_trends import fetch_trends
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request):
    return render(request, 'trends/home.html')



def team(request):
    team_members = [
         {
            'name': 'Lorine Adhiambo',
            'position': 'Founder',
            'bio': 'Lorine Adhiambo is the founder of EcoChic, a fashion brand dedicated to sustainability and style. With a passion for eco-friendly practices, Miss Lorine leads the company in offering ethically sourced and fashionable clothing for the modern consumer.',
            'image_url': os.path.join(settings.STATIC_URL, 'media/C.E.O.jpg'),
        },
    
        {
            'name': 'Victor Jared',
            'position': 'Photographer',
            'bio': 'Victor Jared is a skilled photographer at EcoChic, capturing the essence of sustainable fashion. With a keen eye for detail and a passion for eco-friendly practices, we bring the beauty of ethical fashion to life through stunning visuals.',
            'image_url': os.path.join(settings.STATIC_URL, 'media/Jphoto.jpg'),
        },
        {
            'name': 'Arielle Doreen',
            'position': 'Designer',
            'bio': 'Arielle Doreen is a talented designer at EcoChic, blending sustainability with modern fashion. Arielle creates stylish, ethically sourced clothing that embodies both innovation and environmental responsibility.',
            'image_url': os.path.join(settings.STATIC_URL, 'media/AD.jpg'),
        },
     ]  

    context = {'team_members': team_members}
    return render(request, 'trends/team.html', context)



def milestones(request):
       milestones = [
        {'title': 'Launch of EcoChic Website', 'description': 'The EcoChic website is now live, offering a wide range of sustainable fashion choices. Explore our eco-friendly collections and join us in making fashion more sustainable.', 'date': 'June 1, 2024'},
        {'title': 'Reached 100 Customers', 'description': 'We are excited to celebrate our first major milestone of reaching 100 customers. Thank you for supporting our mission of sustainability in fashion.', 'date': 'July 15, 2024'},
        {'title': 'Summer Collection Launch', 'description': 'We have unveiled our summer collection, featuring the latest trends in sustainable fashion. Discover our new eco-conscious designs and refresh your wardrobe.', 'date': 'August 10, 2024'}
    ]
       context = {'milestones': milestones}
       return render(request, 'trends/milestones.html', context )
    

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

