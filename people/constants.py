
class _ParticipantPreferredMethodsOfContact(object):
    PHONE_MOBILE = 'PHONE_MOBILE'
    PHONE_STATIC = 'PHONE_STATIC'
    EMAIL = 'EMAIL'
    FACEBOOK = 'FACEBOOK'

    def as_choices(self):
        return [
            (self.PHONE_MOBILE, self.PHONE_MOBILE),
            (self.PHONE_STATIC, self.PHONE_STATIC),
            (self.EMAIL, self.EMAIL),
            (self.FACEBOOK, self.FACEBOOK)
        ]


PARTICIPANT_PREFERRED_METHODS_OF_CONTACT = _ParticipantPreferredMethodsOfContact()
