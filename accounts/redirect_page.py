from .models import User

new_cred = User.objects.create(username="John", is_student=True)
def redirect_to_profile_page(user):
    if user.is_student == True:
        return 'student_page'
    else:
        return 'teacher_page' 
