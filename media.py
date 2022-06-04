# list_all = []
global list_search
list_search = []
global total_numbers
total_numbers = 0

global list_all
list_all = []


class Media:
    name = None
    director = None
    imdb_score = None
    url = None
    duration = None
    casts = None
    id = None
    get_manage_menu = None
    get_type = ['Film', 'Documentary', 'Series', 'Clip']
    get_type_film = None

    def get_time(self):
        hours = int(input('Please Inter Hours Time:'))
        minutes = int(input('Please Inter Minutes Time: '))
        second = int(input('Please Inter Second Time: '))
        return (hours * 3600) + (minutes * 60) + second

    def show_time(self, second):
        h = second // 3600
        second = second % 3600
        m = second // 60
        m % 60
        return f'{h}:{m}:{m % 60}'

    def add_data(self):
        self.name = input('Please Inter Name: ')
        self.director = input('Please Inter director: ')
        self.imdb_score = input('Please Inter IMDB Score: ')
        self.url = input('Please Inter URL:')
        self.duration = self.get_time()
        self.casts = self.get_list('Casts')
        self.id = input('Please Inter ID Number: ')
        global total_numbers
        total_numbers += 1

    def edit_data(self, arg_name, arg_id):
        self.name = arg_name
        self.id = arg_id
        self.director = input('Please Inter director: ')
        self.imdb_score = input('Please Inter IMDB Score: ')
        self.url = input('Please Inter URL:')
        self.duration = self.get_time()
        self.casts = self.get_list('Casts')

    def get_list(self, name):
        get_list_item = []
        while True:
            get_list_item.append(input(f'For Exit typed "exit" Please Inter {name}: '))
            if get_list_item[-1] == 'exit':
                get_list_item.remove('exit')
                return get_list_item

    def show_info(self):
        print(f'Name: {self.name} \t Director: {self.director} \n IMDB Score: {self.imdb_score} \t URL: {self.url} \n'
              f'Duration: {self.duration} \t Casts: {self.casts} \n Number Of Code: {self.id} \t'
              f'Number of Totals: {total_numbers}')

    def show_menu(self):
        print('1- Add')
        print('2- Edit')
        print('3- Remove')
        print('4- Search')
        print('5- Show Information And Download')
        print('6- Back to Main Menu')
        self.get_manage_menu = input(f'Select Numbers Menu For {self.get_type_film}:')

    def type_film(self):
        self.get_type = ['Film', 'Documentary', 'Series', 'Clip']
        for b in range(len(self.get_type)):
            print(f'{b + 1}-{self.get_type[b]}')
        self.get_type_film = self.get_type[int(input('Please Select Numbers: ')) - 1]

    def save_file(self, list_all):
        file = open('database.txt', 'w')
        print(list_all)
        stored = repr(list_all)
        file.write(stored)
        file.close()

    def load_file(self):
        file = open('database.txt', 'r')
        list_all_func = file.read()
        file.close()
        global list_all
        if list_all_func != '':
            temp_list_all = eval(list_all_func)
            print(len(temp_list_all))
            print(type(temp_list_all))
            for i in range(len(temp_list_all)):
                list_all.append(temp_list_all[i])

    def search_media(self):
        global list_search
        temp_list_search = []
        flag = False
        search = input('Search by ID Number or Name: For Search by Time Press "t"  or Exit typed "exit"')

        if search == 't':
            flag = True
            time_search_1 = self.get_time(self)
            print('Please Inter Time Two')
            time_search_2 = self.get_time(self)

        if search == 'exit':
            exit()

        for i in range(int(len(list_all))):
            if flag and (int(time_search_1) < int(list_all[i]['duration']) and int(list_all[i]['duration']) < int(time_search_2)):
                temp_list_search.append(list_all[i])
            if not flag and (search in list_all[i]['id'] or search in list_all[i]['name']):
                temp_list_search.append(list_all[i])
                # print(list_all[i])
        if len(temp_list_search) == 1:
            print(f'Result: {len(temp_list_search)}')
            print(temp_list_search[-1])

        if len(temp_list_search) > 1:
            print('Please carefully data entry Try again')
            print(f'Result: {len(temp_list_search)}')
            for b in range(len(temp_list_search)):
                print(f'Do you mean: Name Select = {temp_list_search[b]["name"]} or ID Select {temp_list_search[b]["id"]} '
                      f'or Time {self.show_time(self, int(temp_list_search[b]["duration"]))}')

        list_search = temp_list_search.copy()
        temp_list_search.clear()
        return list_search
