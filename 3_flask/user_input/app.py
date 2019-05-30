from flask import Flask, render_template, request
from iexfinance.stocks import Stock

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search_stock')
def stock():
    return render_template(
        'search_stock.html',
        is_first_search=True,
    )


@app.route('/search_result')
def result():
    TOKEN = 'pk_34947d6f20564c52a9dcd62bf4d4ab5f'
    user_input = request.args.get('keyword')

    try:
        stock = Stock(user_input, token=TOKEN)
        data = stock.get_quote()
    except:
        return render_template(
            'search_stock.html',
            is_success=False,
        )

    return render_template(
        'search_stock.html',
        is_success=True,
        c_name=data['companyName'],
        l_price=data['latestPrice'],
    )


if __name__ == '__main__':
    app.run(debug=True)
