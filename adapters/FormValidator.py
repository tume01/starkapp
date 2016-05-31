from django.contrib import messages

class FormValidator():

    @staticmethod
    def validateForm(form, request):

        if not form.is_valid():

            errors = form.errors.as_data()

            for error in errors:

                validation_instance = errors[error]

                for instance_error in validation_instance:

                    for error_message in instance_error:

                        messages.error(request, (error_message))

            return request

        return False