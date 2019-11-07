from django.conf import settings
#from sendgrid import SendGridAPIClient
#from sendgrid.helpers.mail import Mail


class UserService():

    def send_email_confirmation(self, email_confirmation):
        return True
        """message = Mail(
            from_email='confirmation@domain.com',
            to_emails=email_confirmation.user.email
        )

        message.dynamic_template_data = {
            'subject': 'Test Account Activation',
            'username': email_confirmation.user.username,
            'email': email_confirmation.user.email,
            # 'link': settings.HOST + '/api/v1/users/{}/email_confirmation?identifier={}'.format(email_confirmation.user.id, email_confirmation.identifier)
            'link': 'http://10.42.18.113:8000/api/v1/users/{}/email_confirmation?identifier={}'.format(email_confirmation.user.id, email_confirmation.identifier)
        }

        message.template_id = 'd-f65aea5010a54b8f8aba0a67dfa0f312'

        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            print(response.status_code)
            return True
        except Exception as e:
            print(e.message)
            return False"""
