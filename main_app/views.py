from typing import Any
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Crystal

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"

class Crystal:
    def __init__(self, name, img, bio, location):
        self.name = name
        self.img = img
        self.bio = bio
        self.location = location

crystals = [
    Crystal('Clear Quartz','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7WZ8uk2sJF-gIzj12_dMqwOz-9nH3fi01EQ&usqp=CAU','Clear Quartz is one of the most versatile and widely used crystals. It is known as the "Master Healer" due to its ability to amplify energy and intentions. Clear Quartz is believed to enhance spiritual growth, mental clarity, and overall energy balance.','It is found in various locations worldwide, including Brazil, the United States, and Madagascar.'),
    Crystal('Amethyst','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQv5Tkh4NyLjKjdxpYZXfVaSauunDPpzu0Mkw&usqp=CAU','Amethyst is a popular crystal known for its soothing and protective properties. It is often used to promote calmness, relieve stress, and aid in meditation and spiritual growth.',' Amethyst is typically found in regions such as Brazil, Uruguay, and Zambia.'),
    Crystal('Rose Quartz','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTshnAGeIfRPaYOa7H29XHElzY888MQCuQe8D1BdLKYSRlq_sCAvSdks4AUtXclozLzmPg&usqp=CAU','Rose Quartz is associated with love, compassion, and emotional healing. It is often used to attract and enhance romantic love, promote self-love, and foster a sense of inner peace.',' Rose Quartz can be found in locations such as Brazil, Madagascar, and South Africa.'),
    Crystal('Citrine','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_jV5w-2unT2e8EAkaMFe-HM18khQ-KPYLmNlAUXUdVU3AoUXSXN_if1a5AeHr8PuZZug&usqp=CAU','Citrine is a vibrant crystal known for its association with abundance, success, and positive energy. It is believed to bring prosperity, enhance motivation, and promote creativity. ','Natural Citrine can be found in countries like Brazil, Madagascar, and the United States.'),
    Crystal('Selenite','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmUtBbr1ZtoG1FrxO1qtYkjFdH9aK2fAQN_A&usqp=CAU','Selenite is a gentle and calming crystal often used for cleansing and purifying energy. It is believed to promote clarity, intuition, and spiritual connection.','Selenite is found in countries such as Mexico, Morocco, and the United States.'),
]

class CrystalList(TemplateView):
    template_name = "crystal_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["crystals"] = crystals
        return context
