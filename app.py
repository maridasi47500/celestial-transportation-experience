from flask import Flask, render_template, request
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_celestial_transportation_experience", methods=["GET","POST"])
def add_one_celestial_transportation_experience():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into celestial_transportation_experience (title,description,departurecity_id,arrivalcity_id,frequencetransport,wifi,bluetooth,planemode,cellulardata,hacker,race,gossip,artistic,outofhome,communication,datedebut,datefin,meansoftransport) values (:title,:description,:departurecity_id,:arrivalcity_id,:frequencetransport,:wifi,:bluetooth,:planemode,:cellulardata,:hacker,:race,:gossip,:artistic,:outofhome,:communication,:datedebut,:datefin,:meansoftransport)",request.form)
        user = query_db('select * from celestial_transportation_experience')
        return render_template("celestial_transportation_experienceform.html", celestial_transportation_experiences=user, one_user=one_user, the_title="add new celestial_transportation_experience")
    user = query_db('select * from celestial_transportation_experience')
    one_user = query_db("select * from celestial_transportation_experience limit 1", one=True)
    return render_template("celestial_transportation_experienceform.html", celestial_transportation_experiences=user, one_user=one_user, the_title="add new celestial_transportation_experience")

