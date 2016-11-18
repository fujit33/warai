from flask import render_template, flash, redirect, url_for, request

from App import app, db
from .forms import TodoForm, SurveyForm
from .models import Todo, Survey,Surveynew,Bokete

from datetime import datetime,timedelta, tzinfo
from math import modf

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

@app.route('/result', methods = ["GET", "POST"])
def result():
    if request.method == 'POST':
      bid = request.form["bokes"]
      boke = Bokete.query.get(bid)
      boke.point = int(boke.point+1)
      db.session.commit()
      return render_template("thanks.html")

    return render_template("result.html")

@app.route('/cluster')
def cluster():
    return render_template("cluster.html",
      boke_listA=[boke_list[5],boke_list[7],boke_list[12],boke_list[21],boke_list[25]],
      boke_listB=[boke_list[3],boke_list[9],boke_list[13],boke_list[23],boke_list[28]],
      boke_listC=[boke_list[2],boke_list[6],boke_list[16],boke_list[20],boke_list[27]],
      boke_listD=[boke_list[4],boke_list[10],boke_list[17],boke_list[19],boke_list[26]],
      boke_listE=[boke_list[0],boke_list[8],boke_list[14],boke_list[22],boke_list[29]],
      boke_listF=[boke_list[1],boke_list[11],boke_list[15],boke_list[18],boke_list[24]],
      )

