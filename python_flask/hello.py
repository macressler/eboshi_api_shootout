from flask import Flask
from flask.ext.mysql import MySQL
from flask import jsonify
import dateutil.parser as parser

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'eboshi_test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/api/test")
def hello():
    return "Hello world"

@app.route('/api/clients')
def clients():
    cursor = mysql.connect().cursor()
    cursor.execute('''SELECT * FROM clients''')
    ltpv = [tpv for tpv in cursor]
    lk = [ltpk[0] for ltpk in cursor.description]
    laResults = []
    for tpv in ltpv:
        attributes = {}
        for k, v in zip(lk, tpv):
            if k != 'id':
                attributes[k] = unicode(v)
            else:
                clientId = unicode(v)

        attributes['created_at'] = parser.parse(attributes['created_at']).isoformat()
        attributes['updated_at'] = parser.parse(attributes['updated_at']).isoformat()

        clients = {
            'type': 'clients',
            'id': clientId,
            'attributes': attributes
        }

        laResults.append(clients)
    return jsonify({ 'data': laResults })

if __name__ == "__main__":
    app.debug = True
    app.run(port=6969)
