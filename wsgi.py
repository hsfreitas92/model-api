from app import create_app

app = create_app('development')  # Substitua 'development' pelo nome do ambiente desejado (por exemplo, 'production')

if __name__ == '__main__':
    app.run()
