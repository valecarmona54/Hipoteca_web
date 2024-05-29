"""
Routes and views for the flask application.
"""

from datetime import datetime
from sqlite3 import DatabaseError
from flask import Flask, render_template, request, redirect, url_for, session, flash
from src.view_web import app
from src.model.Calculations import MortgageLifetimeInverse, MortgageTemporaryReverse,MortgageSingleReverse
from email import message
from src.controller.database_manager import DatabaseManager
from src.controller.model_user import Usuario
from src.controller.model_reverse_mortage import model_reverse

db = DatabaseManager()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/session_home')
def session_home():
    return render_template(
        'index_login.html',
        title='Home Page Login',
        year=datetime.now().year,
    )

@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        try:
            data = {
                'id_usuario': request.form['idusuario'],
                'contrasena': request.form['contrasena'],
                'edad': request.form['edad'],
                'nombre_usuario': request.form['nombre_usuario'],
                'genero': request.form['genero']
            }
            
            if Usuario.create('usuario', data):
                return redirect(url_for('login_user'))
            else:
             return render_template('register.html', title='Registro', message=f"El usuario con ID {request.form['idusuario']} ya se encuentra registrado", year=datetime.now().year)

        except Exception as e:
            print(f"Error en el formulario de registro: {e}")
            return render_template('register.html', title='Registro', message='Error en el formulario de registro. Intente nuevamente.', year=datetime.now().year)
    
    return render_template('register.html', title='Registro', message='Por favor, complete el formulario de registro.', year=datetime.now().year)

