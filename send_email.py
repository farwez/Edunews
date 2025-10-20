import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
import os
BREVO_API_KEY = os.getenv("BREVO_API_KEY")

def send_email(subject, html_content, receiver_email):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = BREVO_API_KEY
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": receiver_email}],
        sender={"email": "munnafarwez@gmail.com", "name": "EduPulse"},
        subject=subject,
        html_content=html_content
    )

    try:
        response = api_instance.send_transac_email(send_smtp_email)
        print("✅ Email sent successfully!", response)
    except ApiException as e:
        print("❌ Error:", e)

