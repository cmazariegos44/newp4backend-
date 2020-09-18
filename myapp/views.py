# from django.shortcuts import render,redirect
# from django.http import HttpResponseRedirect
from .models import Task, Reminder
# from .forms import *
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TaskSerializer, ReminderSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated] #Coule be [permissions.IsAuthenticated]

class ReminderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here. 

# def index(request):
#     allItems = Task.objects.all()
#     return render(request, "dashboard.html", {"allItems": allItems})

# def book_by_id(request, book_id):
#     book = Book.objects.get(pk=book_id)
#     return HttpResponse(f"Book: {book.title}, published on {book.pub_date}")
 
# def addTodo(request):
#     new_item = Book(content = request.POST['content'])
#     new_item.save()
#     return HttpResponseRedirect('/app/')


#THESE ARE MY METHOD REQUESTS

# def index(request):
# 	tasks = Task.objects.all()

# 	form = TaskForm()

# 	if request.method =='POST':
# 		form = TaskForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('/')


# 	context = {'tasks':tasks, 'form':form}
# 	return render(request, 'list.html', context)


# def updateTask(request, pk):
# 	task = Task.objects.get(id=pk)

# 	form = TaskForm(instance=task)

# 	if request.method == 'POST':
# 		form = TaskForm(request.POST, instance=task)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/')

# 	context = {'form':form}

# 	return render(request, 'update_task.html', context)

# def deleteTask(request, pk):
# 	item = Task.objects.get(id=pk)

# 	if request.method == 'POST':
# 		item.delete()
# 		return redirect('/')

# 	context = {'item':item}
# 	return render(request, 'delete.html', context)






#BELOW IS THE LOGIN

# def indexView(request):
#     return render(request, 'list.html') 

# @login_required
# def dashboardView(request):
#     return render(request, 'dashboard.html')

# def registerView(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login_url')
#     else:
#         form = UserCreationForm()

#     return render(request, 'registration/register.html', {'form':form})





