# controllers.py

from aplicacao import app
from flask import render_template
from flask import redirect
from flask import request
from models import Presenca


@app.route('/')
def index():
    presencas = Presenca.recupera_todos()

    
    menu = []
   
    menu.append({'active': True,
                 'href': '/',
                 'texto': 'Presenças Registradas'})
    menu.append({'active': False,
                 'href': '/presenca',
                 'texto': 'Registrar Presenças'})
    menu.append({'active': False,
                 'href': '/pedro',
                 'texto': 'Pedro'})
    menu.append({'active': False,
                 'href': '/andre',
                 'texto': 'Andre'})
    menu.append({'active': False,
                 'href': '/ana',
                 'texto': 'Ana'})
    menu.append({'active': False,
                 'href': '/guilherme',
                 'texto': 'Guilherme'})
    

   
    context = {'presenca': 'Presenças Registradas',
               'menu': menu,
               'presencas': presencas}

    return render_template('index.html', **context)


@app.route('/presenca')
def presenca():
   
    menu = []
   
    menu.append({'active': False,
                 'href': '/',
                 'texto': 'Presenças Registradas'})
    menu.append({'active': True,
                 'href': '/presenca',
                 'texto': 'Registrar Presenças'})
    menu.append({'active': False,
                 'href': '/pedro',
                 'texto': 'Pedro'})
    menu.append({'active': False,
                 'href': '/andre',
                 'texto': 'Andre'})
    menu.append({'active': False,
                 'href': '/ana',
                 'texto': 'Ana'})
    menu.append({'active': False,
                 'href': '/guilherme',
                 'texto': 'Guilherme'})

    
    context = {'presenca': 'Registrar Presença',
               'menu': menu}

    return render_template('presenca.html', **context)


@app.route('/presenca/gravar', methods=['POST'])
def gravar_presenca():
    email_f = request.form['email']
    presenca_f = request.form['presenca']
    resposta_f = request.form['resposta']
    comentarios_f = request.form['comentarios']
    presenca = Presenca(email_f, presenca_f, resposta_f, comentarios_f)
    presenca.gravar()
    return redirect('/')


@app.route('/pedro')
def pedro():
    
    menu = []
   
    menu.append({'active': False,
                 'href': '/',
                 'texto': 'Presenças Registradas'})
    menu.append({'active': False,
                 'href': '/presenca',
                 'texto': 'Registrar Presenças'})
    menu.append({'active': True,
                 'href': '/pedro',
                 'texto': 'Pedro'})
    menu.append({'active': False,
                 'href': '/andre',
                 'texto': 'Andre'})
    menu.append({'active': False,
                 'href': '/ana',
                 'texto': 'Ana'})
    menu.append({'active': False,
                 'href': '/guilherme',
                 'texto': 'Guilherme'})


   
    context = {'presenca': 'Sobre - Pedro',
               'menu': menu}

    return render_template('pedro.html', **context)


@app.route('/andre')
def andre():
   
    menu = []
   
    menu.append({'active': False,
                 'href': '/',
                 'texto': 'Presenças Registradas'})
    menu.append({'active': False,
                 'href': '/presenca',
                 'texto': 'Registrar Presenças'})
    menu.append({'active': False,
                 'href': '/pedro',
                 'texto': 'Pedro'})
    menu.append({'active': True,
                 'href': '/andre',
                 'texto': 'Andre'})
    menu.append({'active': False,
                 'href': '/ana',
                 'texto': 'Ana'})
    menu.append({'active': False,
                 'href': '/guilherme',
                 'texto': 'Guilherme'})


    
    context = {'presenca': 'Sobre - Andre',
               'menu': menu}

    return render_template('andre.html', **context)


@app.route('/ana')
def ana():
    
    menu = []
   
    menu.append({'active': False,
                 'href': '/',
                 'texto': 'Presenças Registradas'})
    menu.append({'active': False,
                 'href': '/presenca',
                 'texto': 'Registrar Presenças'})
    menu.append({'active': False,
                 'href': '/pedro',
                 'texto': 'Pedro'})
    menu.append({'active': False,
                 'href': '/andre',
                 'texto': 'Andre'})
    menu.append({'active': True,
                 'href': '/ana',
                 'texto': 'Ana'})
    menu.append({'active': False,
                 'href': '/guilherme',
                 'texto': 'Guilherme'})

    
    context = {'presenca': 'Sobre - Ana',
               'menu': menu}

    return render_template('ana.html', **context)



@app.route('/guilherme')
def ana():
    
    menu = []
   
    menu.append({'active': False,
                 'href': '/',
                 'texto': 'Presenças Registradas'})
    menu.append({'active': False,
                 'href': '/presenca',
                 'texto': 'Registrar Presenças'})
    menu.append({'active': False,
                 'href': '/pedro',
                 'texto': 'Pedro'})
    menu.append({'active': False,
                 'href': '/andre',
                 'texto': 'Andre'})
    menu.append({'active': False,
                 'href': '/ana',
                 'texto': 'Ana'})
    menu.append({'active': True,
                 'href': '/guilherme',
                 'texto': 'Guilherme'})

    
    context = {'presenca': 'Sobre - Guilherme',
               'menu': menu}

    return render_template('guilherme.html', **context)




app.run()
