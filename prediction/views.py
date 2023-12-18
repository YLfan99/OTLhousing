from django.shortcuts import render
from .form import PredictForm
# Create your views here.
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        # 获取前端输入数据
        form = PredictForm(request.POST)
        if form.is_valid():
            # 在这里运行后端逻辑，处理 user_input 数据
            X = process_input(form)
        
        result = model.predict([X])
        return render(request, 'result.html', {'result': result[0]})
    
    context = {}
    context['form'] = PredictForm()
    return render(request, 'index.html', context)

def process_input(input):
    pass