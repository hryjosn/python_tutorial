from pymongo import MongoClient

conn_str = "mongodb+srv://hojaAdmin:blackozark@cluster0.8kb5d.mongodb.net/test?retryWrites=true&w=majority"

client = MongoClient(conn_str, serverSelectionTimeoutMS=5000)
mydb = client["ettoday"]
my_collection = mydb["user"]



try:
    # topic_list = [{"name": "Tom", "age": 26}, {"name": "Mary", "age": 18}, {"name": "Georgy", "age": 25}]
    #
    # my_collection.insert_many(topic_list)  # create
    #
    # for x in my_collection.find():  # Read
    #     print(x)
    # myquery = {"name": "Georgy"}
    # print("====================================")
    # for x in my_collection.find(myquery):
    #     print(x)
    myquery = {"name": "Mary"}
    newvalues = {"$set": {"weight": 43}}

    my_collection.update_one(myquery, newvalues)  # update
    myquery = {"name": "Tom"}

    my_collection.delete_one(myquery)
    for x in my_collection.find():  # Read
        print(x)
except Exception as e:
    print(e)
    print("Unable to connect to the server.")
