from flask import Flask


app = Flask(__name__)
app.config.from_object(__name__)

# configuração
app.config.update(DATABASE='banco_presenca.db', DEBUG=True)
