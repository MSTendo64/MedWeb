from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AABB21405'

doctors = [
    {
        'id': 1,
        'name': 'Иванов Александр Петрович',
        'specialization': 'Терапевт',
        'experience': 15,
        'description': 'Врач высшей категории. Специалист по внутренним болезням.',
        'photo': 'doctor1.jpg'
    },
    {
        'id': 2,
        'name': 'Смирнова Елена Владимировна',
        'specialization': 'Кардиолог',
        'experience': 12,
        'description': 'Кандидат медицинских наук. Эксперт в области кардиологии.',
        'photo': 'doctor2.jpg'
    },
    {
        'id': 3,
        'name': 'Петров Дмитрий Сергеевич',
        'specialization': 'Хирург',
        'experience': 20,
        'description': 'Хирург высшей категории. Ведущий специалист по малоинвазивной хирургии.',
        'photo': 'doctor3.jpg'
    },
    {
        'id': 4,
        'name': 'Козлова Мария Игоревна',
        'specialization': 'Педиатр',
        'experience': 10,
        'description': 'Детский врач. Специалист по детским заболеваниям и профилактике.',
        'photo': 'doctor4.jpg'
    }
]

services = [
    {
        'id': 1,
        'name': 'Первичный прием терапевта',
        'description': 'Консультация врача-терапевта, осмотр, назначение обследования.',
        'price': 1500
    },
    {
        'id': 2,
        'name': 'УЗИ брюшной полости',
        'description': 'Ультразвуковое исследование органов брюшной полости.',
        'price': 2500
    },
    {
        'id': 3,
        'name': 'ЭКГ с расшифровкой',
        'description': 'Электрокардиограмма с консультацией кардиолога.',
        'price': 1200
    },
    {
        'id': 4,
        'name': 'Общий анализ крови',
        'description': 'Лабораторное исследование основных показателей крови.',
        'price': 800
    },
    {
        'id': 5,
        'name': 'Консультация кардиолога',
        'description': 'Прием специалиста по заболеваниям сердечно-сосудистой системы.',
        'price': 2000
    },
    {
        'id': 6,
        'name': 'Массаж лечебный',
        'description': 'Сеанс лечебного массажа (30 минут).',
        'price': 1500
    }
]

appointments = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services_page():
    return render_template('services.html', services=services)

@app.route('/doctors')
def doctors_page():
    return render_template('doctors.html', doctors=doctors)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':
        
        appointment_data = {
            'id': len(appointments) + 1,
            'full_name': request.form['full_name'],
            'phone': request.form['phone'],
            'doctor_id': int(request.form['doctor']),
            'date_time': request.form['date_time'],
            'notes': request.form['notes'],
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        appointments.append(appointment_data)
        
        return redirect(url_for('appointment_success'))
    
    return render_template('appointment.html', doctors=doctors)

@app.route('/appointment/success')
def appointment_success():
    return render_template('success.html')

@app.route('/admin/appointments')
def admin_appointments():
    return render_template('admin_appointments.html', appointments=appointments)

if __name__ == '__main__':
    app.run(debug=True, port=5000)