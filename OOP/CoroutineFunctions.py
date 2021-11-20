def searcher():
    import time
    print("Pausing for 3 secs.")
    book = "hello my name is ali asar"
    # Suppose we are reading data from a big file or database so we have taken sleep()
    time.sleep(3)

    while True:
        word = (yield)
        print(f"Searching word '{word}' in novel.")
        if word in book:
            print(f"{word} word found in book.")
        else:
            print(f"'{word}' word not found in book.")    

s = searcher()
next(s)
# data is saved now and now the reading will not happen anymore infact it will check word from data saved.
s.send("is")
s.send("ali")
s.send("kam")
s.close()
