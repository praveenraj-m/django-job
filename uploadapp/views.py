from django.shortcuts import render

from uploadapp.forms import UPloadFileForm, Uploadform

# Create your views here.
def uploadimage(request):
    if request.method == "POST":
        form = Uploadform(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            saved_obj = form.instance
            return render(request, 'uploadapp/addimage.html', {'form':form, 'saved_obj':saved_obj})
    else:
        form = Uploadform()
    return render(request, 'uploadapp/addimage.html', {'form':form})

def uploadfile(request):
    if request.method == "POST":
        form = UPloadFileForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            saved_file_obj = form.instance
            return render(request, 'uploadapp/addfile.html', {'form':form, 'saved_file_obj':saved_file_obj})
    else:
        form = UPloadFileForm()
    return render(request, 'uploadapp/addfile.html', {'form':form}) 