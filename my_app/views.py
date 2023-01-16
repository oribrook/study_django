from django.shortcuts import render
from django.http import HttpResponse


def my_view(request):
    return HttpResponse("<h3> Hi  <h3>")


def serve_html(request):
    # return render(request=request, template_name="my_app/index.html")
    name = "ori"
    return render(request=request, template_name="my_app/index.html", context={"person": {"name": name}})


def say_hi(req, my_arg):
    return render(request=req, template_name="my_app/index.html", context={"person": {"name": my_arg}})


def default(req):
    return HttpResponse("Not implemented view!, \n"
                        "try: 'http://127.0.0.1:8000/app/home'")
