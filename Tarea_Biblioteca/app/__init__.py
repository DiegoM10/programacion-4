from app.biblioteca import creacion,menu

if __name__ == '__main__':
    try:
        creacion()
        menu()
    except Exception as e:
        menu()
        print(e)
        print('Success!')