@app.route('/login_user', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        id_usuario = request.form['idusuario']
        contrasena = request.form['contrasena']
        
        usuario = Usuario.find_by_credentials(id_usuario, contrasena)
        
        if usuario:
            session['logged_in'] = True
            session['id_usuario'] = id_usuario
            return redirect(url_for('session_home'))
        else:
            return render_template('login.html', title='Inicia Sesion', year=datetime.now().year, error='ID de usuario o contrasena incorrectos.')
    
    return render_template('login.html', title='Inicia Sesion', year=datetime.now().year)




@app.route('/hi_lifetime_cal', methods=['GET', 'POST'])
def hi_lifetime_cal():
    if request.method == 'POST':
        try:
            id_usuario = str(session['id_usuario'])
            total_amount = float(request.form['total_amount'])
            interest = float(request.form['interest'])
            interest_housing = float(request.form['interest_housing'])
            age = Usuario.get_field_by_id(id_usuario, "edad")
            gender = Usuario.get_field_by_id(id_usuario, "genero")

            monthly_payment = MortgageLifetimeInverse(total_amount, interest, interest_housing, age, gender)

            return render_template('lifetime.html', 
                                   monthly_payment=monthly_payment,
                                   total_amount=total_amount, 
                                   interest=interest, 
                                   interest_housing=interest_housing, 
                                   age=age, 
                                   gender=gender, 
                                   tipo="Hipoteca Inversa Vitalicia",
                                   saved=False,
                                   calculated=True)
        except Exception as e:
           print(f"Error al calcular la hipoteca: {e}")
           return redirect(url_for('hi_lifetime_cal'))
    
    return render_template('lifetime.html', 
                           title='HI VITALICA', 
                           message='Por favor, ingrese los datos solicitados.', 
                           year=datetime.now().year)

@app.route('/save_info_lifetime', methods=['POST'])
def save_info_lifetime():
    try:
        id_usuario = str(session['id_usuario'])
        total_amount = float(request.form.get('total_amount'))
        interest = float(request.form.get('interest'))
        interest_housing = float(request.form.get('interest_housing'))
        age = int(request.form.get('age'))
        gender = request.form.get('gender')
        monthly_payment = float(request.form.get('monthly_payment'))
        
        print(id_usuario, total_amount, interest, interest_housing, age, gender, monthly_payment)

        data = {
            'id_usuario': id_usuario,
            'total_amount': total_amount,
            'interest': interest,
            'interest_housing': interest_housing,
            'age': age,
            'result': monthly_payment
        }
        print(data)
        
        model_reverse.create("mortgage_lifetime_inverse", data)
        return render_template('lifetime.html',saved=True,calculated=False)
    except Exception as e:
        return f"Error al guardar la informacion: {e}", 500




@app.route('/hi_temporary_cal', methods=['GET', 'POST'])
def hi_temporary_cal():
    if request.method == 'POST':
        try:
            
            id_usuario = str(session['id_usuario'])
            total_amount = float(request.form['total_amount'])
            interest = float(request.form['interest'])
            interest_housing = float(request.form['interest_housing'])
            quotas = int(request.form['quotas'])
            monthly_payment = MortgageTemporaryReverse(total_amount, interest, interest_housing, quotas)
            
            return render_template('temporary.html', 
                                   monthly_payment=monthly_payment,
                                   total_amount=total_amount, 
                                   interest=interest, 
                                   interest_housing=interest_housing, 
                                   quotas = quotas,
                                   tipo="Hipoteca Inversa Temporal",
                                   saved=False,
                                   calculated=True)
        except Exception as e:
           print(f"Error al calcular la hipoteca: {e}")
           return redirect(url_for('hi_temporary_cal'))
    
    return render_template('temporary.html', 
                           title='HI TEMPORAL', 
                           message='Por favor, ingrese los datos solicitados.', 
                           year=datetime.now().year)

@app.route('/save_info_temporary', methods=['POST'])
def save_info_temporary():
    try:
        id_usuario = str(session['id_usuario'])
        total_amount = float(request.form.get('total_amount'))
        interest = float(request.form.get('interest'))
        interest_housing = float(request.form.get('interest_housing'))
        quotas = int(request.form.get('quotas'))
        monthly_payment = float(request.form.get('monthly_payment'))
        
        print(id_usuario, total_amount, interest, interest_housing, quotas, monthly_payment)

        data = {
            'id_usuario': id_usuario,
            'total_amount': total_amount,
            'interest': interest,
            'interest_housing': interest_housing,
            'quotas': quotas,
            'result': monthly_payment
        }
        print(data)
        
        model_reverse.create("mortgage_temporary_reverse", data)
        return render_template('temporary.html',saved=True,calculated=False)
    except Exception as e:
        return f"Error al guardar la informacion: {e}", 500




@app.route('/hi_unique_cal', methods=['GET', 'POST'])
def hi_unique_cal():
    if request.method == 'POST':
        try:
            
            id_usuario = str(session['id_usuario'])
            total_amount = float(request.form['total_amount'])
            interest_housing = float(request.form['interest_housing'])
            
            monthly_payment = MortgageSingleReverse(total_amount, interest_housing)
            
            return render_template('unique.html', 
                                   monthly_payment=monthly_payment,
                                   total_amount=total_amount, 
                                   interest_housing=interest_housing, 
                                   tipo="Hipoteca Inversa Unica",
                                   saved=False,
                                   calculated=True)
        except Exception as e:
           print(f"Error al calcular la hipoteca: {e}")
           return redirect(url_for('hi_unique_cal'))
    
    return render_template('unique.html', 
                           title='HI UNICAL', 
                           message='Por favor, ingrese los datos solicitados.', 
                           year=datetime.now().year)

@app.route('/save_info_unique', methods=['POST'])
def save_info_unique():
    try:
        id_usuario = str(session['id_usuario'])
        total_amount = float(request.form.get('total_amount'))
        interest_housing = float(request.form.get('interest_housing'))
        monthly_payment = float(request.form.get('monthly_payment'))
        
        print(id_usuario, total_amount, interest_housing, monthly_payment)

        data = {
            'id_usuario': id_usuario,
            'total_amount': total_amount,
            'interest_housing': interest_housing,
            'result': monthly_payment
        }
        print(data)
        
        model_reverse.create("mortgage_single_reverse", data)
        return render_template('unique.html',saved=True,calculated=False)
    except Exception as e:
        return f"Error al guardar la informacion: {e}", 500
    



@app.route('/calculations_user', methods=['GET'])
def calculations_user():
    id_usuario = str(session['id_usuario'])

    if 'id_usuario' not in session:
        return redirect(url_for('login'))


    try:
        hipoteca_inversa_vitalicia = db.get_data('mortgage_lifetime_inverse', id_usuario)
        hipoteca_inversa_temporal = db.get_data('mortgage_temporary_reverse', id_usuario)
        hipoteca_inversa_unica = db.get_data('mortgage_single_reverse', id_usuario)
        print(hipoteca_inversa_vitalicia)
    except Exception as e:
        print(f"Error fetching data: {e}")
        hipoteca_inversa_vitalicia = []
        hipoteca_inversa_temporal = []
        hipoteca_inversa_unica = []

    return render_template('calculations_user.html', 
                           hipoteca_inversa_vitalicia=hipoteca_inversa_vitalicia, 
                           hipoteca_inversa_temporal=hipoteca_inversa_temporal, 
                           hipoteca_inversa_unica=hipoteca_inversa_unica)

@app.route('/delete_calculo/<table>/<int:id>', methods=['POST'])
def delete_calculo(table, id):
    try:
        db.delete_data(table, id)
        flash('Cálculo eliminado correctamente.', 'success')
    except Exception as e:
        flash(f'Error al eliminar el calculo: {e}', 'danger')
    return redirect(url_for('calculations_user'))

@app.route('/update_user', methods=['GET', 'POST'])
def update_user():
    id_usuario = str(session.get('id_usuario'))

    if request.method == 'POST':
        contrasena = request.form['contrasena']
        edad = request.form['edad']
        nombre_usuario = request.form['nombre_usuario']
        genero = request.form['genero']

        data = {
            'contrasena': contrasena,
            'edad': edad,
            'nombre_usuario': nombre_usuario,
            'genero': genero
        }

        try:
            db.update_data('usuario', data, id_usuario)
            flash('Usuario actualizado correctamente.', 'success')
        except Exception as e:
            flash(f'Error al actualizar el usuario: {e}', 'danger')

        return redirect(url_for('update_user'))

    user_data = db.get_data('usuario', id_usuario)
    if user_data:
        user = user_data[0]
        user_dict = {
            'id_usuario': id_usuario,
            'contrasena': user[1],
            'edad': user[2],
            'nombre_usuario': user[3],
            'genero': user[4]
        }
        return render_template('update_user.html', title='Actualizar Usuario', user=user_dict)
    else:
        flash('Usuario no encontrado.', 'danger')
        return redirect(url_for('update_user'))



