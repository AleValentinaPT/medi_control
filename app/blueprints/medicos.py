from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Medico

bp_medicos = Blueprint('bp_medicos', __name__, template_folder='../templates')

@bp_medicos.route('/')
def listar():
    medicos = Medico.query.all()
    return render_template('medicos/index.html', medicos=medicos)

@bp_medicos.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        
        nuevo_medico = Medico(nombre=nombre, especialidad=especialidad)
        db.session.add(nuevo_medico)
        db.session.commit()
        return redirect(url_for('bp_medicos.listar'))
        
    return render_template('medicos/crear.html')

@bp_medicos.route('/eliminar/<int:id>')
def eliminar(id):
    medico = Medico.query.get_or_404(id)
    db.session.delete(medico)
    db.session.commit()
    return redirect(url_for('bp_medicos.listar'))