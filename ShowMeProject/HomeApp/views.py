from django.shortcuts import render, redirect
from .models import *
from accountapp.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

def LandingPage(request):
    auth_usr = request.user
    context = {
        'usr': auth_usr
    }
    return render(request, 'HomeApp/LandingPage.html', context)

def WatchApp(request):
    auth_usr = request.user
    obj = UploadVideoModel.objects.all()
    #a = UploadVideoModel.objects.get(root_user__username)
    context = {
        'usr': auth_usr,
        'obj': obj,
    }
    return render(request, 'HomeApp/watch.html', context)

def user_details(request, usr_id):
    usr_obj = UsrRegModel.objects.get(root_user__username=usr_id)
    vid_obj = UploadVideoModel.objects.filter(root_user__username=usr_id)
    context = {
        'obj': usr_obj,
        'vid_obj': vid_obj,
    }
    return render(request, 'HomeApp/user_details.html', context)

def user_details_video(request, usr_id):
    usr_obj = UsrRegModel.objects.get(root_user__username=usr_id)
    vid_obj = UploadVideoModel.objects.filter(root_user__username=usr_id)
    context = {
        'obj': usr_obj,
        'vid_obj': vid_obj,
    }
    return render(request, 'HomeApp/user_details_video.html', context)

def video_like_fun(request, likeid):
    print('just came in video like function')
    vdobj = UploadVideoModel.objects.get(id=likeid)
    vdobj.video_likes.add(request.user)
    vdobj.save()
    print('like saved brooooo...')
    return HttpResponseRedirect(reverse('Watch'))

def video_dislike_fun(request, dislikeid):
    return redirect('Watch')




