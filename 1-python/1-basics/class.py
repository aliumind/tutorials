class Person():

    def __init__(self, firstname, lastname):
        print('Initialization class person')
        self.firstname = firstname
        self.lastname = lastname
        print('Initialization class person closed')

    def whoami(self):
        return self.firstname + ' ' + self.lastname

    def myjob(self):
        return 'do nothing everyday'


class Singer(Person):

    def __init__(self, firstname, lastname):
        print('Initialization class singer')
        super().__init__(firstname, lastname)
        print('Initialization class singer closed')

    def myjob(self):
        return "Singer"


if __name__ == '__main__':

    person = Person('Valerio', 'Mellini')
    print("PERSON")
    print("I'm " + person.whoami())
    print("My Job is " + person.myjob())
    print('\n')

    print("SINGER")
    singer = Singer('Valerio', 'Mellini')
    print("I'm " + singer.whoami())
    print("My Job is " + singer.myjob())
