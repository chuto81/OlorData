from flask import Flask, render_template, request, flash, redirect
from contact_model import Contact
from google.cloud import ndb

app = Flask(__name__)
app.secret_key = 'some_secret'
app.debug = True

@app.route(r'/', methods=['GET'])
def contact_book():
    return render_template('contact_book.html')

@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():
    if request.form:
        identification = request.form.get('identification')
        name = request.form.get('name')
        gender = request.form.get('gender')
        age = request.form.get('age')
        company = request.form.get('company')
        currentdate = request.form.get('currentdate')

        contact = (identification, name, gender, age, company, currentdate)

        return render_template('prueba_1.html', contact=contact)

    return render_template('add_contact.html')

@app.route(r'/prueba1', methods=['GET', 'POST'])
def prueba1():
    if request.form:
        identification = request.form.get('identification')
        name = request.form.get('name')
        gender = request.form.get('gender')
        age = request.form.get('age')
        company = request.form.get('company')
        currentdate = request.form.get('currentdate')
        test1 = request.form.get('prueba_1')

        contact = (identification, name, gender, age, company, currentdate, test1)

        return render_template('prueba_2.html', contact=contact)

    return render_template('prueba_1.html')

@app.route(r'/prueba2', methods=['GET', 'POST'])
def prueba2():
    if request.form:
        identification = request.form.get('identification')
        name = request.form.get('name')
        gender = request.form.get('gender')
        age = request.form.get('age')
        company = request.form.get('company')
        currentdate = request.form.get('currentdate')
        test1 = request.form.get('test1')
        test2 = request.form.get('prueba_2')

        contact = (identification, name, gender, age, company, currentdate, test1, test2)

        return render_template('prueba_3.html', contact=contact)

    return render_template('prueba_2.html')

@app.route(r'/prueba3', methods=['GET', 'POST'])
def prueba3():
    if request.form:
        identification = request.form.get('identification')
        name = request.form.get('name')
        gender = request.form.get('gender')
        age = request.form.get('age')
        company = request.form.get('company')
        currentdate = request.form.get('currentdate')
        test1 = request.form.get('test1')
        test2 = request.form.get('test2')
        test3 = request.form.get('prueba_3')

        contact = (identification, name, gender, age, company, currentdate, test1, test2, test3)

        return render_template('prueba_4.html', contact=contact)

    return render_template('prueba_3.html')

@app.route(r'/prueba4', methods=['GET', 'POST'])
def prueba4():

    import time
    global ahora
    ahora = time.strftime("%y/%m/%d %H:%M:%S")

    if request.form:
        identification = request.form.get('identification')
        name = request.form.get('name')
        gender = request.form.get('gender')
        age = request.form.get('age')
        company = request.form.get('company')
        currentdate = request.form.get('currentdate')
        test1 = request.form.get('test1')
        test2 = request.form.get('test2')
        test3 = request.form.get('test3')
        test4 = request.form.get('prueba_4')
        time = ahora

        client = ndb.Client()
        with client.context():
            contact = Contact(identification=identification,
                              name=name, 
                              gender=gender,
                              age=age,
                              company=company,
                              currentdate=currentdate,
                              test1=test1,
                              test2=test2,
                              test3=test3,
                              test4=test4,
                              time=time)
            contact.put()

        usuario = (identification, name, company, currentdate)

        p4 = int(test4)
        p3 = int(test3)
        p2 = int(test2)
        p1 = int(test1)
        final = p1 + p2 + p3 + p4

        if final == 4:
            flash('POSITIVO PARA ANOSMIA')
        elif final == 3 or final == 2:
            flash('POSITIVO PARA HIPOSMIA')
        elif final == 1 or final == 0:
            flash('NEGATIVO')
        return render_template('final.html', usuario=usuario)

    return render_template('prueba_4.html')

if __name__ == '__main__':
    app.run()