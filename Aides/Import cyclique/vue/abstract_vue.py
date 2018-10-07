from vue.session import Session


class AbstractVue:
    session = Session()

    # Un petit contructeur pour inititier mon nombre d'iteration. Il est direction mis en session
    def __init__(self):
        if (not AbstractVue.session.iteration):
            AbstractVue.session.iteration = 1

    def display_info(self):
        pass

    def make_choice(self):
        pass
