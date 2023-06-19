from django.shortcuts import redirect

def admin_only(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:  # Verifica si el usuario no es un administrador
            return redirect('home')  # Redirige al usuario a la página de inicio
        return view_func(request, *args, **kwargs)
    return wrapper
