from prettyinpecans import settings

import mailchimp

UPDATES_LIST_ID = '654f489fe4'

def get_mailchimp_api():
    return mailchimp.Mailchimp(settings.MAILCHIMP_API_KEY)

def subscribe_user(email):
    try:
        get_mailchimp_api().lists.subscribe(
            UPDATES_LIST_ID, {'email': email})
    except mailchimp.Error:
        print("Subscribe failed.")
        