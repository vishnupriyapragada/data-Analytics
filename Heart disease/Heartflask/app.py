import pickle
from flask import Flask, request, render_template

flask_app = Flask(__name__)

@flask_app.route("/")
def Home():
    return render_template("index.html")
@flask_app.route('/forms/contact.php',methods=['POST'])
def handle_form_submission():
    name = request.form.get('name')
    email = request.form.get('email')
    subject=reuest.form.get('subject')
    message = request.form.get('message')

    # Perform form validation
    error_message = None
    if not name:
        error_message = "Name is required."
    elif not email:
        error_message = "Email is required."
    elif not subject:
        error_message = "Subject is required."
    elif not message:
        error_message = "Message is required."

    if error_message:
        # Display an error message to the user
        return render_template('index.html', error_message=error_message)
    else:
        # Data is valid, you can save it to a database or perform other actions
        # For example, you can return a thank-you message to the user
        return render_template('index.html', success_message="Thank you for your submission!")
if __name__ == "__main__":
    flask_app.run(debug=False,port=8000)