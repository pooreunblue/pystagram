from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import LoginForm, SignupForm
from users.models import User

def login_view(request):
    if request.user.is_authenticated:
        return redirect("posts:feeds")

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        # LoginForm에 전달된 데이터가 유효하다면
        if form.is_valid():
            # username과 password 값을 가져와 변수에 할당
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # username, password에 해당하는 사용자가 있는지 검사
            user = authenticate(username=username, password=password)

            # 해당 사용자가 존재한다면
            if user:
                # 로그인 처리 후, 피드 페이지로 redirect
                login(request, user)
                return redirect("posts:feeds")
            # 사용자가 없다면 "실패했습니다" 로그 출력
            else:
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다")
        # 어떤 경우든 실패한 경우(데이터 검증, 사용자 검사) 다시 LoginForm을 사용한 로그인 페이지 렌더링
        context = {"form": form}
        return render(request, "users/login.html", context)
    else:
        form = LoginForm()
        context = {"form": form}
        return render(request, "users/login.html", context)

def logout_view(request):
    # logout 함수 호출에 request를 전달한다
    logout(request)

    # logout 처리 후, 로그인 페이지로 이동한다
    return redirect("users:login")

def signup(request):
    # POST 요청 시, form 이 유효하다면 최종적으로 redirect 처리된다
    if request.method == "POST":
        form = SignupForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("posts:feeds")
        # POST 요청에서 form이 유효하지 않다면, 아래의 context = ... 부분으로 이동한다.

    else:
        form = SignupForm()
    # context로 전당되는 form은 두 가지 경우가 존재한다
    # 1. POST 요청에서 생성된 form이 유효하지 않은 경우 -> 에러를 포함한 form이 사용자에게 보여진다
    # 2. GET 요청으로 빈 form이 생성된 경우 -> 빈 form이 사용자에게 보여진다
    context = {"form": form}
    return render(request, "users/signup.html", context)