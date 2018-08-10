
class _ParticipantPreferredMethodsOfContact(object):
    PHONE_MOBILE = ('PHONE_MOBILE', 'Mobile phone')
    PHONE_STATIC = ('PHONE_STATIC', 'Home phone')
    EMAIL = ('EMAIL', 'Email')
    FACEBOOK = ('FACEBOOK', 'Facebook')

    def as_choices(self):
        return [self.PHONE_MOBILE, self.PHONE_STATIC, self.EMAIL, self.FACEBOOK]


PARTICIPANT_PREFERRED_METHODS_OF_CONTACT = _ParticipantPreferredMethodsOfContact()
