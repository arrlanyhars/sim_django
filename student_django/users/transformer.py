def transform(values):
    list_user = []

    for item in values:
        list_user.append(response_sign_up_and_sign_in(item))

    return list_user


def singleTransform(values):
    return {
        'id': values.u_id,
        'fullname': values.u_fullname,
        'email': values.u_email,
        'created_at': None
    }

def response_sign_up_and_sign_in(values):
    return {
        'id': values.u_id,
        'fullname': values.u_fullname,
        'nickname': values.u_nickname,
        'email': values.u_email,
        'whatsapp_number': values.u_whatsapp_number,
        'created_at': values.u_created_at
    }