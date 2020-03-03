from notebook import Notebook, Note
from menu import Menu

# Exploring Note
print("Let's explore Note: \n")
note = Note("It's a new notebook.")
print('memo: ', note.memo)
print('memo type: ', type(note.memo))
print('id: ', note.id)
print('id type: ', type(note.id))
print('creation date: ', note.creation_date)
print('creation date type: ', type(note.creation_date), '\n')

print('Exploring some class methods: ')
print("method match: ")
print(note.match('new'))
print(note.match('hello'))

print('\nAll attributes of class Note: ')
print(dir(Note))

print("\nDocumentation of note: ")
print(note.__doc__)

print("Type of note: ")
print(type(note))

print("\nWhether note is object: ")
print(isinstance(note, object))

print("\nWhether note is Note: ")
print(isinstance(note, Note))

print("\nAll attributes of note: ")
print(note.__dir__())


# Exploring Notebook
print("\nLet's explore Notebook: ")
notebook = Notebook()

print('\nExploring some class methods: ')
print('method new_note: ')  # checking method new note
note2 = Note('Hello!', 'w')
notebook.new_note(note2.memo, note2.tags)
note3 = Note('Hi', 'world!')
notebook.new_note(note3.memo, note3.tags)
for note in notebook.notes:
    print(note.__dict__)
print('method _find_note: ')  # checking method find note
res = notebook._find_note(notebook.notes[1].id)
print(res.memo)
print('method modify_memo:')  # checking method modify memo
notebook.modify_memo(notebook.notes[1].id, 'Hey')
print(notebook.notes[1].memo)
print('method modify_tags: ')  # checking method modify tags
notebook.modify_tags(notebook.notes[1].id, 'wow')
print(notebook.notes[1].tags)
print('method search: ')  # checking method search
for note in notebook.search('w'):
    print(note.memo)

print('\nAll attributes of Notebook: ')
print(dir(Notebook))

print("\nDocumentation of notebook: ")
print(notebook.__doc__)

print("Type of notebook: ")
print(type(notebook))

print("\nWhether notebook is object: ")
print(isinstance(notebook, object))

print("\nWhether notebook is Notebook: ")
print(isinstance(notebook, Notebook))

print("\nAll attributes of notebook: ")
print(notebook.__dir__())

# Exploring menu
print("\nLet's explore Menu: ")
menu = Menu()

print('All attributes of class Menu: ')
print(dir(Menu))

print("\nDocumentation of menu: ")
print(menu.__doc__)

print("Type of menu: ")
print(type(menu))

print("\nWhether menu is object: ")
print(isinstance(menu, object))

print("\nWhether menu is Menu: ")
print(isinstance(menu, Menu))

print("\nAll attributes of menu: ")
print(menu.__dir__())


