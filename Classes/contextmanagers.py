class Connector:
    def __init__(self, credentials = None):
        print("Inside __init__ method")
        self.credentials = credentials
    
    def __enter__(self):
        print("Inside __enter__ method")
        return self
    
    def __exit__(self, ex_type, ex_obj, traceback_obj):
        print("Inside __exit__ method")
        if ex_obj:
            print("Exception Handeled here")
            print(traceback_obj)
        return True
    
    def __del__(self):
        print("Inside __del__ method")
    
    def query(self):
        return {
            "data1" : [1, 2, 3, 4, 5],
            "data2": self.credentials
        }
    

def withException():
    with Connector() as c:
        print(c.query())
        z = 1/0
        print("I won't get printed")

def withoutException():
    with Connector() as c:
        print(c.query())
        print(c.query())
    
withException()
print("I get printed even after exception")

# withoutException()