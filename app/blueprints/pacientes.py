from flask import Blueprint
bp_pacientes = Blueprint('bp_pacientes', __name__)
from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Paciente

bp_pacientes = Blueprint('bp_pacientes', __name__, template_folder='../templates')

@bp_pacientes.route('/')
def listar():
    pacientes = Paciente.query.all()
    return render_template('pacientes/index.html', pacientes=pacientes)

@bp_pacientes.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        
        nuevo_paciente = Paciente(nombre=nombre, telefono=telefono)
        db.session.add(nuevo_paciente)
        db.session.commit()
        return redirect(url_for('bp_pacientes.listar'))
        
    return render_template('pacientes/crear.html')

@bp_pacientes.route('/eliminar/<int:id>')
def eliminar(id):
    paciente = Paciente.query.get_or_404(id)
    db.session.delete(paciente)
    db.session.commit()
    return redirect(url_for('bp_pacientes.listar'))