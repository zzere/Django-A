from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    formulario_contacto=FormularioContacto()          #cap43

    if request.method=="POST":                          #cap 45
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            mail=EmailMessage(
                "Mensaje desde App Django",
                "El usuario con nombre {} con la direccion {} escribe lo siguiente: \n\n {}".format(nombre,email,contenido),
                "",
                ["uinfop@gmail.com"],
                reply_to=[email],
                )
            
            confima=EmailMessage(
                "Mensaje desde App Django",
                "Su mensaje ha sido enviado correctamente",
                "",
                [email],
                reply_to=["uinfop@gmail.com"],
            )
            confima.extra_headers={'X-Priority':'1', 'Importance':'high'}
            
            try:
                mail.send()
                confima.send()
                return redirect("/contacto/?s")
            except:
                return redirect("/contacto/?n")

    return render(request,'contacto/contacto.html',{'miformulario': formulario_contacto})
