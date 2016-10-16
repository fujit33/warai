import datetime
from flask import render_template, flash, redirect, url_for, request

from App import app, db
from .forms import TodoForm, SurveyForm
from .models import Todo, Survey

import logging

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = TodoForm()
    if request.method == 'POST' and form.validate():
        title = form.title.data
        detail = form.detail.data
        timestamp = datetime.datetime.utcnow()
        todo = Todo(title=title, detail=detail, timestamp=timestamp)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('survey'))

    todo_list = Todo.query.order_by(Todo.timestamp.desc())
    return render_template('register.html',
                           form=form,
                           todo_list=todo_list)

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    form = SurveyForm()
    boke_list = [
    {"id":0, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/44285705a73651179df91885985d12f3_600.jpg', "text":'コンプレックスですか？ありませんよ。', "model":"c0"},
    {"id":1, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/8460f2e5f80260be8995a058d10acf39_400.jpg', "text":'綾鷹', "model":"c1"},
    {"id":2, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/44285705a73651179df91885985d12f3_600.jpg', "text":'コンプレックスですか？ありませんよ。', "model":"c2"},
    {"id":3, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/8460f2e5f80260be8995a058d10acf39_400.jpg', "text":'綾鷹', "model":"c3"},
    {"id":4, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/44285705a73651179df91885985d12f3_600.jpg', "text":'コンプレックスですか？ありませんよ。', "model":"c4"},
    {"id":5, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/8460f2e5f80260be8995a058d10acf39_400.jpg', "text":'綾鷹', "model":"c5"},
    {"id":6, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/44285705a73651179df91885985d12f3_600.jpg', "text":'コンプレックスですか？ありませんよ。', "model":"c6"},
    {"id":7, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/8460f2e5f80260be8995a058d10acf39_400.jpg', "text":'綾鷹', "model":"c7"},
    {"id":8, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/44285705a73651179df91885985d12f3_600.jpg', "text":'コンプレックスですか？ありませんよ。', "model":"c8"},
    {"id":9, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/8460f2e5f80260be8995a058d10acf39_400.jpg', "text":'綾鷹', "model":"c9"},
    {"id":10, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/44285705a73651179df91885985d12f3_600.jpg', "text":'コンプレックスですか？ありませんよ。', "model":"c10"},
    {"id":11, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/8460f2e5f80260be8995a058d10acf39_400.jpg', "text":'綾鷹', "model":"c11"},
    {"id":12, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/44285705a73651179df91885985d12f3_600.jpg', "text":'コンプレックスですか？ありませんよ。', "model":"c12"},
    {"id":13, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/8460f2e5f80260be8995a058d10acf39_400.jpg', "text":'綾鷹', "model":"c13"},
    {"id":14, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/44285705a73651179df91885985d12f3_600.jpg', "text":'コンプレックスですか？ありませんよ。', "model":"c14"},
    {"id":15, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/8460f2e5f80260be8995a058d10acf39_400.jpg', "text":'綾鷹', "model":"c15"},
    {"id":16, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/44285705a73651179df91885985d12f3_600.jpg', "text":'コンプレックスですか？ありませんよ。', "model":"c16"},
    {"id":17, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/8460f2e5f80260be8995a058d10acf39_400.jpg', "text":'綾鷹', "model":"c17"},
    {"id":18, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/44285705a73651179df91885985d12f3_600.jpg', "text":'コンプレックスですか？ありませんよ。', "model":"c18"},
    {"id":19, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/8460f2e5f80260be8995a058d10acf39_400.jpg', "text":'綾鷹', "model":"c19"},
    {"id":20, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/44285705a73651179df91885985d12f3_600.jpg', "text":'コンプレックスですか？ありませんよ。', "model":"c20"},
    {"id":21, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/8460f2e5f80260be8995a058d10acf39_400.jpg', "text":'綾鷹', "model":"c21"},
    {"id":22, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/44285705a73651179df91885985d12f3_600.jpg', "text":'コンプレックスですか？ありませんよ。', "model":"c22"},
    {"id":23, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/8460f2e5f80260be8995a058d10acf39_400.jpg', "text":'綾鷹', "model":"c23"},
    {"id":24, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/44285705a73651179df91885985d12f3_600.jpg', "text":'コンプレックスですか？ありませんよ。', "model":"c24"},
    {"id":25, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/8460f2e5f80260be8995a058d10acf39_400.jpg', "text":'綾鷹', "model":"c25"},
    {"id":26, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/44285705a73651179df91885985d12f3_600.jpg', "text":'コンプレックスですか？ありませんよ。', "model":"c26"},
    {"id":27, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/8460f2e5f80260be8995a058d10acf39_400.jpg', "text":'綾鷹', "model":"c27"},
    {"id":28, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/44285705a73651179df91885985d12f3_600.jpg', "text":'コンプレックスですか？ありませんよ。', "model":"c28"},
    {"id":29, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/8460f2e5f80260be8995a058d10acf39_400.jpg', "text":'綾鷹', "model":"c29"}
    ]
    if request.method == 'POST' and form.validate():
        boke0 = int(form.choice0.data)
        boke1 = int(form.choice1.data)
        boke2 = int(form.choice2.data)
        boke3 = int(form.choice3.data)
        boke4 = int(form.choice4.data)
        boke5 = int(form.choice5.data)
        boke6 = int(form.choice6.data)
        boke7 = int(form.choice7.data)
        boke8 = int(form.choice8.data)
        boke9 = int(form.choice9.data)
        boke10 = int(form.choice10.data)
        boke11 = int(form.choice11.data)
        boke12 = int(form.choice12.data)
        boke13 = int(form.choice13.data)
        boke14 = int(form.choice14.data)
        boke15 = int(form.choice15.data)
        boke16 = int(form.choice16.data)
        boke17 = int(form.choice17.data)
        boke18 = int(form.choice18.data)
        boke19 = int(form.choice19.data)
        boke20 = int(form.choice20.data)
        boke21 = int(form.choice21.data)
        boke22 = int(form.choice22.data)
        boke23 = int(form.choice23.data)
        boke24 = int(form.choice24.data)
        boke25 = int(form.choice25.data)
        boke26 = int(form.choice26.data)
        boke27 = int(form.choice27.data)
        boke28 = int(form.choice28.data)
        boke29 = int(form.choice29.data)

        comp0 = "".join(form.comp0.data)
        comp1 = "".join(form.comp1.data)
        comp2 = "".join(form.comp2.data)
        comp3 = "".join(form.comp3.data)

        botti = int(form.botti.data)

        bokete = form.bokete.data

        timestamp = datetime.datetime.utcnow()
        survey = Survey(boke0=boke0, boke1=boke1,boke2=boke2,boke3=boke3,boke4=boke4,boke5=boke5,boke6=boke6,boke7=boke7,boke8=boke8,boke9=boke9,
            boke10=boke10, boke11=boke11,boke12=boke12,boke13=boke13,boke14=boke14,boke15=boke15,boke16=boke16,boke17=boke17,boke18=boke18,boke19=boke19,
            boke20=boke20, boke21=boke21,boke22=boke22,boke23=boke23,boke24=boke24,boke25=boke25,boke26=boke26,boke27=boke27,boke28=boke28,boke29=boke29,
            comp0 = comp0, comp1= comp1, comp2=comp2, comp3=comp3, botti=botti, bokete=bokete, timestamp=timestamp)
        db.session.add(survey)
        db.session.commit()
        return redirect(url_for('survey'))

    survey_list = Survey.query.order_by(Survey.timestamp.desc())
    return render_template('survey.html',
                           form=form,
                           bokes=boke_list,
                           hyoka_list=survey_list)





