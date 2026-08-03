class UserAlreadyExistsException(Exception):
    pass


class InvalidCredentialsException(Exception):
    pass


class UserNotFoundException(Exception):
    pass


class InvalidRefreshTokenException(Exception):
    pass

class QuestionNotFoundException(Exception):
    def __init__(self, interview_id):
        self.interview_id = interview_id
