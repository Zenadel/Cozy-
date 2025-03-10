from flask import Flask, render_template_string

app = Flask(__name__)

# Данные о товарах
products = [
    {"id": 1, "name": "Плед мягкий", "price": 450, "image": "https://via.placeholder.com/150", "link": "#"},
    {"id": 2, "name": "Свеча ароматическая", "price": 120, "image": "https://via.placeholder.com/150", "link": "#"},
    {"id": 3, "name": "Кружка керамическая", "price": 200, "image": "https://via.placeholder.com/150", "link": "#"},
    {"id": 4, "name": "Декоративная подушка", "price": 300, "image": "https://via.placeholder.com/150", "link": "#"},
]

# HTML-шаблон
html_template = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cozy Market</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            color: #333;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #6d6875;
            color: white;
            padding: 20px;
            text-align: center;
        }
        .product-list {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            padding: 20px;
        }
        .product {
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            margin: 10px;
            padding: 20px;
            width: 200px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .product img {
            max-width: 100%;
            border-radius: 8px;
        }
        .product h3 {
            font-size: 18px;
            margin: 10px 0;
        }
        .product p {
            font-size: 16px;
            color: #6d6875;
        }
        .product a {
            display: inline-block;
            margin-top: 10px;
            padding: 10px 15px;
            background-color: #6d6875;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        .product a:hover {
            background-color: #5a5560;
        }
    </style>
</head>
<body>
    <header>
        <h1>Cozy Market</h1>
        <p>Уютные товары для дома и души</p>
    </header>

    <div class="product-list">
        {% for product in products %}
        <div class="product">
            <img src="{{ product.image }}" alt="{{ product.name }}">
            <h3>{{ product.name }}</h3>
            <p>{{ product.price }} грн</p>
            <a href="{{ product.link }}">Купить</a>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template, products=products)

if __name__ == '__main__':
    app.run(debug=True)
