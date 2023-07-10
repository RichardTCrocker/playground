

from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/play')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<color>')
@app.route('/play/<color>/<int:num>')
@app.route('/play/<color>')
def play(num=3, color='blue'):
    return render_template("index.html", num=num, color=color)



# @app.route('/get_user/<int:index>')
# def get_user(index):
#     return list[index]

# @app.route('/template/<color>/<int:num>')
# def show_temp(color, num):
#     return render_template("index.html",string="Hello", num=num, color=color)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.