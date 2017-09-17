class FakeMe:
    def __init__(self):
        self.name = '<Fake Twitter User>'

    def __call__(self):
        return self

class FakeAPI:
    def __init__(self):
        self.me = FakeMe()

    def me():
        return self.me

    def update_status(self, *, status='<NO ACTUAL STATUS CHANGE GIVEN!>'):
        print('FAKE API: update_status() called (status text not shown)')

    # for debugging purposes
    def __repr__(self):
        return 'FakeAPI instance'
