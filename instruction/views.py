from django.shortcuts import render
from django.views.generic import View
from .models import Instruction

# Create your views here.

class Instructions (View):
    template_name = 'instruction/Education.html'
    def get(self, request):
        instructions = Instruction.objects.all()
        context = {
            'instructions' : instructions
        }

        return render(request, self.template_name, context)
    def post(self, request):
        post = request.POST
        title = post.get('amozesh', False)
        ingredients = post.get('mavad', False)
        time = post.get('zaman', False)
        difficulty = post.get('brand', False)
        recipe = post.get('recipe')
        instruction = Instruction(title=title, ingredients=ingredients, time=time, difficulty=difficulty, recipe=recipe)
        instruction.save()
        context = {
            'instructions' : instructions
        }
        return render(request, self.template_name, context)