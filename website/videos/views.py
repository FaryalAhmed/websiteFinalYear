from django.shortcuts import render, redirect, get_object_or_404
from .models import Video, UserProfile
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import auth



def UploadView(request):
    if not request.user.is_authenticated:
        return redirect('../login')
    else:

        if request.GET.get('query'):
            return redirect('/videos/?query=' + request.GET.get('query') )
        if request.FILES.get('video'):
            if request.POST.get('title') and request.FILES.get('video') and request.POST.get('description'):
                video = Video()
                video.title = request.POST.get('title')
                video.description = request.POST.get('description')
                video.video = request.FILES.get('video')
                video.user = request.user
                video.save()
                return redirect('/videos/' + str(video.id))

        return render(request, 'upload.html', {})

def VideosView(request):

    queryset_list = Video.objects.all()
    query = request.GET.get('query')
    if query:
        queryset_list = queryset_list.filter(
        Q(title__icontains=query)|
        Q(description__icontains=query)|
        Q(user__username__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 5)
    page = request.GET.get('page')
    queryset = paginator.get_page(page)

   
    return render(request, 'videos.html', {'queryset': queryset})



def VideoDetailView(request,video_id):


    video = get_object_or_404(Video, pk = video_id)
    videoUserName = video.user.username
    userprofile = get_object_or_404(UserProfile, username=videoUserName)


    recentvideos =Video.objects.all()
    tempvideos= []
    count = 0
    for recentvideo in recentvideos:
        if recentvideo.id != video_id:
            tempvideos.append(recentvideo)
            count= count +1
            if count >= 4:
                break


    recentvideos = tempvideos


    #Used When Query Search Used in Video Detail View to redirect to the search view.
    if request.GET.get('query'):

        return redirect('/videos/?query=' + request.GET.get('query') )

    videoUserName = video.user.username
    userprofile = get_object_or_404(UserProfile, username=videoUserName)
    #adding a view with every video detail GET request
    video.views = video.views + 1
    video.save()





    return render(request,'videodetail.html',{'video':video,'recentvideos':recentvideos, 'userprofile':userprofile})







