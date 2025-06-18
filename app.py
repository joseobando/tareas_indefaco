from flask import Flask, render_template, request, redirect, jsonify
import json, os
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
    tareas_activas = [t for t in tareas if t['color'] != 'white']
    tareas_completadas = [t for t in tareas if t['color'] == 'white']
    return render_template('index.html', tareas=tareas_activas, completadas=tareas_completadas)

@app.route('/agregar', methods=['POST'])
def agregar():
    tareas = cargar_tareas()
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