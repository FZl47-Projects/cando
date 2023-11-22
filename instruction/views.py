from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Instruction, Article

# Create your views here.

class Instructions (View):
    template_name = 'instruction/Education.html'
    def get(self, request):
        instructions = Instruction.objects.all()
        articles = Article.objects.all()
        context = {
            'instructions' : instructions,
            'articles' : articles
        }

        return render(request, self.template_name, context)
    def post(self, request):
        post = request.POST
        if 'add-instruction' in post:
            title = post.get('amozesh', False)
            ingredients = post.get('mavad', False)
            time = post.get('zaman', False)
            difficulty = post.get('brand', False)
            recipe = post.get('recipe')
            img = request.FILES.get('image',False)
            instruction = Instruction(title=title, ingredients=ingredients, time=time, difficulty=difficulty, recipe=recipe, img=img)
            instruction.save()

        elif 'add-article' in post:
            title = post.get('article-title', False)
            description = post.get(('article-content', False))
            article = Article(title=title, description=description)
            article.save()
        return redirect ('instruction:instructions')
            
        
    

       
      
