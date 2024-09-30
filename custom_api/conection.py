import xmlrpc.client

url = 'http://localhost:8069'
db = 'prueba-tecnica'
username = 'jm25prueba'
password = 'JMprueba25.'

# Conectar al servidor
try:
    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
    print('¡CONEXION CORRECTA! :D')
except:
    print('¡CONEXION INCORRECTA! :C')
finally:
    print('¡FIN!.')

products = models.execute_kw(db, uid, password,
    'product.template', 'search_read',
    [[]], {'fields': ['name', 'qty_available']})

for product in products:
    print(f"Producto: {product['name']}, Cantidad disponible: {product['qty_available']}")