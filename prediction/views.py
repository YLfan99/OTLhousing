from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        # 获取前端输入数据
        user_input = request.POST.get('user_input')
        
        # 在这里运行后端逻辑，处理 user_input 数据
        X = process_input(user_input)
        result = model.predict([X])
        return render(request, 'result.html', {'result': result[0]})
    return render(request, 'index.html')

