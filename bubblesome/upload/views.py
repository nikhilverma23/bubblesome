from bubblesome.upload.models import UploadImage
from bubblesome.upload.forms import UploadImageForm
from django.shortcuts import render_to_response
from django.template import RequestContext


def demo_upload(request):
    """
    showing the demo upload
    """
    if request.method == "POST":
        form = UploadImageForm(request.POST,request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            title = cd['title']
            image = cd['image']
            upload_image_obj = UploadImage.objects.get_or_create(
                title = title,
                image=image
            )
            return render_to_response(
                            "upload/place_bubble.html",
                            {"upload_image_obj":upload_image_obj[0]},
                            context_instance = RequestContext(request)
                            )
        else:
            print "UploadImageForm is Invalid"
    else:
        form = UploadImageForm()
    return render_to_response(
                            "upload/demo_page.html",
                            {"form":UploadImageForm},
                            context_instance = RequestContext(request)
                            )