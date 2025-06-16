from django.shortcuts import render, redirect
from .models import Users, Teacher

# Landing page with login form
def index(request):
    return render(request, "index.html")

# Login logic
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = Users.objects.get(username=username, password=password)
            # You can store user info in session
            request.session['user_id'] = user.id
            return redirect('dashboard')
        except Users.DoesNotExist:
            return render(request, "index.html", {'error': 'Invalid credentials'})
    else:
        return redirect('index')



# Dashboard page
def dashboard(request):
    return render(request, "dashboard.html")

# Manage teachers page
def manage_teacher(request):
    teachers = Teacher.objects.all()
    return render(request, "manage_teacher.html", {"teachers": teachers})

# Save teacher record
def save_teacher(request):
    if request.method == "POST":
        teacher_id = request.POST.get("id")
        if teacher_id:
            # Update existing teacher
            teacher = Teacher.objects.get(id=teacher_id)
        else:
            # Create new teacher
            teacher = Teacher()

        teacher.tname = request.POST["tname"]
        teacher.subject = request.POST["subject"]
        teacher.qualification = request.POST["qualification"]
        teacher.contact = request.POST["contact"]
        teacher.leave_record = request.POST["leave_record"]
        teacher.save()

    return redirect("manage_teacher")


# Edit teacher (loads form or updates record)
def edit_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    if request.method == 'POST':
        teacher.tname = request.POST.get('tname')
        teacher.subject = request.POST.get('subject')
        teacher.qualification = request.POST.get('qualification')
        teacher.contact = request.POST.get('contact')
        teacher.leave_record = request.POST.get('leave_record')
        teacher.save()
        return redirect('manage_teacher')
    return render(request, "edit_teacher.html", {"teacher": teacher})

# Delete teacher
def delete_teacher(request, id):
    if request.method == 'POST':
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
    return redirect('manage_teacher')
def register(request):
    if request.method == 'POST':
        names = request.POST.get('names')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Optional: check if username already exists
        if Users.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already taken."})

        # Save the new user
        Users.objects.create(names=names, username=username, password=password)

        # Redirect to login (index page)
        return redirect('index')
    
    return render(request, "register.html")

def view_users(request):
    users = Users.objects.all()
    return render(request, 'view_users.html', {'users': users})

