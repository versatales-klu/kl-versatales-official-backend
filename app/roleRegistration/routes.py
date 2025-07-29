from flask import Blueprint, request, jsonify
from app.utils import check_registration_status, add_role_registration

role_registration_bp = Blueprint('role_registration', __name__)

@role_registration_bp.route('/', methods=['GET'])
def role_registration_home():
    return jsonify({'status': True})


@role_registration_bp.route('/initial-role-form-submit', methods=['POST'])
def initial_form():
    data = request.get_json()
    college_id = data.get('college_id')
    name = data.get('name')
    mail = data.get('mail')

    if not all([college_id, name, mail]):
        return jsonify({'status': False, 'message': 'Missing required fields'}), 400

    already_registered = check_registration_status(mail)

    return jsonify({'status': not already_registered})


@role_registration_bp.route('/full-role-form-submit', methods=['POST'])
def detail_form():
    data = request.get_json()

    required_fields = [
        'college_id', 'name', 'mail', 'year', 'gender',
        'dept', 'wingname'
    ]

    if not all(field in data for field in required_fields):
        return jsonify({'status': False, 'message': 'Missing required fields'}), 400

    success = add_role_registration(
        college_id=data['college_id'],
        name=data['name'],
        mail=data['mail'],
        year=int(data['year']),
        gender=data['gender'],
        dept=data['dept'],
        wingname=data['wingname'],
        reason=data.get('reason'),
        experience=data.get('experience')
    )

    return jsonify({'status': success})
