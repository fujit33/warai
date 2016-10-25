from flask_wtf import Form
from wtforms import StringField, TextAreaField,RadioField, widgets, SelectMultipleField, SelectField
from wtforms.validators import DataRequired, Length

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class TodoForm(Form):
    title = StringField('title', validators=[DataRequired()], default='default')
    detail = TextAreaField('detail', validators=[Length(min=0, max=5000)])

class SurveyForm(Form):
    todofukens = []
    choice0 = RadioField('Choice0',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice1 = RadioField('Choice1',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice2 = RadioField('Choice2',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice3 = RadioField('Choice3',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice4 = RadioField('Choice4',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice5 = RadioField('Choice5',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice6 = RadioField('Choice6',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice7 = RadioField('Choice7',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice8 = RadioField('Choice8',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice9 = RadioField('Choice9',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice10 = RadioField('Choice10',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice11 = RadioField('Choice11',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice12 = RadioField('Choice12',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice13 = RadioField('Choice13',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice14 = RadioField('Choice14',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice15 = RadioField('Choice15',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice16 = RadioField('Choice16',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice17 = RadioField('Choice17',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice18 = RadioField('Choice18',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice19 = RadioField('Choice19',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice20 = RadioField('Choice20',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice21 = RadioField('Choice21',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice22 = RadioField('Choice22',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice23 = RadioField('Choice23',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice24 = RadioField('Choice24',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice25 = RadioField('Choice25',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice26 = RadioField('Choice26',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice27 = RadioField('Choice27',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice28 = RadioField('Choice28',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice29 = RadioField('Choice29',validators=[DataRequired()], choices=[("0", '解釈できない'), ("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    hito0 = RadioField('hito0',validators=[DataRequired()], choices=[("男性", '男性'), ("女性", "女性")])
    hito1 = RadioField('hito1',validators=[DataRequired()], choices=[("17未満", '17未満'), ("17-19", "17-19"), ("20-24", "20-24"), ("25-29", "25-29"), ("30-39", "30-39"), ("40-49", "40-49"),("50以上","50以上")])
    hito2 = SelectField('hito2',validators=[DataRequired()], choices=[("北海道", '北海道'), ("青森", "青森"), ("岩手", "岩手"), ("宮城", "宮城"), ("秋田", "秋田"), ("山形", "山形"), ("福島", "福島"), ("茨城", "茨城"), ("栃木", "栃木"), ("群馬", "群馬"), ("埼玉", "埼玉"), ("千葉", "千葉"), ("東京", "東京"), ("神奈川", "神奈川"), ("新潟", "新潟"), ("富山", "富山"), ("石川", "石川"), ("福井", "福井"), ("山梨", "山梨"), ("長野", "長野"), ("岐阜", "岐阜"), ("静岡", "静岡"), ("愛知", "愛知"), ("三重", "三重"), ("滋賀", "滋賀"), ("京都", "京都"), ("大阪", "大阪"),
                                          ("兵庫", "兵庫"), ("奈良", "奈良"), ("和歌山", "和歌山"), ("鳥取", "鳥取"), ("島根", "島根"), ("岡山", "岡山"), ("広島", "広島"), ("山口", "山口"), ("徳島", "徳島"), ("香川", "香川"), ("愛媛", "愛媛"), ("高知", "高知"), ("福岡", "福岡"), ("佐賀", "佐賀"), ("長崎", "長崎"), ("熊本", "熊本"), ("大分", "大分"), ("宮崎", "宮崎"), ("鹿児島", "鹿児島"), ("沖縄", "沖縄")])
    hito3 = MultiCheckboxField('hito3',validators=[DataRequired()], choices=[("ひとりっこ", 'ひとりっこ'), ("兄", "兄"), ("姉", "姉"), ("弟", "弟"), ("妹", "妹")])
    hito4 = RadioField('hito4',validators=[DataRequired()], choices=[("運動部（屋外）", '運動部（屋外）'), ("運動部（屋内）", "運動部（屋内）"), ("文化部（音楽）", "文化部（音楽）"), ("文化部（美術）", "文化部（美術）"), ("文化部（その他）", "文化部（その他）"), ("帰宅部", "帰宅部")])
    hito5 = RadioField('hito5',validators=[DataRequired()], choices=[("草食系", "草食系（消極的）"),("どちらかと言えば草食系","どちらかと言えば草食系"), ("どちらかと言えば肉食系","どちらかと言えば肉食系"),("肉食系","肉食系（積極的）")])
    hito6 = RadioField('hito6',validators=[DataRequired()], choices=[("Ｍ", "Ｍ"),("どちらかと言えばＭ","どちらかと言えばＭ"), ("どちらかと言えばＳ","どちらかと言えばＳ"),("Ｓ","Ｓ")])
    comp0 = MultiCheckboxField('comp0', choices=[("容姿", '容姿'), ("性格", "性格"),("家族","家族"), ("友人関係","友人関係"),("恋愛","恋愛"),("周囲の評価","周囲の評価"),("過去の体験","過去の体験")])
    comp1 = MultiCheckboxField('comp1', choices=[("容姿", '容姿'), ("性格", "性格"),("家族","家族"), ("友人関係","友人関係"),("恋愛","恋愛"),("周囲の評価","周囲の評価"),("過去の体験","過去の体験")])
    comp2 = MultiCheckboxField('comp2', choices=[("容姿", '容姿'), ("性格", "性格"),("家族","家族"), ("友人関係","友人関係"),("恋愛","恋愛"),("周囲の評価","周囲の評価"),("過去の体験","過去の体験")])
    comp3 = RadioField('comp3',validators=[DataRequired()], choices=[("活かす", '活かす'), ("個性として受け入れる", "個性として受け入れる"),("時間が解決するのを待つ","時間が解決するのを待つ"), ("他の部分でカバーする","他の部分でカバーする")])

    botti = RadioField('botti',validators=[DataRequired()], choices=[("1", "1.ぼっち"),("2","2"), ("3","3"), ("4","4.クラスの人気者")])

    bokete0 = StringField('bokete0', validators=[Length(min=0, max=500)])
    bokete1 = StringField('bokete1', validators=[Length(min=0, max=500)])
    twitter = StringField('twitter', validators=[Length(min=0, max=500)])


