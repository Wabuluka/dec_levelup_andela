from . import *

"""
    creating a red flag incident
"""
class CreateRedFlagMap(MethodView):
    
    def post(self, id):
        data = request.get_json()
        global count

        count +=1
        red_flag_record = CorruptionCase(
            id = data['id'],
            createdBy = data['createdBy'],
            caseType = data['caseType'],
            location = data['location'],
            status = data['status'],
            image = data['image'],
            video = data['video'],
            comment = data['comment']
        )
        red_flag_records.append(red_flag_record)
        return jsonify({"data": red_flag_record.case_dictionary()})
    