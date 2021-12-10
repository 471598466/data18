import configparser
from conf.get_path import *
class ReadConfig:
    @staticmethod
    def read_config(file_name,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_name,encoding='utf-8')
        return cf.get(section,option)
        # return cf[section][option]

    @staticmethod
    def setConfig(file_name,section,option,value):
        cf=configparser.ConfigParser()
        cf.read(file_name, encoding='utf-8')
        cf.set(section,option,value)
        with open(file_name, "w+") as f:
            cf.write(f)

if __name__ == '__main__':
    # print(ReadConfig.read_config(config_path,'MODE','mode1'))
    print(ReadConfig.read_config(config_path, 'DB', 'db_config'))
    # mode2=eval(ReadConfig.read_config(config_path, 'MODE', 'mode2'))
    # for key in mode2:
    #     for value in mode2[key]:
    #         print(type(mode2[key]))




