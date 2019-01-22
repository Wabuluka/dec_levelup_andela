from flask import jsonify
from validate_email import validate_email


def validate_user_details(firstname, lastname, othernames, email, phonenumber, username, password):
    if not firstname and lastname and othernames and email and phonenumber and username and password:
        return jsonify({"message": "all fields are required"}), 400
    
    valid_email = validate_email(email)
    if not valid_email:
        return jsonify({
            "message": "Please use a valid email address for example nich@gmail.com"
        }), 400


    if not isinstance(firstname, str) or not isinstance(lastname, str) or not isinstance(othernames, str) or not isinstance(username, str):
        return jsonify({"message":"string needed here"})




        

    # if not firstname == "" and lastname == "" and othernames == "" and email == "" \
    #         and phonenumber == "" and username == "" and password == "":
    #     return jsonify({"message": "fields cant be  empty"}), 400

    # valid_email = validate_email(email)
    # if not valid_email:
    #     return jsonify({
    #         "error": "Please use a valid email address for example nich@gmail"
    #     }), 400

    # if not firstname.isalpha() or not lastname.isalpha():
    #     return jsonify({
    #         "error": "First and last name should only be alphabets"
    #     }), 400







# class Validator:

#     def input_check(self, input_check):
#         if str(user_input).replace(" ", "") == "":
#             return True
#         return False