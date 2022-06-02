from flask_restful import Resource
from ..models.StudentModel import Student, StudentSchema
from flask import jsonify, request
from flask_restful import reqparse

student_serializer = StudentSchema()


class StudentResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", location='args')
        args = parser.parse_args()
        students = Student.query.filter(name=args.get("name")).all()
        data = student_serializer.dump(students, many=True)
        return jsonify(data)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True, help="name is required")
        parser.add_argument("age", type=int, required=True, help="age is required")
        parser.add_argument("address")

        data = parser.parse_args()
        student = Student(data)
        student.save()
        response_data = student_serializer.dump(student)
        return jsonify(response_data)
