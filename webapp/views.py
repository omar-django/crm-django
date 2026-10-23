from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Record
import logging
from django.contrib import messages
from django.views.decorators.http import require_POST


def index(request):
    return render(request, 'web/index.html')


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect('login')
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'web/register.html', context)


def my_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('dashboard')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'web/login.html', context)


@login_required(login_url='login')
@never_cache
def dashboard(request):
    records = Record.objects.filter(owner=request.user)

    return render(request, 'web/dashboard.html', context={'record': records})


@login_required(login_url='login')  
def create_record(request):
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.owner = request.user
            record.save()
            messages.success(request, "Record created successfully.")
            return redirect('dashboard')

    else:
        form = CreateRecordForm()
    context = {'form': form}
    return render(request, 'web/create-record.html', context)


@login_required(login_url='login')
@never_cache
def view_record(request, record_id):
    all_records = get_object_or_404(Record, id=record_id, owner=request.user)
    context = {'record': all_records}
    return render(request, 'web/view-record.html', context)


@login_required(login_url='login')
def update_record(request, record_id):
    record = get_object_or_404(Record, id=record_id, owner=request.user)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated.")
            return redirect('dashboard')
    else:
        form = UpdateRecordForm(instance=record)
    context = {'form': form}
    return render(request, 'web/update-record.html', context)


@login_required(login_url='login')
@require_POST
def delete_record(request, record_id):
    record = get_object_or_404(Record, id=record_id, owner=request.user)
    record.delete()
    messages.success(request, "Record deleted.")
    return redirect('dashboard')


logger = logging.getLogger(__name__)


@login_required(login_url='login')
@never_cache
def search_records(request):
    query = request.GET.get('query')
    results = []
    try:
        if query:
            results = Record.objects.filter(owner=request.user).filter(
                Q(id__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query))
    except Exception as e:
        logger.error(f"Error occurred during search: {e}")

    return render(request, 'web/search-records.html', context={'results': results, 'query': query})


def custom_404_view(request, exception):
    return render(request, 'web/404.html', status=404)


def my_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
