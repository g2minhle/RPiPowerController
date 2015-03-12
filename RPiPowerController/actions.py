from django.shortcuts import render

def turnOff(request):
    print "requested to turnOff"
    return render(request, 'turnOff.html', {})

def turnOn(request):
    print "requested to turnOn"
    return render(request, 'turnOn.html', {})
    return "turnOn"
