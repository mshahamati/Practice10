from media import *

list_film = []


class Film(Media):
    subject = None
    critics = None
    ages = None
    honors = None

    def add_data(self):
        Media.add_data(self)
        self.critics = Media.get_list(self, 'Critics')
        self.ages = input('Please Inter Age Rate: ')
        self.honors = Media.get_list(self, 'Honors')
        self.subject = 'Film'

    def edit_data(self, arg_nam, arg_i):
        Media.edit_data(self, arg_nam, arg_i)
        self.critics = Media.get_list(self, 'Critics')
        self.ages = input('Please Inter Age Rate: ')
        self.honors = Media.get_list(self, 'Honors')
        self.subject = 'Film'

    def show_info(self):
        Media.show_info(self)
        print(f'critics: {self.critics} \t Ages: {self.ages} \n Honors: {self.honors}')

    def add_film(self):
        pass

