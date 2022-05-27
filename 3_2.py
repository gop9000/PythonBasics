usr = {'name': 'Vanya',
       'second_name': 'Vanin',
       'year': '1900',
       'city': 'Karaganda',
       'e-mail': '1@1.local',
       'phone': '+79998887766'
       }


def my_f(name, sname, year, city, email, phone):
    print(f"Name is {name}, Second name is {sname}, age is {int(2022 - int(year))}, city is {city}, email is {email}, "
          f"phone number is {phone}.")


my_f(name=usr.get('name'), sname=usr.get('second_name'), year=usr.get('year'), city=usr.get('city'),
     email=usr.get('e-mail'), phone=usr.get('phone'))
