# utils.py

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.teacher.user.id}/{filename}'


def course_image_upload_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<user_id>/course_<course_number>/<filename>
    return f'user_{instance.teacher.user.id}/course_{instance.course_number}/{filename}'
