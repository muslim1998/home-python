from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'muslim_secret_key'

class LoginForm(FlaskForm):
	username = StringField('Логин', validators=[DataRequired()])
	password = PasswordField('Пароль', validators=[DataRequired()])
	remember_me = BooleanField('Запомнить меня')
	submit = SubmitField('Войти')

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect('/')
	return render_template('login.html', title='Авторизация', form=form)


class LoginMars(FlaskForm):
	username = StringField('id Астранавта', validators=[DataRequired()])
	password = PasswordField('Пароль Астранавта', validators=[DataRequired()])
	login = StringField('id Капитан', validators=[DataRequired()])
	parol = PasswordField('Пароль Капитана', validators=[DataRequired()])
	remember_me = BooleanField('Запомнить меня')
	submit = SubmitField('Доступ')


@app.route('/mars_login', methods=['GET','POST'])
def mars_login():
	form = LoginMars()
	if form.validate_on_submit():
		return redirect('/answer')
	return render_template('prof_2.html',title='Аварийный доступ',form=form)


@app.route('/distribution')
def distribution():
	return render_template('dist.html',title=distribution)


@app.route('/')
def main_page():
	title = 'Первый шаблон'
	name = 'Алексей'
	return render_template('index.html', title=title, name='Вася')


@app.route('/odd_even')
def odd_even():
	number = 4
	return render_template('odd_even.html', title='Четное Нечетное', number=number)


@app.route('/list_names')
def lisT_names():
	names = ['Alice', 'Vlad', 'Yuki']
	return render_template('list_names.html', title='Список имён', list_of_names=names)


@app.route('/no_params')
def no_params():
	return render_template('params.html', title='Параметры')


@app.route('/templates_try')
def templates_try():
	return render_template('template1.html', title='Шаблон 1', date='21.03.2022')


@app.route('/qwerty')
def qwerty():
	param = {}
	param['username'] = 'Привет пользователь!'
	param['title'] = 'Домашняя страница'
	return render_template('new_file.html', **param)


@app.route('/polaris')
def polaris():
	return render_template('index_one.html', title='Заготовка' )


@app.route('/training/<prof>')
def training(prof):
	if 'инженер' in prof or 'строитель' in prof:
		return render_template('train.html', title='training')
	else:
		return render_template('prof.html',title='training')


@app.route('/list_prof/<pppp>')
def list_prof(pppp):
	if pppp == 'ul':
		return render_template('prof_1.html',title='Профессий')
	elif pppp == 'ol':
		return render_template('prof_2.html',title='Профессий')


@app.route('/answer')
def answer():
	ans = {}
	ans['title'] = 'Анкета'
	ans['surname'] = 'Watny'
	ans['name'] = 'Mark'
	ans['education'] = 'выше среднего'
	ans['profession'] = 'штурман марсхода'
	ans['sex'] = 'male'
	ans['motivation'] = 'Всегда мечтал застрять на Марсе!'
	ans['ready'] = 'True'
	return render_template('answer.html', **ans)


@app.route('/table/<sex>/<int:age>')
def table(sex,age):
	return render_template('name.html', sex=sex, age=age)

@app.route('/galery')
def galery():
	return render_template("gal.html",title=galery)

if __name__ == '__main__':
	app.run(port=8080, host='127.0.0.1',debug=True)