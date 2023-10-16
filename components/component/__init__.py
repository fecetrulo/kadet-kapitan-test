from kapitan.inputs import kadet

def main():
    with open("./redis.conf", "r", encoding="utf-8") as file:
        test = kadet.BaseObj()
        test.root.test.data = file.read()
        return test