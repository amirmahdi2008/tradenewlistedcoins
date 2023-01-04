#In The Creator Of Money | به نام آن که پول را آفرید

class ini:
    @staticmethod
    def configs():
        configs = dict()

        f = open("config.ini" , "r")
        lines = f.read().split("\n")

        for line in lines:
            splited = line.split("=")
            configs[splited[0].strip()] = splited[1].strip()

        f.close()

        return configs

    @staticmethod
    def get(item , default=""):
        return ini.configs()[item].strip()
