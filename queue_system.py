from flask import Flask, request, redirect, render_template
from datetime import datetime

app = Flask(__name__, template_folder='/Users/guledali/Desktop/untitled folder/queue system test/templates')

queue = []
filtered_queue = []

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
  name = request.form['name']
  subject = request.form['subject']
  phone_number = request.form['phone']
  number_guests = request.form['guests']
  time = datetime.now()
  time = time.strftime("%I:%M %p")
  newsletter = request.form['newsletter']
  queue.append((name,phone_number,number_guests,subject, time, newsletter))
  filtered_queue.append((name,time))
  return redirect('/')

@app.route('/remove', methods=['POST'])
def remove():
  index = int(request.form['id_tag'])
  queue.pop(index - 1)
  filtered_queue.pop(index - 1)
  return redirect('/admin_view')

@app.route('/admin_view')
def admin_view():
  return render_template('admin_view.html', queue=queue)

@app.route('/view')
def view():
  return render_template('view.html', filtered_queue=filtered_queue)

if __name__ == '__main__':
  app.run()