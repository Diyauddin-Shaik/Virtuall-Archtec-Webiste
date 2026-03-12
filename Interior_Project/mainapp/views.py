from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import RoomDesign, ChatMessage


# ---------------- HOME ----------------

def home(request):
    return render(request, 'home.html')


# ---------------- REGISTER ----------------

def register(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'register.html')


# ---------------- LOGIN ----------------

def user_login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('rooms')

        return render(request,'login.html',{'error':'Invalid username or password'})

    return render(request,'login.html')


# ---------------- LOGOUT ----------------

def user_logout(request):
    logout(request)
    return redirect('login')


# ---------------- DASHBOARD ----------------

@login_required
# def dashboard(request):
#     return render(request, 'dashboard.html')

def dashboard(request):
    return redirect('rooms')


# ---------------- ROOM SELECTION ----------------

@login_required
def room_select(request):
    return render(request, 'room_select.html')


# ---------------- ROOM DESIGN FORM ----------------

@login_required
def room_design(request):

    room = request.GET.get('room')

    if request.method == "POST":

        image = request.FILES.get('image')

        wall = request.POST.get('wall')
        lamp = request.POST.get('lamp')
        furniture = request.POST.get('furniture')
        house = request.POST.get('house')

        design = RoomDesign.objects.create(
            user=request.user,
            room_type=room,
            house_type=house,
            wall_color=wall,
            lamp_type=lamp,
            furniture=furniture,
            image=image
        )

        return redirect('design_result', design_id=design.id)

    return render(request, 'room_design.html', {'room': room})


# ---------------- DESIGN RESULT PAGE ----------------

@login_required
def design_result(request, design_id):

    design = RoomDesign.objects.get(id=design_id)

    suggestion = ""

    if design.room_type == "Living Room":

        suggestion = f"""
        You selected {design.wall_color} wall color with {design.lamp_type} lighting
        and {design.furniture} style furniture.

        This combination can work well for a modern living room. If you want to
        improve the ambiance further, consider adding warm lighting and neutral
        color accents to make the room feel more spacious and comfortable.
        """

    elif design.room_type == "Kitchen":

        suggestion = f"""
        Your kitchen design includes {design.wall_color} cabinets,
        {design.lamp_type} lighting, and {design.furniture} countertop style.

        For better functionality you may consider brighter LED lighting
        and lighter cabinet colors to enhance visibility and cleanliness.
        """

    elif design.room_type == "Bedroom":

        suggestion = f"""
        You selected a {design.house_type} bedroom with {design.furniture} style.

        Bedrooms usually benefit from soft ambient lighting and calm color
        palettes that help improve relaxation and sleep quality.
        """

    elif design.room_type == "Bathroom":

        suggestion = f"""
        Bathroom design with {design.wall_color} tile style,
        {design.lamp_type} shower type, and {design.furniture} sink style
        can create a modern bathroom look.

        Adding brighter mirror lighting can further improve functionality.
        """

    elif design.room_type == "Dining Room":

        suggestion = f"""
        Your dining space includes {design.furniture} dining table style
        with {design.lamp_type} lighting.

        Pendant lights above the dining table usually enhance the
        dining experience and create a warm atmosphere.
        """

    elif design.room_type == "Kids Room":

        suggestion = f"""
        A kids room with {design.wall_color} theme and {design.furniture}
        furniture can create a playful environment.

        Consider adding colorful wall art and storage units to keep
        the room organized and fun.
        """

    else:

        suggestion = "Your design choices have been saved successfully."

    return render(request, 'design_result.html', {
        'design': design,
        'suggestion': suggestion
    })


# ---------------- USER DESIGN HISTORY ----------------

@login_required
def my_designs(request):

    designs = RoomDesign.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'my_designs.html', {
        'designs': designs
    })


# ---------------- CHAT ----------------

@login_required
def chat(request):

    if request.method == "POST":

        msg = request.POST.get("message")

        if msg:
            ChatMessage.objects.create(
                user=request.user,
                message=msg
            )

    # Only show current user's messages
    messages = ChatMessage.objects.filter(
        user=request.user
    ).order_by("created_at")

    return render(request, "chat.html", {
        "messages": messages
    })