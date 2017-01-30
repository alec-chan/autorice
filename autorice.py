import os
autorice_main_dir="~/autorice/"
autorice_rice_dir=autorice_main_dir+"rices/"
#holds parameters for a rice.
class Rice:
    name=""
    author=""
    version=""
    sections={}
    deps={}

    def install():
        #create a new directory for our rice
        #OSError will be raised if it exists, so add exception catch..
        this_rice_dir=autorice_rice_dir+name+"/"
        os.mkdir(this_rice_dir)
        for s in sections:
            for key in s.params:
                os.symlink(this_rice_dir+key, s.params[key] )

class Section:
    name=""
    params={}

def readconf():
    import ConfigParser
    Config=ConfigParser.ConfigParser()
    Config.read()
    sects={}
    rice = {}
    r = Rice()
    for section in Config.sections():

        if section == 'Rice':
            rice = ConfigSectionMap(section)
            r.name=rice['name']
            r.author=rice['author']
            r.version=rice['version']
        elif section == 'Deps':
            r.deps=ConfigSectionMap(section)
        else:
            s = Section()
            s.name=section
            s.params=ConfigSectionMap(section)
            sects[section] = s

    r.sections=sects

#source: https://wiki.python.org/moin/ConfigParserExamples
def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

#untar the rice archive to our autorice_dir
def openrice(path):
    import tarfile
    #tarfile.open()
    #...

