def transform(values):
    list_user = []

    for item in values:
        list_user.append(singleTransform(item))

    return list_user


def singleTransform(values):
    return {
        'id': values.u_id,
        'fullname': values.u_fullname,
        'email': values.u_email,
        'created_at': None
    }