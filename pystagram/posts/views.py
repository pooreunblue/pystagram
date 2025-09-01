from posts.forms import CommentForm
from posts.models import Post
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect

def feeds(request):
    # 요청에 포함된 사용자가 로그인하지 않은 경우
    if not request.user.is_authenticated:
        return redirect("/users/login/")

    # 모든 글 목록을 템플릿으로 전달
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        "posts": posts,
        "comment_form": comment_form,
    }
    return render(request, "posts/feeds.html", context)

@require_POST # 댓글 작성을 처리할 View, Post 요청만 허용한다
def comment_add(request):
        # request.POST러 전달된 데이터를 사용해 CommentForm 인스턴스를 생성
        form = CommentForm(data=request.POST)
        if form.is_valid():
            # commit=False 옵션으로 메모리상에 Comment 객체 생성
            comment = form.save(commit=False)

            # Comment 생성에 필요한 사용자 정보를 request에서 가져와 할당
            comment.user = request.user

            # DB에 Comment 객체 저장
            comment.save()

            # 생성된 Comment의 정보 확인
            print(comment.id)
            print(comment.content)
            print(comment.user)
            # 생성 완료 후에는 피드 페이지로 다시 이동
            return HttpResponseRedirect(f"/posts/feeds/#post-{comment.post.id}")
