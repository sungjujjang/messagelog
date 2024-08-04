from flask import Flask, render_template, request, redirect, url_for
from threading import Thread
import sqlite3

app = Flask('')

def checkint(vars):
    try:
        int(vars)
    except:
        return False
    else:
        return True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query')
def query():
    userid = request.args.get('userid')
    chid = request.args.get('chid')
    con = sqlite3.connect('./message.db')
    cur = con.cursor()
    datas = data = []
    if userid:
        if not checkint(userid):
            return redirect(url_for('home'))
        cur.execute(f"SELECT * FROM Msg WHERE userid == {userid} ORDER BY msgid DESC")
        datas = cur.fetchall()
    elif chid:
        if not checkint(chid):
            return redirect(url_for('home'))
        cur.execute(f"SELECT * FROM Msg WHERE channelid == {chid} ORDER BY msgid DESC")
        datas = cur.fetchall()
    else:
        con.close()
        return redirect(url_for('home'))
    con.close()
    print(datas)
    return render_template('query.html', data=datas)

def run():
  app.run(host='0.0.0.0',port=80)

def keep_alive():
    t = Thread(target=run)
    t.start()