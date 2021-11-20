import time

def getOccurance(queries, sentences):
    counter = 0
    for query in queries:
        for sentence in sentences.split():
            if query.lower() == sentence:
                counter += 1
    return counter

if __name__ == '__main__':

    myList = ["this is good", "python is python of the python", "python is good", "python is not python snake"]
    query = input("Enter a string query to be searched: ").strip().split(" ")
    lst = []
    results = 0
    for i in myList:
        start_time = time.time()
        occur = getOccurance(query, i)
        if occur > 0:
            results += 1
        lst.append(occur)
        #time.sleep(1) For testing that time is working correctly
    totalTime = time.time() - start_time

    sorted = [score for score in sorted(zip(lst, myList), reverse = True) if score[0] != 0]
    print(f"\n{results} results found in {totalTime} seconds: ")
    for score, item in sorted:
        print(f"\"{item}\" with releavancy of {score}")
