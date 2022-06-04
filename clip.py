
from media import *


class Clip(Media):
    critics = None
    ages = None
    honors = None

    def add_data(self):
        Media.add_data(self)
        self.critics_Clip = Media.get_list(self, 'Critics')
        self.ages_Clip = input('Please Inter Age Rate: ')
        self.honors = Media.get_list(self, 'Honors')
        self.subject = 'Clip'

    def edit_data(self, arg_nam, arg_i):
        Media.edit_data(self, arg_nam, arg_i)
        self.critics_Clip = Media.get_list(self, 'Critics')
        self.ages_Clip = input('Please Inter Age Rate: ')
        self.subject = 'Clip'
