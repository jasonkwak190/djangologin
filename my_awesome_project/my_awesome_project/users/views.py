from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login


def main(request):
    if request.method == 'GET':  # GET 방식은 여기서 처리
        return render(request, 'users/main.html')
    elif request.method == 'POST': # POST 방식은 여기서 처리
        # 로그인은 POST 방식이기에 여기서 처리
        username = request.POST['username'] # 전용 html 만들기
        password = request.POST['password'] #
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('posts:index')) # 성공시 post로 이동
        else:
            return render(request, 'users/main.html') # 다시 메인페이지로 랜더


