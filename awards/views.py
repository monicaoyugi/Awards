from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from . models import Project , Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Profile, Post
from django.utils import timezone
from django.views.generic import RedirectView
from django.template.loader import render_to_string



@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user.id
    user = request.user
    date = dt.date.today()
    posts = Post.objects.all()
    if Profile.objects.filter(user = request.user).count() == 0:
        prof = Profile(user=request.user)
        prof.save()
    return render(request, 'index.html',{"date": date, "posts": posts})


def add_comment(request,id):
    current_user = request.user
    image = Image.get_single_photo(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image_id = id
            comment.save()
        return redirect('index')

    else:
        form = CommentForm()
        return render(request,'new_comment.html',{"form":form,"image":image})

def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"profile":searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

class PostList(APIView):
    def get(self, request, format=None):
        all_post = Post.objects.all()
        serializers = PostSerializer(all_post, many=True)
        return Response(serializers.data)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Post.objects.all()
        serializers = PostSerializer(all_profile, many=True)
        return Response(serializers.data)