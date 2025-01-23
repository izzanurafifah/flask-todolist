from flask import Flask, render_template, request, redirect, url_for, jsonify
import os

app = Flask(__name__)

tasks = []

# Home page to display the to-do list
@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

# Add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task')
    if task_name:
        tasks.append({"id": len(tasks) + 1, "name": task_name, "completed": False})
    return redirect(url_for('home'))

# Mark a task as completed
@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            break
    return redirect(url_for('home'))

# Delete a task
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
