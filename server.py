from flask import Flask, render_template

app = Flask(__name__)

@app.route('/lists')
def render_lists():
    # Muy pronto, obtendremos datos de una base de datos, pero por ahora, estamos codificando datos
    estudiantes_info = [
        {'name' : 'Michael', 'edad' : 35},
        {'name' : 'John', 'edad' : 30 },
        {'name' : 'Mark', 'edad' : 25},
        {'name' : 'KB', 'edad' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], estudiantes = estudiantes_info)

if __name__ == '__main__':
    app.run(debug=True)