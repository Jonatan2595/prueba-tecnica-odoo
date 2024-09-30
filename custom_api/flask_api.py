from flask import Flask, jsonify, request
import xmlrpc.client

app = Flask(__name__)

# Configura la conexión a Odoo
url = 'http://localhost:8069'
db = 'prueba-tecnica'
username = 'jm25prueba'
password = 'e191b08851fc4e2ebdc280fcceab75220278ffe2'

@app.route('/api/inventory', methods=['GET'])
def get_data():

# Conectar a Odoo
    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# Aquí puedes hacer una llamada a Odoo, por ejemplo, obtener registros
    records = models.execute_kw(db, uid, password,
    'tu.modelo', 'search_read', [[]], {'fields': ['campo1', 'campo2']})

    return jsonify(records)

if __name__ == '__main__':
    app.run(debug=True)