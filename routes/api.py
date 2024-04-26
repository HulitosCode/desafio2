from app import app,db, request, jsonify
from Entity.Meal import Meal

@app.route('/meals', methods=['POST'])
def create_meal():
    data = request.json
    new_meal = Meal(
        name=data['name'],
        description=data['description'],
        is_within_diet=data['is_within_diet']
    )
    db.session.add(new_meal)
    db.session.commit()
    return jsonify({'message': 'Meal created successfully'}), 201

@app.route('/meals/<int:meal_id>', methods=['GET'])
def get_meal(meal_id):
    meal = Meal.query.get_or_404(meal_id)
    return jsonify({
        'id': meal.id,
        'name': meal.name,
        'description': meal.description,
        'date_time': meal.date_time.strftime('%Y-%m-%d %H:%M:%S'),
        'is_within_diet': meal.is_within_diet
    })

@app.route('/meals/<int:meal_id>', methods=['PUT'])
def update_meal(meal_id):
    meal = Meal.query.get_or_404(meal_id)
    data = request.json
    meal.name = data['name']
    meal.description = data['description']
    meal.is_within_diet = data['is_within_diet']
    db.session.commit()
    return jsonify({'message': 'Meal updated successfully'}), 200

@app.route('/meals/<int:meal_id>', methods=['DELETE'])
def delete_meal(meal_id):
    meal = Meal.query.get_or_404(meal_id)
    db.session.delete(meal)
    db.session.commit()
    return jsonify({'message': 'Meal deleted successfully'}), 200

@app.route('/meals', methods=['GET'])
def get_all_meals():
    meals = Meal.query.all()
    result = []
    for meal in meals:
        result.append({
            'id': meal.id,
            'name': meal.name,
            'description': meal.description,
            'date_time': meal.date_time.strftime('%Y-%m-%d %H:%M:%S'),
            'is_within_diet': meal.is_within_diet
        })
    return jsonify(result)
