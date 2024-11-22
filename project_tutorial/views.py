from django.shortcuts import render, redirect

from .forms import DroneForm
from .models import Drone, News


# def create_drone(request):
#     if request.method == 'POST':
#         form = DroneForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('drone_list')
#     else:
#         form = DroneForm()
#         return render(request, 'drone/create_update.html', {'form': form})


def create_drone(request):
    if request.method == 'POST':
        form = DroneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drone_list')
        else:
            return render(request, 'drone/create_update.html', {'form': form})
    else:
        form = DroneForm()
    return render(request, 'drone/create_update.html', {'form': form})


def drone_list(request):
    drones = Drone.objects.all()
    return render(request, 'drone/list.html', {'drones': drones})


def get_drone(request, pk):
    drone = Drone.objects.get(pk=pk)
    context = {
        'drone': drone
    }
    return render(request, 'drone/detail.html', context)


def update_drone(request, pk):
    instance = Drone.objects.get(pk=pk)
    form = DroneForm(request.POST, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('drone_list')
    else:

        form = DroneForm(instance=instance)
    return render(request, 'drone/create_update.html', {'form': form})


def delete_drone(request, pk):
    drone = Drone.objects.get(pk=pk)
    if request.method == 'POST':
        drone.delete()
        return redirect('drone_list')
    return render(request, 'drone/delete.html', {'drone': drone})


def news_get(request):
    # news = News.objects.filter(pk__gte=4)
    news=News.objects.filter(title='Sanjar')
    return render(request, 'drone/news.html', {'news': news})


