from ..models import Cliente

def get_clientes():
    """ Retorna una lista de todos los clientes registrados en la base de datos. """
    return Cliente.objects.all()

def get_cliente(id):
    """ Retorna un solo cliente basado en su ID. """
    return Cliente.objects.filter(pk=id).first()

def create_cliente(form):
    """ Crea un nuevo cliente a partir de un formulario validado y lo guarda en la base de datos. """
    cliente = form.save(commit=False)
    cliente.save()
    return cliente
