
#* This server does not work because it does not have the
#* Flask mail username and password imported
#*
#* Our actual python server code is untracked on github because 
#* this can give anyone access to our gmail account
#* 

from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Message, Mail

mail = Mail()

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'peepeepoopoo'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = '' #! Gmail email name goes here
app.config["MAIL_PASSWORD"] = '' #! Gmail password goes here

mail.init_app(app)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/about/', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/contact-us/', methods=['GET', 'POST'])
def contact_us():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact-us.html', form=form)
        else:
            msg = Message(form.reason.data + ': ' + form.subject.data, sender='contact@example.com', recipients=[
                          'neighborz.help@gmail.com', form.email.data])
            msg.body = """
            Dear %s, you are receiving this email because you,
                 or someone pretending to be you filled out our
                 contact form on NeighborZ 
                 (https://xXTechGodSquadXx.pythonanywhere.com). 
                 If this was not you, please respond to this 
                 email saying that this was not you. 
              
                 Thanks, NeighborZ Staff.
            ---
            From: %s <%s>
            
            Reason: %s
            Body:
            %s
            """ % (form.email.data, form.name.data, form.email.data, form.reason.data, form.message.data)
            mail.send(msg)

            return '<h3>Message submitted, redirecting back to home page in 3 seconds. If your browser does not support auto redirecting, <a href="/../"> click here </a> </h3> <meta http-equiv="Refresh" content="3; url=/../" />'

    elif request.method == 'GET':
        return render_template('contact-us.html', form=form)


@app.route('/forum/', methods=['GET'])
def forum():
    return '<meta http-equiv="Refresh" content="0; url=https://neighborz.freeforums.net/" />'


@app.route('/sitemap/', methods=['GET'])
def sitemap():
    return render_template('sitemap.html')


@app.route('/gallery/', methods=['GET'])
def gallery():
    return render_template('gallery.html')
