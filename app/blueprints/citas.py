from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Cita, Medico, Paciente

bp_citas = Blueprint('bp_citas', __name__, template_folder='../templates')

@bp_citas.route('/')
def listar():
    citas = Cita.query.all()
    return render_template('citas/index.html', citas=citas)

@bp_citas.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        fecha = request.form['fecha']
        hora = request.form['hora']
        medico_id = request.form['medico_id']
        paciente_id = request.form['paciente_id']
        
        nueva_cita = Cita(fecha=fecha, hora=hora, medico_id=medico_id, paciente_id=paciente_id)
        db.session.add(nueva_cita)
        db.session.commit()
        return redirect(url_for('bp_citas.listar'))
        
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    return render_template('citas/crear.html', medicos=medicos, pacientes=pacientes)

@bp_citas.route('/eliminar/<int:id>')
def eliminar(id):
    cita = Cita.query.get_or_404(id)
    db.session.delete(cita)
    db.session.commit()
    return redirect(url_for('bp_citas.listar'))