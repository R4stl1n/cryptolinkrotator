from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from brake.decorators import ratelimit

from .models import Rotator
from .models import RotatorLink

# Create your views here.

def index(request):
	template = loader.get_template('rotator/index.html')
	return HttpResponse(template.render({}, request))

@ratelimit(rate='10/h')
def rotate(request, rotate):
    
    rotator = get_object_or_404(Rotator, rotator_slug=rotate)

    rotator_set = rotator.rotatorlink_set.all()

    rotator.current_index = rotator.current_index + 1

    if rotator.current_index > (len(rotator_set)-1):
        rotator.current_index = 0
    
    print(rotator_set[rotator.current_index].rotator_link)

    rotator_set[rotator.current_index].times_viewed = rotator_set[rotator.current_index].times_viewed + 1

    rotator_set[rotator.current_index].save()
    rotator.save()

    return redirect(rotator_set[rotator.current_index].rotator_link)
