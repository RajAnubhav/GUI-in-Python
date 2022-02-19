class Calc:
    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age

    def info(self):
        return (self.name, self.jobs)


rec1 = Calc("Bob", ['dev', 'mgr'], 45)
rec2 = Calc("Sue", ['dev', 'cto'])

print(rec1.jobs)
print(rec2.info)
