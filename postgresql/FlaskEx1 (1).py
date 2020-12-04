from flask import Flask, request, render_template
import random
import datetime
import psycopg2
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('H:/Machine Learning A-Z (Codes and Datasets)/Part 7 - Natural Language Processing/Section 36 - Natural Language Processing/Python/Template/Flask.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['Name']
    n=random.randint(100,900)
    n1 = random.randint(100, 900)
    processed_text = "Name:"+text.upper()+"\n Age  :"+request.form['Age']+"\n Mobile No  :"+request.form['Mob']+"\n Gender  :"+request.form['Gen']+"\n Registration Id: R"+str(n)+str(n1)+"\n Registration Time: "+str(datetime.datetime.now())
    connection = psycopg2.connect(user="postgres",
                                 password="Santu@1485",
                                 host="127.0.0.1",
                                 port="5432",
                                 database="postgres")
    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO Patient_Reg VALUES (%s,%s,%s,%s,%s,%s)"""
    record_to_insert = ("R"+str(n)+str(n1), text.upper(), request.form['Age'], request.form['Gen'],request.form['Mob'],str(datetime.datetime.now()))
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    return processed_text
if __name__ == "__main__":
    app.run()