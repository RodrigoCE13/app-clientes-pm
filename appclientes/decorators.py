from django.shortcuts import redirect

def admin_only(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser and not request.user.is_staff:
            return redirect('home')  # Redirige al usuario a la página de inicio si no es un administrador ni personal con el rol de staff
        return view_func(request, *args, **kwargs)
    return wrapper
