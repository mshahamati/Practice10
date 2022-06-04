
from media import *


class Series(Media):
    critics = None
    part_num = None
    subject = None

    def add_data(self):
        Media.add_data(self)
        self.critics = Media.get_list(self, 'Critics')
        self.part_num = input('Please Inter Part Number: ')
        self.subject = 'Series'

    def edit_data(self, arg_nam, arg_i):
        Media.edit_data(self, arg_nam, arg_i)
        self.critics = Media.get_list(self, 'Critics')
        self.part_num = input('Please Inter Part Number: ')
        self.subject = 'Series'
