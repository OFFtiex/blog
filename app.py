from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    conn = sqlite3.connect('blog.sqlite')
    cur = conn.cursor()
    cur.execute("""SELECT hello, about FROM main LIMIT 1;""")
    name = 'Создатель сайта: Герман Маслов!'
    text = 'Привет, меня зовут Герман. Я из города Калиниград. Мне 14 лет. Я люблю плаванье и видеоигры!'

    for hello, about in cur.fetchall():
        name = hello
        text = about

    conn.close()

    context = {
        'hello': name,
        'user': 'John',
        'about': text
    }
    return render_template("index.html", **context)


@app.route('/blog/')
def blog():
    conn = sqlite3.connect('blog.sqlite')
    cur = conn.cursor()
    cur.execute("""SELECT head, text, image FROM blog where visible ==?;""", (1,));
    cur.execute("""SELECT head, story, image FROM blog where visible == 1;""");

    stories = []
    for head, story, image in cur.fetchall():
        stories.append({'head': head, 'text': story, 'img': image})



    conn.close()

    context = {}



    stories = [
         {
             'head': 'История 1',
             'text': 'Однажды я гулял по лесу и увидел белку. Она испугалась меня и убежала.',
             'img': '../static/img/1.jpeg'
         },

         {
             'head': 'История 2',
             'text': 'На мой день рождения меня повезли на картинг. Там было очень интересно. Мне понравилось.',
             'img': '../static/img/2.jpeg'
         },
         {
             'head': 'История 3',
             'text': 'Летом во время купания меня ужалила медуза. Больше я в море с медузами не захожу.',
             'img': '../static/img/3.jpeg'
         }
     ]

    context['stories'] = stories

    return render_template("blog.html", **context)


@app.route('/about/')
def about():
    conn = sqlite3.connect('blog.sqlite')
    cur = conn.cursor()
    cur.execute("""SELECT phone, email FROM about LIMIT 1;""")
    number = ''
    address = ''

    for phone, email in cur.fetchall():
        number = phone
        address = email

    conn.close()


    context = {}
    info = [
        {
            'email': address,
            'number': number
        }
    ]

    context['info'] = info

    return render_template("about.html", **context)
