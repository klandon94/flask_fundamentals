from flask import Flask, render_template,session,request,redirect
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('gold.html')

@app.route('/process_money',methods=['POST'])
def process():
    property = request.form['property']
    goldEarned = 0
    activity = ''
    if property == 'farm':
        goldEarned = random.randint(10,20)
    elif property == 'cave':
        goldEarned = random.randint(5,10)
    elif property == 'house':
        goldEarned = random.randint(2,5)
    elif property == 'casino':
        goldEarned = random.randint(-50,50)

    if goldEarned >= 0:
        activity = "Earned " + str(goldEarned) + " golds from the " + property + "! (" + str(datetime.now()) + ")"
        color = 'green'
    else:
        activity = "Entered a casino and lost " + str(abs(goldEarned)) + " golds...Ouch... " + " (" + str(datetime.now()) + ")"
        color = 'red'

    dictionary = {'content':activity, 'class':color}
    # print("\n",dictionary,"\n")
    session['activities'].append(dictionary)
    session['gold'] += goldEarned

    return redirect('/')


    # property = request.form['property']
    # session['time'] = datetime.now()
    # if property == 'farm':
    #     session['gain'] = random.randint(10,20)
    #     session['gold'] += session['gain']
    #     session['activities'].append(f"Earned {session['gain']} golds from the farm! --- {session['time']}")
    # if property == 'cave':
    #     session['gain'] = random.randint(5,10)
    #     session['gold'] += session['gain']
    #     session['activities'].append(f"Earned {session['gain']} golds from the cave! --- {session['time']}")
    # if property == 'house':
    #     session['gain'] = random.randint(2,5)
    #     session['gold'] += session['gain']
    #     session['activities'].append(f"Earned {session['gain']} golds from the house! --- {session['time']}")
    # if property == 'casino':
    #     session['gain'] = random.randint(-50,50)
    #     if session['gain']<0:
    #         session['activities'].append(f"Entered a casino and lost {abs(session['gain'])} golds... Ouch... --- {session['time']}")
    #     else:
    #         session['activities'].append(f"Entered a casino and won {session['gain']} golds... Sweet! --- {session['time']}")
    #     session['gold'] += session['gain']

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    # run our server
    app.run(debug=True)