from flask import Flask, render_template, request, redirect, url_for, flash , session
from db import add_task,delete_task,edit_task,show_tasks_db
import json


# Create a Flask Instance
# Edited by harshit
# Edited by Ishant
# Edited by Riyaz

app = Flask(__name__)
app.secret_key="This_secret_key"


# Create a route decorator
@app.route("/")
def home1():
    return render_template("home1.html")


@app.route('/show_tasks_web',methods=["GET","POST"])
def show_tasks_web():
    task_details=show_tasks_db(1)
    if task_details[0]==True:
        return render_template('tasks1.html',tasks=[task_details[1]])
    else:
        return "An error occured"
    
@app.route("/add_task_template",methods=['GET','POST'])
def add_task_template():
    return render_template("add_task1.html")


@app.route("/add_task_auth",methods=['GET','POST']) 
def add_task_auth():
    if request.method=="POST":
        task_title=request.form.get("task_title")
        task_description=request.form.get("task_description")
        task_deadline=request.form.get("task_deadline")
        
        #task_details->[0]=user_id(foreign key),[1]=task_title,[2]=task_description,[3]=date
        task_details=[1,task_title,task_description,task_deadline]
        #print(task_details)
        feedback=add_task(task_details)
        #print(feedback)
        return redirect(url_for("add_task_template"))
    else:
        return render_template("add_task1.html")

        


@app.route('/del_task/<int:task_id>',methods=['GET','POST'])
def del_task(task_id):
    feedback=delete_task(task_id)
    return redirect(url_for("home"))

@app.route('/complete_task/<int:task_id>/<int:update_code>',methods=['GET','POST'])
def complete_task(task_id,update_code):
    edit_code=2
    task_details=[update_code,task_id]
    feedback=edit_task(edit_code,task_details)
    return redirect(url_for('home'))

# now render feature.html
@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)
    
