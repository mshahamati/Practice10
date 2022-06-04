
from media import *


class Documentary(Media):
    critics = None
    ages = None
    honors = None

    def add_data(self):
        Media.add_data(self)
        self.critics = Media.get_list(self, 'Critics')
        self.ages = input('Please Inter Age Rate: ')
        self.honors = Media.get_list(self, 'Honors')
        self.subject = 'Documentary'

    def edit_data(self, arg_nam, arg_i):
        Media.edit_data(self, arg_nam, arg_i)
        self.critics = Media.get_list(self, 'Critics')
        self.ages = input('Please Inter Age Rate: ')
        self.honors = Media.get_list(self, 'Honors')
        self.subject = 'Documentary'
