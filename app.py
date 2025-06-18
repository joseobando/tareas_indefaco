from flask import Flask, render_template, request, redirect, jsonify
<<<<<<< HEAD
import json, os
=======
import os
import json
>>>>>>> a6585d755692f2117a329c8960e77a5fee8a43fb
from datetime import datetime

app = Flask(__name__)
DATA_FILE = 'tareas.json'

def cargar_tareas():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def guardar_tareas(tareas):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    tareas = cargar_tareas()
<<<<<<< HEAD
    tareas_activas = [t for t in tareas if t['color'] != 'white']
    tareas_completadas = [t for t in tareas if t['color'] == 'white']
    return render_template('index.html', tareas=tareas_activas, completadas=tareas_completadas)
=======
    activas = [t for t in tareas if not t['completada']]
    completadas = [t for t in tareas if t['completada']]
    return render_template('index.html', tareas=activas, completadas=completadas)
>>>>>>> a6585d755692f2117a329c8960e77a5fee8a43fb

@app.route('/agregar', methods=['POST'])
def agregar():
    tareas = cargar_tareas()
<<<<<<< HEAD
    nueva_tarea = {
        'texto': request.form['texto'],
        'color': request.form['color'],
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'autor': request.form.get('autor', 'Desconocido')
    }
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    return redirect('/')

@app.route('/completar/<int:indice>', methods=['POST'])
def completar(indice):
    tareas = cargar_tareas()
    if 0 <= indice < len(tareas):
        tareas[indice]['color'] = 'white'
        guardar_tareas(tareas)
    return redirect('/')

@app.route('/eliminar/<int:indice>', methods=['POST'])
def eliminar(indice):
    tareas = cargar_tareas()
    if 0 <= indice < len(tareas):
        tareas.pop(indice)
        guardar_tareas(tareas)
    return redirect('/')

if __name__ == '__main__':
    app.run()
=======
    nueva = {
        'id': len(tareas) + 1,
        'texto': request.form['texto'],
        'prioridad': request.form['prioridad'],
        'comentarios': [],
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'completada': False,
        'autor': request.form.get('autor', 'Usuario')
    }
    tareas.append(nueva)
    guardar_tareas(tareas)
    return redirect('/')

@app.route('/completar/<int:id>', methods=['POST'])
def completar(id):
    tareas = cargar_tareas()
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['completada'] = True
            break
    guardar_tareas(tareas)
    return redirect('/')

@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    tareas = cargar_tareas()
    tareas = [t for t in tareas if t['id'] != id]
    guardar_tareas(tareas)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> a6585d755692f2117a329c8960e77a5fee8a43fb
