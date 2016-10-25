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

@app.route('/thanks')
def thanks():
    return render_template("thanks.html")

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    form = SurveyForm(request.form)
    boke_list = [{'cluster': 'E',
  'id': 1,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/3cd8b682b427bed6bdde8b6fd40ff726_600.jpg',
  'text': 'Trick or treat'},
 {'cluster': 'F',
  'id': 2,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135274.jpg',
  'text': 'めんどくさい先輩に会った'},
 {'cluster': 'C',
  'id': 3,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135284.jpg',
  'text': 'まろろろろろ'},
 {'cluster': 'B',
  'id': 4,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135282.jpg',
  'text': 'みんなー修学旅行のグループ分け終わったかー？'},
 {'cluster': 'D',
  'id': 5,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/af75ddb1f8fd57efb8c7dafab026388e_600.jpg',
  'text': '10、9、8、7'},
 {'cluster': 'A',
  'id': 6,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/5724746438cffa225ccd1da313b0b816_600.jpg',
  'text': 'ロンパ／肩に貼る／くっつい'},
 {'cluster': 'C',
  'id': 7,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135271.jpg',
  'text': '先週のシルエットクイズの答えはこれだ！'},
 {'cluster': 'A',
  'id': 8,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/27039b0a71f740acd6f2fe959247e347_600.jpg',
  'text': '快適な空の旅をお楽しみ下さい。'},
 {'cluster': 'E',
  'id': 9,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135273.jpg',
  'text': 'NHKへの最終手段'},
 {'cluster': 'B',
  'id': 10,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/0c35e058806de5ed98d34846ea1a6b1e_400.jpg',
  'text': '便所飯'},
 {'cluster': 'D',
  'id': 11,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135280.jpg',
  'text': '手品師の人に貸した1000円札が返されないまま、次のマジックが始まった'},
 {'cluster': 'F',
  'id': 12,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135277.jpg',
  'text': 'いらっしゃいませ／あちらの席へどうぞ！'},
 {'cluster': 'A',
  'id': 13,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135286.jpg',
  'text': '急いでるんで'},
 {'cluster': 'B',
  'id': 14,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/3ff522e9bfe7fe20fab0cf4380c0e269_600.jpg',
  'text': 'ノックをする'},
 {'cluster': 'E',
  'id': 15,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135287.jpg',
  'text': '創造/破壊'},
 {'cluster': 'F',
  'id': 16,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/3b4435e86a40b4aa803e9c2a8e52ec37_600.jpg',
  'text': '申し訳ついでなのですが帰り道にポストがありましたら・・・'},
 {'cluster': 'C',
  'id': 17,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135285.jpg',
  'text': '燃え上が～れ\u3000炊き上が～れ\u3000召し上が～れ\u3000ガンダム～♪'},
 {'cluster': 'D',
  'id': 18,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135270.jpg',
  'text': '／ミ"ャ"ーーーー！！！＼'},
 {'cluster': 'F',
  'id': 19,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135237.jpg',
  'text': '一塁ランナーがめっちゃ挑発してくる'},
 {'cluster': 'D',
  'id': 20,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135269.jpg',
  'text': '「これ以上ステーキに水をかけないでいただけますか」'},
 {'cluster': 'C',
  'id': 21,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135276.jpg',
  'text': 'ゴルフ場にしましょう！'},
 {'cluster': 'A',
  'id': 22,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/de5419516de5bd75b3df533036b929ed_400.jpg',
  'text': '米洗い部'},
 {'cluster': 'E',
  'id': 23,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135281.jpg',
  'text': 'ここ一塁にするね'},
 {'cluster': 'B',
  'id': 24,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135272.jpg',
  'text': '任天堂の全盛期を語るマリオとドンキーコング'},
 {'cluster': 'F',
  'id': 25,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135278.jpg',
  'text': 'ギューって／甘えん坊さん／おいで！'},
 {'cluster': 'A',
  'id': 26,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135283.jpg',
  'text': 'オンお客様感謝'},
 {'cluster': 'D',
  'id': 27,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135236.jpg',
  'text': 'ろすぞリーブ21'},
 {'cluster': 'C',
  'id': 28,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135279.jpg',
  'text': '「床ぁぁ‼︎」『それそれぇ‼︎』「床ぁぁ‼︎」『それそれぇ‼︎』「床ぁぁ‼︎」『それそれぇ‼︎』'},
 {'cluster': 'B',
  'id': 29,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/a3c355f4d0ca1a0ebe2aaeb52dc24e80_600.jpg',
  'text': '神よ！悪しき者達に裁きを'},
 {'cluster': 'E',
  'id': 30,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135275.jpg',
  'text': '離れて 飛び散るよ'}]

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

        hito0 = form.hito0.data
        hito1 = form.hito1.data
        hito2 = form.hito2.data
        hito3 = form.hito3.data
        hito4 = form.hito4.data
        hito5 = form.hito5.data
        hito6 = form.hito6.data


        comp0 = "".join(form.comp0.data)
        comp1 = "".join(form.comp1.data)
        comp2 = "".join(form.comp2.data)
        media = "".join(form.media.data)

        botti = int(form.botti.data)

        bokete = form.bokete0.data + "/"+form.bokete1.data
        twitter = form.twitter.data

        timestamp = datetime.now(tz=JST())
        survey = Survey(boke0=boke0, boke1=boke1,boke2=boke2,boke3=boke3,boke4=boke4,boke5=boke5,boke6=boke6,boke7=boke7,boke8=boke8,boke9=boke9,
            boke10=boke10, boke11=boke11,boke12=boke12,boke13=boke13,boke14=boke14,boke15=boke15,boke16=boke16,boke17=boke17,boke18=boke18,boke19=boke19,
            boke20=boke20, boke21=boke21,boke22=boke22,boke23=boke23,boke24=boke24,boke25=boke25,boke26=boke26,boke27=boke27,boke28=boke28,boke29=boke29,
            comp0 = comp0, comp1= comp1, comp2=comp2, media=media, botti=botti, hito0=hito0, hito1=hito1, hito2=hito2, hito3=hito3, hito4=hito4,
            hito5=hito5, hito6=hito6, bokete=bokete, twitter=twitter, timestamp=timestamp)
        db.session.add(survey)
        db.session.commit()
        return redirect(url_for('thanks'))

    survey_list = Survey.query.order_by(Survey.timestamp.desc())
    return render_template('survey.html',
                           form=form,
                           bokes=boke_list,
                           hyoka_list=survey_list)





