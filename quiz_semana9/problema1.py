from string import ascii_letters
def corutine():

      n =  yield ascii_letters
      yield n



if __name__ == "__main__":
 
    abc = corutine()

    print(next(abc))


