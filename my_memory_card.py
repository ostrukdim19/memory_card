from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGroupBox, QWidget, QPushButton, QHBoxLayout, QLabel, QMessageBox, QRadioButton, QVBoxLayout, QButtonGroup
from random import shuffle
from random import randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()

main_win.total = 0
main_win.score = 0

lb_Question = QLabel()
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

RadioGroupBox = QGroupBox('Варианты ответов:')
rbtn_1 = QRadioButton()
rbtn_2 = QRadioButton()
rbtn_3 = QRadioButton()
rbtn_4 = QRadioButton()
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

btn_OK = QPushButton('Ответить')

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line2.addWidget(RadioGroupBox)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.setSpacing(5)
main_win.setLayout(layout_card)

AnsGroupBox = QGroupBox('Результаты теста:')
text1 = QLabel('Правильно/Неправильно')
text2 = QLabel('Правильный ответ')

layout_line2.addWidget(AnsGroupBox)

lineV = QVBoxLayout()
lineV.addWidget(text1, alignment = Qt.AlignCenter)
lineV.addWidget(text2, alignment = Qt.AlignCenter)
AnsGroupBox.setLayout(lineV)

AnsGroupBox.hide()

def rating_def():
    rating = main_win.score / main_win.total * 100
    print(rating)
    

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    if btn_OK.text() == 'Ответить':
        show_result()
    else:
        show_question()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Французкий', 'Испанский'))
questions_list.append(Question('Какое самое популярное домашнее животное?', 'Кошки и собаки', 'Хомяки и рыбки', 'Попугаи и кролики', 'Морские свинки и крысы'))

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    text2.setText(q.right_answer)
    show_question()

def show_correct(result):
    text1.setText(result)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
    else:
        show_correct('Неправильно')
    rating_def()
    

def next_question():
    cur_question = randint(0, len(questions_list) - 1)
    lists = questions_list[cur_question]
    ask(lists)
    main_win.total += 1
    

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

next_question()

btn_OK.clicked.connect(click_OK)

main_win.setWindowTitle('MEMORY CARD')
main_win.show()
app.exec()

