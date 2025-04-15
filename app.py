from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    prediction = None
    input_value = None

    if request.method == 'POST':
        input_value = request.form.get('input_value')
        # Simulation de prédiction
        prediction = float(input_value) * 2  # À remplacer par ton vrai modèle ML

    return render_template('dashboard.html', input_value=input_value, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
