my_dict={"a":1,"b":2,"c":3}
try:
    value=my_dict["d"]
except IndexError:
    print("This index does not exist!")
except KeyError:
    print("This key is not in the dictionary")
except:
    print("Some other error occurred!")




