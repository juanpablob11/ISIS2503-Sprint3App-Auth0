from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import ClienteForm
from .logic.client_logic import get_clientes, get_cliente, create_cliente
from django.contrib.auth.decorators import login_required
# from .auth import get_role  # Asumiendo que este método está definido en un módulo de autenticación

@login_required
def cliente_list(request):
    if get_role(request) == "gerente":
        clientes = get_clientes()
        return render(request, 'Client/clients.html', {'cliente_list': clientes})
    else:
        return HttpResponse("Unauthorized User", status=403)

@login_required
def single_cliente(request, id):
    if get_role(request) == "gerente":
        cliente = get_cliente(id)
        if cliente:
            return render(request, 'Client/client.html', {'cliente': cliente})
        else:
            return HttpResponse("Cliente no encontrado", status=404)
    else:
        return HttpResponse("Unauthorized User", status=403)

@login_required
def cliente_create(request):
    if get_role(request) == "gerente":
        if request.method == 'POST':
            form = ClienteForm(request.POST)
            if form.is_valid():
                create_cliente(form)
                messages.success(request, 'Cliente creado con éxito')
                return redirect('clientList')
            else:
                messages.error(request, form.errors)
        else:
            form = ClienteForm()
        return render(request, 'Client/clientCreate.html', {'form': form})
    else:
        return HttpResponse("Unauthorized User", status=403)