@app.route('/grandprix', methods = ["GET"])
def rank():
  bokelist = db.session.query(Bokete).order_by(Bokete.point)
  bokelist_A = [x.point for x in bokelist if x.cluster=="A"][::-1]
  bokelist_A_boke = [x.bokete for x in bokelist if x.cluster=="A"][::-1]
  bokelist_B = [x.point for x in bokelist if x.cluster=="B"][::-1]
  bokelist_B_boke = [x.bokete for x in bokelist if x.cluster=="B"][::-1]
  bokelist_C = [x.point for x in bokelist if x.cluster=="C"][::-1]
  bokelist_C_boke = [x.bokete for x in bokelist if x.cluster=="C"][::-1]
  bokelist_D = [x.point for x in bokelist if x.cluster=="D"][::-1]
  bokelist_D_boke = [x.bokete for x in bokelist if x.cluster=="D"][::-1]
  bokelist_E = [x.point for x in bokelist if x.cluster=="E"][::-1]
  bokelist_E_boke = [x.bokete for x in bokelist if x.cluster=="E"][::-1]
  bokelist_F = [x.point for x in bokelist if x.cluster=="F"][::-1]
  bokelist_F_boke = [x.bokete for x in bokelist if x.cluster=="F"][::-1]
  bokelist_A = ["ウザウザ言葉遊び"].extend(bokelist_A)
  bokelist_B = ["ヲタヲタ悲哀"].extend(bokelist_B)
  bokelist_C = ["ノリノリ幸せ"].extend(bokelist_C)
  bokelist_D = ["いやいやリアクション"].extend(bokelist_D)
  bokelist_E = ["ないない世界観"].extend(bokelist_E)
  bokelist_F = ["あるあるキャラ"].extend(bokelist_F)
  print()
  return render_template("grandprix.html",
                          pntA=bokelist_A,
                          pntB=bokelist_B,
                          pntC=bokelist_C,
                          pntD=bokelist_D,
                          pntE=bokelist_E,
                          pntF=bokelist_F,
                          bokeA=bokelist_A_boke,
                          bokeB=bokelist_B_boke,
                          bokeC=bokelist_C_boke,
                          bokeD=bokelist_D_boke,
                          bokeE=bokelist_E_boke,
                          bokeF=bokelist_F_boke,
                          )

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    form = SurveyForm(request.form)
    boke_list = [{'cluster': 'E',
  'id': 1,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/3cd8b682b427bed6bdde8b6fd40ff726_600.jpg',
  'text': 'Trick or treat',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluE.png"},
 {'cluster': 'F',
  'id': 2,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135274.jpg',
  'text': 'めんどくさい先輩に会った',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluF.png"},
 {'cluster': 'C',
  'id': 3,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135284.jpg',
  'text': 'まろろろろろ',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluC.png",},
 {'cluster': 'B',
  'id': 4,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135282.jpg',
  'text': 'みんなー修学旅行のグループ分け終わったかー？',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluB.png"},
 {'cluster': 'D',
  'id': 5,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/af75ddb1f8fd57efb8c7dafab026388e_600.jpg',
  'text': '10、9、8、7',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluD.png"},
 {'cluster': 'A',
  'id': 6,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/5724746438cffa225ccd1da313b0b816_600.jpg',
  'text': 'ロンパ／肩に貼る／くっつい',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluA.png"},
 {'cluster': 'C',
  'id': 7,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135271.jpg',
  'text': '先週のシルエットクイズの答えはこれだ！',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluC.png"},
 {'cluster': 'A',
  'id': 8,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/27039b0a71f740acd6f2fe959247e347_600.jpg',
  'text': '快適な空の旅をお楽しみ下さい。',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluA.png"},
 {'cluster': 'E',
  'id': 9,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135273.jpg',
  'text': 'NHKへの最終手段',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluE.png"},
 {'cluster': 'B',
  'id': 10,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/0c35e058806de5ed98d34846ea1a6b1e_400.jpg',
  'text': '便所飯',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluB.png"},
 {'cluster': 'D',
  'id': 11,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135280.jpg',
  'text': '手品師の人に貸した1000円札が返されないまま、次のマジックが始まった',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluD.png"},
 {'cluster': 'F',
  'id': 12,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135277.jpg',
  'text': 'いらっしゃいませ／あちらの席へどうぞ！',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluF.png"},
 {'cluster': 'A',
  'id': 13,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135286.jpg',
  'text': '急いでるんで',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluA.png"},
 {'cluster': 'B',
  'id': 14,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/3ff522e9bfe7fe20fab0cf4380c0e269_600.jpg',
  'text': 'ノックをする',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluB.png"},
 {'cluster': 'E',
  'id': 15,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135287.jpg',
  'text': '創造/破壊',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluE.png"},
 {'cluster': 'F',
  'id': 16,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/3b4435e86a40b4aa803e9c2a8e52ec37_600.jpg',
  'text': '申し訳ついでなのですが帰り道にポストがありましたら・・・',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluF.png"},
 {'cluster': 'C',
  'id': 17,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135285.jpg',
  'text': '燃え上が～れ\u3000炊き上が～れ\u3000召し上が～れ\u3000ガンダム～♪',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluC.png"},
 {'cluster': 'D',
  'id': 18,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135270.jpg',
  'text': '／ミ"ャ"ーーーー！！！＼',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluD.png"},
 {'cluster': 'F',
  'id': 19,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135237.jpg',
  'text': '一塁ランナーがめっちゃ挑発してくる',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluF.png"},
 {'cluster': 'D',
  'id': 20,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135269.jpg',
  'text': '「これ以上ステーキに水をかけないでいただけますか」',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluD.png"},
 {'cluster': 'C',
  'id': 21,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135276.jpg',
  'text': 'ゴルフ場にしましょう！',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluC.png"},
 {'cluster': 'A',
  'id': 22,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/de5419516de5bd75b3df533036b929ed_400.jpg',
  'text': '米洗い部',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluA.png"},
 {'cluster': 'E',
  'id': 23,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135281.jpg',
  'text': 'ここ一塁にするね',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluE.png"},
 {'cluster': 'B',
  'id': 24,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135272.jpg',
  'text': '任天堂の全盛期を語るマリオとドンキーコング',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluB.png"},
 {'cluster': 'F',
  'id': 25,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135278.jpg',
  'text': 'ギューって／甘えん坊さん／おいで！',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluF.png"},
 {'cluster': 'A',
  'id': 26,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135283.jpg',
  'text': 'オンお客様感謝',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluA.png"},
 {'cluster': 'D',
  'id': 27,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135236.jpg',
  'text': 'ろすぞリーブ21',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluD.png"},
 {'cluster': 'C',
  'id': 28,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135279.jpg',
  'text': '「床ぁぁ‼︎」『それそれぇ‼︎』「床ぁぁ‼︎」『それそれぇ‼︎』「床ぁぁ‼︎」『それそれぇ‼︎』',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluC.png"},
 {'cluster': 'B',
  'id': 29,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/a3c355f4d0ca1a0ebe2aaeb52dc24e80_600.jpg',
  'text': '神よ！悪しき者達に裁きを',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluB.png"},
 {'cluster': 'E',
  'id': 30,
  'img': 'http://web.sfc.keio.ac.jp/~t13804kf/orf2016/bokeimg/S__7135275.jpg',
  'text': '離れて 飛び散るよ',
  "cimg":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/cluE.png"}]

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

        bokete = form.bokete.data
        twitter = form.twitter.data
        mail = form.mail.data
        timestamp = datetime.now(tz=JST())

        survey = Surveynew(boke0=boke0, boke1=boke1,boke2=boke2,boke3=boke3,boke4=boke4,boke5=boke5,boke6=boke6,boke7=boke7,boke8=boke8,boke9=boke9,
            boke10=boke10, boke11=boke11,boke12=boke12,boke13=boke13,boke14=boke14,boke15=boke15,boke16=boke16,boke17=boke17,boke18=boke18,boke19=boke19,
            boke20=boke20, boke21=boke21,boke22=boke22,boke23=boke23,boke24=boke24,boke25=boke25,boke26=boke26,boke27=boke27,boke28=boke28,boke29=boke29,
            timestamp=timestamp)
        db.session.add(survey)
        db.session.commit()
        all_mean  =2.4614121510673237
        means = {'4': 2.9745484400656816,
 '8': 2.0377668308702792,
 '0': 2.2110016420361247,
 '19': 2.4376026272577995,
 '27': 1.4541050903119868,
 '11': 2.6559934318555007,
 '22': 2.8390804597701149,
 '2': 2.1129720853858787,
 '3': 2.1945812807881775,
 '1': 2.7947454844006567,
 '26': 2.7036124794745486,
 '25': 2.6756978653530377,
 '24': 2.3563218390804597,
 '20': 2.3042364532019706,
 '13': 2.0435139573070606,
 '5': 2.8103448275862069,
 '18': 2.5919540229885056,
 '23': 2.8275862068965516,
 '9': 2.6313628899835795,
 '6': 2.2298850574712645,
 '14': 2.8530377668308704,
 '7': 2.7183908045977012,
 '12': 2.8924466338259442,
 '10': 2.8103448275862069,
 '16': 2.3768472906403941,
 '15': 2.3990147783251232,
 '28': 1.8039408866995073,
 '21': 2.2725779967159276,
 '29': 2.5533661740558293,
 '17': 1.8954844006568144}
        hyokas = [boke0,boke1,boke2,boke3,boke4,boke5,boke6,boke7,boke8,boke9,
        boke10,boke11,boke12,boke13,boke14,boke15,boke16,boke17,boke18,boke19,
        boke20,boke21,boke22,boke23,boke24,boke25,boke26,boke27,boke28,boke29,]

        # ボケリストに評価を代入
        for b,h in zip(boke_list,hyokas):
          b["score"] = h
        bokelist_top5 = sorted(boke_list, key=lambda x:x['score'], reverse=True)[:5]
        # boke_listに短縮テキストを代入
        for b in boke_list:
          b["short_text"] = b["text"][:4] + "…"

        A_mean = sum([boke5*all_mean/means["5"],boke7*all_mean/means["7"],boke12*all_mean/means["12"],boke21*all_mean/means["21"],boke25*all_mean/means["25"]])/5
        B_mean = sum([boke3*all_mean/means["3"],boke9*all_mean/means["9"],boke13*all_mean/means["13"],boke23*all_mean/means["23"],boke28*all_mean/means["28"]])/5
        C_mean = sum([boke2*all_mean/means["2"],boke6*all_mean/means["6"],boke16*all_mean/means["16"],boke20*all_mean/means["20"],boke27*all_mean/means["27"]])/5
        D_mean = sum([boke4*all_mean/means["4"],boke10*all_mean/means["10"],boke17*all_mean/means["17"],boke19*all_mean/means["19"],boke26*all_mean/means["26"]])/5
        E_mean = sum([boke0*all_mean/means["0"],boke8*all_mean/means["8"],boke14*all_mean/means["14"],boke22*all_mean/means["22"],boke29*all_mean/means["29"]])/5
        F_mean = sum([boke1*all_mean/means["1"],boke11*all_mean/means["11"],boke15*all_mean/means["15"],boke18*all_mean/means["18"],boke24*all_mean/means["24"]])/5
        means = [round(A_mean,1),round(B_mean,1), round(C_mean,1),round(D_mean,1),round(E_mean,1),round(F_mean,1)]
        means2 = {"A":round(A_mean,1),"B":round(B_mean,1),"C": round(C_mean,1),"D":round(D_mean,1),"E":round(E_mean,1),"F":round(F_mean,1)}
        wariais = {"A":str(means2["A"]) + "P","B":str(means2["B"])+ "P","C":str(means2["C"])+ "P", "D":str(means2["D"])+ "P","E":str(means2["E"])+ "P","F":str(means2["F"])+ "P"}
        topcluster = ["A","B","C","D","E","F"][means.index(max(means))]

        if bokete!="":
          bokete_add = Bokete(bokete=bokete,twitter=twitter,mail=mail,count=0,point=0,timestamp=timestamp, cluster=topcluster)
          db.session.add(bokete_add)
          db.session.commit()

        top = ["ウザウザ言葉遊び","ヲタヲタ悲哀","ノリノリ幸せ","イヤイヤリアクション","ないない世界観","あるある井戸端会議長"][means.index(max(means))]
        names = {"A":"ウザウザ言葉遊び","B":"ヲタヲタ悲哀","C":"ノリノリ幸せ","D":"イヤイヤリアクション","E":"ないない世界観","F":"あるある井戸端会議長"}
        detail = ["あなたは、お題に“上手く”ハマったボケに、ついついにやけてしまうのではないでしょうか？上手く、駄洒落が思いついた時などは、相手にどう思おわれようと、言ってしまうキザな一面があるお人かも？「サンドウィッチマン」等もお好きでは？",
                    "あなたは、ボケから感じ取れる“悲哀”に、ついつい笑ってしまうのではないでしょうか？人の弱みや哀愁に敏感、また自身の過去等を笑い飛ばせるようなお人かも？「２ちゃんねる」等もお好きでは？",
                    "あなたは、“勢いのある”“突拍子もない”ボケに、ついつい笑ってしまうのではないでしょうか？他者が楽しそうな様子を幸せそうに見守る優しいお人かも？「サンシャイン池崎」等もお好きでは？",
                    "あなたは、人が怒っている、恥じている等の“リアクション”に、ついつい笑ってしまうのではないでしょうか？他者のリアクションを楽しむSの心が隠れているかも「千鳥」等もお好きでは？",
                    "あなたは、一見真剣そうな表情から起きる“常識はずれ”な言動に、ついつい笑ってしまうのではないでしょうか？常識はずれな言動に敏感なあなたは、常識的な人かも？？不気味な非常識さを持つ「野生爆弾川島」等もお好きでは？",
                    "あなたは、日常でよく見かける・体験する“あるある”に、ついつい笑ってしまうのではないでしょうか？ちょっと誇張されたウザい“あるある”を日常生活に当てはめられるあたり、人間観察能力が高いお人かも？「ロバート」等もお好きでは？"
                    ][means.index(max(means))]
        # result
        zab = "http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/zabuton.png"
        zab0 = ["","http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/zabuton01.png","http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/zabuton02.png","http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/zabuton03.png","http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/zabuton04.png",
        "http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/zabuton05.png","http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/zabuton06.png","http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/zabuton07.png",
        "http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/zabuton08.png","http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/zabuton09.png"]
        hitos = {"A":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/hitoA.png","B":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/hitoB.png","C":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/hitoC.png",
        "D":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/hitoD.png","E":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/hitoE.png","F":"http://web.sfc.keio.ac.jp/~t13804kf/orf2016/img/hitoF.png"}
        tableA_img = {"r1":"","r2":"","r3":"","r4":"","r5":"","r6":"","r7":"","r8":""}
        tableA_txt = {"r1":"","r2":"","r3":"40%","r4":"ウザウザ言葉遊びタイプ","r5":"","r6":"","r7":"","r8":""}
        clusters = ["A","B","C","D","E","F"]
        tablis = {"A":"tabliA","B":"tabliB","C":"tabliC","D":"tabliD","E":"tabliE","F":"tabliF"}
        tabs = {"A":"tabA","B":"tabB","C":"tabC","D":"tabD","E":"tabE","F":"tabF"}
        tables = []
        for c in clusters:
          decimal, integer = modf(means2[c])

          if means2[c]<1:
            tables.append({"r1":"","r2":"","r3":"","r4":"","r5":"","r6":"","r7":hitos[c],"r8": zab0[int(decimal * 10)],
              "t1":"","t2":"","t3":"","t4":"","t5":wariais[c],"t6":names[c],"t7":"","t8":"", "tabli":tablis[c], "tabs":tabs[c]})
          elif means2[c]<2:
            tables.append({"r1":"","r2":"","r3":"","r4":"","r5":"","r6":hitos[c],"r7":zab0[int(decimal * 10)],"r8":zab ,
              "t1":"","t2":"","t3":"","t4":wariais[c],"t5":names[c],"t6":"","t7":"","t8":"", "tabli":tablis[c], "tabs":tabs[c]})
          elif means2[c]<3:
            tables.append({"r1":"","r2":"","r3":"","r4":"","r5":hitos[c],"r6":zab0[int(decimal * 10)],"r7":zab,"r8": zab,
              "t1":"","t2":"","t3":wariais[c],"t4":names[c],"t5":"","t6":"","t7":"","t8":"", "tabli":tablis[c], "tabs":tabs[c]})
          elif means2[c]<4:
            tables.append({"r1":"","r2":"","r3":"","r4":hitos[c],"r5":zab0[int(decimal * 10)],"r6":zab,"r7":zab,"r8": zab,
              "t1":"","t2":wariais[c],"t3":names[c],"t4":"","t5":"","t6":"","t7":"","t8":"", "tabli":tablis[c], "tabs":tabs[c]})
          elif means2[c]<5:
            tables.append({"r1":"","r2":"","r3":hitos[c],"r4":zab0[int(decimal * 10)],"r5":zab,"r6":zab,"r7":zab,"r8": zab,
              "t1":wariais[c],"t2":names[c],"t3":"","t4":"","t5":"","t6":"","t7":"","t8":"", "tabli":tablis[c], "tabs":tabs[c]})
          else:
            tables.append({"r1":"","r2":hitos[c],"r3":zab0[int(decimal * 10)],"r4":zab,"r5":zab,"r6":zab,"r7":zab,"r8": zab,
              "t1":names[c],"t2":"","t3":"","t4":"","t5":"","t6":"","t7":"","t8":"", "tabli":tablis[c], "tabs":tabs[c]})
        #======================
        # grand prix
        bokelist = db.session.query(Bokete).order_by(Bokete.count)
        utc = datetime.utcnow()
        diff = [utc - b.timestamp for b in bokelist]
        print((bokelist[0].count>4) & (bokelist[0].point==0))
        bokes = [{"bokete": b.bokete, "id": b.id, "count":b.count} for b,d in zip(bokelist,diff) if (d.seconds >900) & (b.cluster == topcluster) & ((b.count<=4) | (b.point>0))]
        bokes6 = bokes[:6]
        for b in bokes6:
          boke = Bokete.query.get(b["id"])
          boke.count = int(b["count"]+1)
          db.session.commit()

        bokes0 = [x for x in boke_list if x["score"]==0]
        bokes1 = [x for x in boke_list if x["score"]==1]
        bokes2 = [x for x in boke_list if x["score"]==2]
        bokes3 = [x for x in boke_list if x["score"]==3]
        bokes4 = [x for x in boke_list if x["score"]==4]
        bokes5 = [x for x in boke_list if x["score"]==5]

        return render_template('result.html',
                                hyokas = hyokas,
                                scores = means,
                                top = top,
                                tables=tables,
                                topcluster = topcluster,
                                bokelist_top5 = bokelist_top5,
                                bokes0 = bokes0,
                                bokes1 = bokes1,
                                bokes2 = bokes2,
                                bokes3 = bokes3,
                                bokes4 = bokes4,
                                bokes5 = bokes5,
                                boke_listA=[boke_list[5],boke_list[7],boke_list[12],boke_list[21],boke_list[25]],
                                boke_listB=[boke_list[3],boke_list[9],boke_list[13],boke_list[23],boke_list[28]],
                                boke_listC=[boke_list[2],boke_list[6],boke_list[16],boke_list[20],boke_list[27]],
                                boke_listD=[boke_list[4],boke_list[10],boke_list[17],boke_list[19],boke_list[26]],
                                boke_listE=[boke_list[0],boke_list[8],boke_list[14],boke_list[22],boke_list[29]],
                                boke_listF=[boke_list[1],boke_list[11],boke_list[15],boke_list[18],boke_list[24]],
                                bokes6 = bokes6,
                                )

    survey_list = Survey.query.order_by(Survey.timestamp.desc())
    return render_template('survey.html',
                           form=form,
                           bokes=boke_list,
                           hyoka_list=survey_list)





