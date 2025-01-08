# class Loader:
#     def __init__(self):
#         self.name = "Loader"
#         self.data = None

#     def load(self):
#         print("Loading...")


# class CSVLoader(Loader):
#     def __init__(self):
#         super().__init__()
#         self.name = "CSVLoader"
#         self.data = "CSV Data"


# class JSONLoader(CSVLoader):
#     def __init__(self):
#         self.name = "JSONLoader"
#         self.data = "JSON Data"


# loader = JSONLoader()


class MyTest:
    def __init__(self):
        self.name = "MyTest"
        self.fullname = "MyTest"

    @staticmethod
    def test(fullname):
        print("Test" + fullname)


mt = MyTest()
mt.test("MyTest")
