"""
flasking
"""
from flask import Flask, request


app = Flask(__name__)


# TODO: Implementiere eine Route für '/', die bei einem GET-Request den Text 'Willkommen bei meiner Flask-App!' zurückg
@app.route('/', methods=['GET'])
def home():
    """Gibt den Text 'Willkommen bei meiner Flask-App!' zurück."""
    return 'Willkommen bei meiner Flask-App!'


# TODO: Implementiere eine Route für '/info', die bei einem GET-Request den Text 'Dies ist die Info-Seite.' zurückgibt.
@app.route('/info', methods=['GET'])
def info():
    """Gibt den Text 'Dies ist die Info-Seite.' zurück."""
    return 'Dies ist die Info-Seite.'


# TODO: Implementiere eine Route für '/user/<username>', die bei einem GET-Request den Text 'Hallo, [username]!' zurück
@app.route('//user/<username>', methods=['GET'])
def user(username):
    """Gibt den Text 'Hallo, [username]!' zurück, wobei [username] durch den in der URL angegebenen Benutzernamen ."""
    return f'Hallo, {username}!'


# TODO: Implementiere eine Route für '/post', die bei einem POST-Request den Text 'Daten erfolgreich erhalten!' zurückt.
@app.route('/post', methods=['POST'])
def post_data():
    """Akzeptiert Daten und gibt den Text 'Daten erfolgreich erhalten!' zurück."""
    return 'Daten erfolgreich erhalten!'


# TODO: Implementiere eine Route für '/feedback', die bei einem GET-Request den Text 'Bitte geben Sie Ihr Feedback
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    """Bei einem GET-Request gibt es den Text 'Bitte geben Sie Ihr Feedback ab.' zurück. Bei einem POST-Request."""
    if request.method == 'GET':
        return 'Bitte geben Sie Ihr Feedback ab.'
    elif request.method == 'POST':
        return 'Danke für Ihr Feedback!'


# TODO: Implementiere eine Route für '/item/<int:item_id>', die bei einem GET-Request den Text 'Artikel-ID: [item
@app.route('/item/<int:item_id>', methods=['GET'])
def item(item_id):
    """Gibt den Text 'Artikel-ID: [item_id]' zurück, wobei [item_id] durch die in der URL angegebene Artikel-"""
    return f'Artikel-ID: {item_id}'


if __name__ == '__main__':
    app.run(debug=True)
