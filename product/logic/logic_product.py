from ..models import Product

def get_products():
    """
    Obtiene los productos ordenados por su 'score_de_confiabilidad' de mayor a menor y
    limita los resultados a los 10 primeros para mostrar solo los más relevantes.
    """
    queryset = Product.objects.all().order_by('-score_de_confiabilidad')[:10]
    return queryset

def create_product(form):
    """
    Crea un nuevo producto a partir del formulario validado y lo guarda en la base de datos.
    """
    product = form.save(commit=False)
    product.save()
    return product
