from flask import jsonify, request
from app.routes import users_bp
from app.models import User
from app import db


@users_bp.route('', methods=['GET'])
def get_users():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    users = [User(
        id=row[0],
        name=row[1],
        email=row[2],
        email_verified_at=row[3],
        password=row[4],
        password_recovery_code=row[5],
        remember_token=row[6],
        created_at=row[7],
        updated_at=row[8],
        status_id=row[9],
        profile_id=row[10],
        document=row[11],
        token_2fa=row[12]
    ) for row in result]
    cursor.close()
    return jsonify({'users': [user.to_dict() for user in users]})

# endpoint em construcao
@users_bp.route('', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')
    email = data.get('email')

    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO users (name, password, email) VALUES (%s, %s, %s)", (name, password, email))
    db.commit()
    cursor.close()

    return jsonify({'message': 'User created successfully'}), 201


@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    result = cursor.fetchone()
    if result:
        user = User(
            id=result[0],
            name=result[1],
            email=result[2],
            email_verified_at=result[3],
            password=result[4],
            password_recovery_code=result[5],
            remember_token=result[6],
            created_at=result[7],
            updated_at=result[8],
            status_id=result[9],
            profile_id=result[10],
            document=result[11],
            token_2fa=result[12]
        )
        cursor.close()
        return jsonify(user.to_dict())
    else:
        cursor.close()
        return jsonify({'message': 'User not found'}), 404
