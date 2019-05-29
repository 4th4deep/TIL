from flask import Flask, render_template  # pip install requests
import lotto_package

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pick_lotto')
def pick_lotto():
    lucky_numbers = random.sample(range(1, 46), 6)
    lucky_numbers.sort()
    return render_template('pick_lotto.html', numbers=lucky_numbers)


@app.route('/get_lotto/<int:num>')
def get_lotto(num):
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    res = requests.get(url).text  # type == String
    data = json.loads(res)  # type == dict

    real_numbers = []

    if data['returnValue'] == 'success':
        for key, value in data.items():
            if 'drwtNo' in key:
                real_numbers.append(value)

        real_numbers.sort()

    return render_template(
        'get_lotto.html',
        numbers=real_numbers,
        draw_no=num
    )


@app.route('/lotto/<int:num>')
def lotto(num):
    lucky_numbers = get_random_numbers()

    real_data = get_lotto_numbers(num)  # { 'real': [1,2,3,4,5,6], 'bonus': 7 }

    real_numbers = real_data['real']
    bonus_number = real_data['bonus']

    # 등수 비교


    return render_template(
        'lotto.html',
        result=result,
        real_numbers=real_numbers,
        lucky_numbers=lucky_numbers,
        bonus=bonus_number,
        winning=data['firstAccumamnt']
    )

@app.route('/square/<int:num>')
def square(num):
    result = num ** 2
    return f'{result}'


if __name__ == '__main__':
    app.run(debug=True)
