from django import template

register = template.Library()

@register.filter
def get_student_fields(student):
    fields = []
    for field in student._meta.fields:
        if field.name != 'id' and field.name != 'user':
            fields.append((field.verbose_name, field.value_from_object(student)))
    return fields
