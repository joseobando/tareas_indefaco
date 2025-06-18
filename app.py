from flask import Flask, render_template, request, redirect, jsonify
import os
import json
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
    activas = [t for t in tareas if not t['completada']]
    completadas = [t for t in tareas if t['completada']]
    return render_template('index.html', tareas=activas, completadas=completadas)

@app.route('/agregar', methods=['POST'])
def agregar():
    tareas = cargar_tareas()
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