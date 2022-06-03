from flask_restful import Resource
from ..models.StudentModel import Student, StudentSchema
from flask import jsonify, abort
from flask_restful import reqparse

student_serializer = StudentSchema()

post_parser = reqparse.RequestParser()
post_parser.add_argument("name", required=True, help="name is required")
post_parser.add_argument("age", type=int, required=True, help="age is required")
post_parser.add_argument("address")


class StudentListResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", location='args')
        args = parser.parse_args()

        students = Student.query
        if args.get("name"):
            search_name = "%{}%".format(args.get("name"))
            students = students.filter(Student.name.like(search_name))

        students = students.order_by(Student.id)
        data = student_serializer.dump(students, many=True)
        return jsonify(data)

    def post(self):
        data = post_parser.parse_args()
        student = Student(data)
        student.save()
        response_data = student_serializer.dump(student)
        return jsonify(response_data)


class StudentResource(Resource):
    def get(self, student_id):
        student = Student.query.get(student_id)
        if not student:
            abort(404, 'resource not found')
        response_data = student_serializer.dump(student)
        return jsonify(response_data)

    def post(self, student_id):
        data = post_parser.parse_args()
        student = Student.query.get(student_id)
        student.update(data)

        return 'success'

    def delete(self, student_id):
        student = Student.query.get(student_id)
        if not student:
            raise abort(404, 'resource not found')
        student.delete()
        return 'success'

