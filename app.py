from flask import Flask,request,render_template,redirect,url_for,abort
from models import db, Student

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="postgresql://brian:brian@localhost:5432/student"
app.config["DATABASE_TRACK_MODIFICATIONS"]=False
db.init_app(app)



@app.before_first_request
def create_table():
    db.create_all()


@app.route('/create',methods=['GET', 'POST'] )
def create():
    if request.method=='GET':
        return render_template('create.html')

    if request.method=='POST':
        hobby=request.form.getlist('hobbies')  
        hobbies=",".join(map(str, hobby)) 
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        email=request.form['email']
        password=request.form['password']
        gender=request.form['gender']
        country=request.form['country']

        students=Student(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            gender=gender,
            hobbies=hobbies,
            country=country
        )
        db.session.add(students)
        db.session.commit()
        return redirect('/')

@app.route('/students/<int:id>/delete',methods=['GET', 'POST'])
def delete(id):
    students=Student.query.filter(Student.id==id).one_or_none()
    if request.method=='POST':
        if students:
            db.session.delete(students)
            db.session.commit()
            return redirect('/')

    return render_template('delete.html')
            
@app.route('/students/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    student=Student.query.filter(Student.id==id).one_or_none()
    print('hello')


    if request.method=='POST':
        db.session.delete(student)
        db.session.commit()

        if student:
            hobby=request.form.getlist('hobbies')  
            hobbies=",".join(map(str, hobby)) 
            first_name=request.form['first_name']
            last_name=request.form['last_name']
            email=request.form['email']
            password=request.form['password']
            gender=request.form['gender']
            country=request.form['country']

            students=Student(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                gender=gender,
                hobbies=hobbies,
                country=country
            )
            db.session.add(students)
            db.session.commit()
            return redirect('/')
        return f"student with ={id} does not exist"

    return render_template('update.html', student=student)


@app.route('/')
def get_student():
    students=Student.query.all()
    return render_template('index.html', students=students)    