from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data
students = [
    {"id": 1, "name": "Anisha Karki", "course": "IT"},
    {"id": 2, "name": "Bishal", "course": "CS"},
]

# GET → all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# POST → add new student
@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    students.append(new_student)
    return jsonify({"message": "Student added!", "data": new_student}), 201

# PUT → update student by id
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    for s in students:
        if s["id"] == id:
            s.update(request.get_json())
            return jsonify({"message": "Student updated!", "data": s})
    return jsonify({"error": "Student not found"}), 404

# DELETE → remove student by id
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s["id"] != id]
    return jsonify({"message": f"Student with id {id} deleted"})

if __name__ == '__main__':
    app.run(debug=True)
