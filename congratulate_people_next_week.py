from datetime import datetime, timedelta

'''Uncomment 'users' below and run the code, if you want to test.'''

users = [{"name": "Rob Taylor", "birthday": datetime(1975, 1, 2)},
         {"name": "Stenly Fox", "birthday": datetime(1985, 10, 17)},
         {"name": "Bill Gates", "birthday": datetime(1995, 10, 20)},
         {"name": "Sasha Dike", "birthday": datetime(1959, 10, 20)},
         {"name": "Trinity Step", "birthday": datetime(1935, 11, 28)},
         {"name": "Stefan Teneth", "birthday": datetime(1935, 12, 29)},
         {"name": "Jack Smith", "birthday": datetime(1935, 12, 30)},
         {"name": "Maria", "birthday": datetime(1995, 10, 21)}]

MAXDAYINDEX = 6
WORKDAYS = 5


def get_key(user):
    return user['birthday']


def get_birthdays_per_week(users: list):
    users = sorted(users, key=get_key)
    today = datetime.today().date()
    today_weekday = today.weekday()
    celebrate = {}
    delta_days = timedelta(MAXDAYINDEX - today_weekday + WORKDAYS)
    for user in users:
        was_born = user['birthday'].date()
        birthday = was_born.replace(year=today.year)
        if birthday < today-timedelta(days=2):
            birthday = was_born.replace(year=today.year+1)
        user_weekday = birthday.strftime('%A')
        if user_weekday == 'Saturday':
            birthday += timedelta(days=2)
            user_weekday = 'Monday'
        if user_weekday == 'Sunday':
            birthday += timedelta(days=1)
            user_weekday = 'Monday'
        if today < birthday <= (today + delta_days):
            if user_weekday not in celebrate:
                celebrate[user_weekday] = []
            celebrate[user_weekday].append(user['name'])
    for day, people in celebrate.items():
        print(day+': ' + ', '.join(people))


if __name__ == '__main__':
    get_birthdays_per_week(users)
