from flask import render_template, flash, redirect, url_for, request

from App import app, db
from .forms import TodoForm, SurveyForm
from .models import Todo, Survey

from datetime import datetime,timedelta, tzinfo

class JST(tzinfo):
    # タイムゾーンの変更用
    def utcoffset(self, dt):
        return timedelta(hours=9)
    def dst(self, dt):
        return timedelta(0)
    def tzname(self, dt):
        return 'JST'

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    form = SurveyForm(request.form)
    boke_list = [
    {"id":0, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/5724746438cffa225ccd1da313b0b816_600.jpg', "text":'ロンパ／肩に貼る／くっつい'},
    {"id":1, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/27039b0a71f740acd6f2fe959247e347_600.jpg', "text":'快適な空の旅をお楽しみ下さい。'},
    {"id":2, "img":'http://d13n9ry8xcpemi.cloudfront.net/photo/odai/400/de26cb822d7a5a9ad8b26746ebf572da_400.jpg', "text":'急いでるんで'},
    {"id":3, "img":'http://d13n9ry8xcpemi.cloudfront.net/photo/odai/400/de5419516de5bd75b3df533036b929ed_400.jpg', "text":'米洗い部'},
    {"id":4, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/ca1bf475bc65c118bee651fd872d379d_600.jpg', "text":'オンお客様感謝'},
    {"id":5, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/a978eeb652f570186bc3f321b096f377_600.jpg', "text":'みんなー修学旅行のグループ分け終わったかー？'},
    {"id":6, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/0c35e058806de5ed98d34846ea1a6b1e_400.jpg', "text":'便所飯'},
    {"id":7, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/3ff522e9bfe7fe20fab0cf4380c0e269_600.jpg', "text":'ノックをする'},
    {"id":8, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/8fdd1e3afbf040758eea24e3429efda0_600.jpg', "text":'任天堂の全盛期を語るマリオとドンキーコング'},
    {"id":9, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/a3c355f4d0ca1a0ebe2aaeb52dc24e80_600.jpg', "text":'神よ！悪しき者達に裁きを'},
    {"id":10, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/d12449d3b8eecae96d01b49a299e04ad_400.jpg', "text":'まろろろろろ'},
    {"id":11, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/8e7f79a9ba4831aebc2816a978cda6e7_600.jpg', "text":'先週のシルエットクイズの答えはこれだ！'},
    {"id":12, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/db559143ef2ac74c6acaa6b7d3ba9c3b_600.jpg', "text":'燃え上が～れ　炊き上が～れ　召し上が～れ　ガンダム～♪'},
    {"id":13, "img":'http://d13n9ry8xcpemi.cloudfront.net/photo/odai/400/3146f4d9bff12a28e6fc7e8f3fc15118_400.jpg', "text":'ゴルフ場にしましょう！'},
    {"id":14, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/5791cd18cc629803724655aebab0579d_400.jpg', "text":'「床ぁぁ‼︎」『それそれぇ‼︎』「床ぁぁ‼︎」『それそれぇ‼︎』「床ぁぁ‼︎」『それそれぇ‼︎』'},
    {"id":15, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/af75ddb1f8fd57efb8c7dafab026388e_600.jpg', "text":'10、9、8、7'},
    {"id":16, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/1890020c6f9981f3a9c53a2ba7048538_400.jpg', "text":'手品師の人に貸した1000円札が返されないまま、次のマジックが始まった'},
    {"id":17, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/8c1a11fb6e62ee06c7d67de823687561_600.jpg', "text":'／ミ"ャ"ーーーー！！！＼'},
    {"id":18, "img":'http://d13n9ry8xcpemi.cloudfront.net/photo/odai/400/5b18ba7c7920808b3d52530490ab63f2_400.jpg', "text":'「これ以上ステーキに水をかけないでいただけますか」'},
    {"id":19, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/88fb8e6fd8a42810ee1dc582adc7695a_600.jpg', "text":'ろすぞリーブ21'},
    {"id":20, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/3cd8b682b427bed6bdde8b6fd40ff726_600.jpg', "text":'Trick or treat'},
    {"id":21, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/400/9e0ab9369d234a8e7c5a3f3c5dca6fc5_400.jpg', "text":'NHKへの最終手段'},
    {"id":22, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/e6cde0f7ab312ccb74bb840538d7f44a_600.jpg', "text":'創造/破壊'},
    {"id":23, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/240/a957b08c1c641d2421b09ad8956b68de_240.jpg', "text":'ここ一塁にするね'},
    {"id":24, "img":'http://d13n9ry8xcpemi.cloudfront.net/photo/odai/400/994ade3113a72a1f31287e307e22f71c_400.jpg', "text":'離れて 飛び散るよ'},
    {"id":25, "img":'http://d13n9ry8xcpemi.cloudfront.net/photo/odai/240/139deac06eefa353ae5f5097c1ccefa0_240.jpg', "text":'めんどくさい先輩に会った'},
    {"id":26, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/03747f0fccd5f688264dcfec451fd836_600.jpg', "text":'いらっしゃいませ／あちらの席へどうぞ！'},
    {"id":27, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/3b4435e86a40b4aa803e9c2a8e52ec37_600.jpg', "text":'申し訳ついでなのですが帰り道にポストがありましたら・・・'},
    {"id":28, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/9e1376d07e9caeb524e9395e4e385255_600.jpg', "text":'一塁ランナーがめっちゃ挑発してくる'},
    {"id":29, "img":'http://d2dcan0armyq93.cloudfront.net/photo/odai/600/5536d4094adcfade44f607b18bb40e52_600.jpg', "text":'綾鷹ギューって／甘えん坊さん／おいで！'}
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
        twitter = form.twitter.data

        timestamp = datetime.now(tz=JST())
        survey = Survey(boke0=boke0, boke1=boke1,boke2=boke2,boke3=boke3,boke4=boke4,boke5=boke5,boke6=boke6,boke7=boke7,boke8=boke8,boke9=boke9,
            boke10=boke10, boke11=boke11,boke12=boke12,boke13=boke13,boke14=boke14,boke15=boke15,boke16=boke16,boke17=boke17,boke18=boke18,boke19=boke19,
            boke20=boke20, boke21=boke21,boke22=boke22,boke23=boke23,boke24=boke24,boke25=boke25,boke26=boke26,boke27=boke27,boke28=boke28,boke29=boke29,
            comp0 = comp0, comp1= comp1, comp2=comp2, comp3=comp3, botti=botti, bokete=bokete, twitter=twitter, timestamp=timestamp)
        db.session.add(survey)
        db.session.commit()
        return redirect(url_for('thanks'))

    survey_list = Survey.query.order_by(Survey.timestamp.desc())
    return render_template('survey.html',
                           form=form,
                           bokes=boke_list,
                           hyoka_list=survey_list)

@app.route('/thanks')
def thanks():
    return render_template("thanks.html")



