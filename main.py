from film import *
from documentary import *
from clip import *
from series import *
import json

list_class = [Film, Documentary, Clip, Series]
# Load File
Media.load_file(self=Media)

while True:
    Media.type_film(self=Media)
    while True:
        Media.show_menu(self=Media)
        get_choice = Media.get_manage_menu
        if get_choice == '1' or get_choice == 'add':
            for i in range(len(Media.get_type)):
                if Media.get_type_film == list_class[i].__name__:
                    temp = list_class[i]()
                    temp.add_data()
                    jsonStr = json.dumps(temp.__dict__)
                    list_all.append(eval(jsonStr))
                    temp.save_file(list_all)
            flag = input('Do you want Continue "y" or Back to Menu "n":  ')
            if flag == 'n':
                break
            else:
                continue

        if get_choice == '2' or get_choice == 'edit':
            while True:
                r = Media.search_media(self=Media)
                if len(r) == 1:
                    for i in range(len(list_all)):
                        if r[0]['id'] == list_all[i]['id']:
                            print('Change Value For', list_all[i]['name'], 'by ID: ', list_all[i]['id'])
                            for h in range(len(Media.get_type)):
                                if (r[0]['subject'].lower()) == (list_class[h].__name__.lower()):
                                    temp_edit = list_class[h]()
                                    temp_edit.edit_data(r[0]['name'], r[0]['id'])
                                    jsonStr = json.dumps(temp_edit.__dict__)
                                    list_all.append(eval(jsonStr))
                                    print('Successful editing', list_all)
                                    list_all.pop(i)
                                    temp_edit.save_file(list_all)
                            break
                            print('List all = ', list_all[i])
                conti_while = input('Do you want try again : y/n')
                if conti_while == 'n':
                    break
        if get_choice == '3' or get_choice == 'remove':
            while True:
                r = Media.search_media(self=Media)
                if len(r) == 1:
                    for i in range(len(list_all)):
                        if r[0]['id'] == list_all[i]['id']:
                            for h in range(len(Media.get_type)):
                                if (r[0]['subject'].lower()) == (list_class[h].__name__.lower()):
                                    temp_edit = list_class[h]()
                                    list_all.pop(i)
                                    print('Successful Removed', list_all)
                                    temp_edit.save_file(list_all)
                conti_while = input('Do you want try again : y/n')
                if conti_while == 'n':
                    break
        if get_choice == '4' or get_choice == 'search':
            Media.search_media(self=Media)


