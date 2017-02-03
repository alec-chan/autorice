import os
import argparse
import logging
import tarfile
autorice_main_dir="~/autorice/"
autorice_rice_dir=autorice_main_dir+"rices/"
#holds parameters for a rice.
class Rice:
    name=""
    author=""
    version=""
    sections={}
    deps={}

    def install(path):
        #create a new directory for our rice
        #OSError will be raised if it exists, so add exception catch..
        this_rice_dir=autorice_rice_dir+name+"/"
        os.mkdir(this_rice_dir)
        for s in sections:
            for key in s.params:
                os.symlink(this_rice_dir+key, s.params[key] )

    def unpackage(path):
        if tarfile.is_tarfile(path):
            print 'Rice is a valid tarfile, extracting..'
            tar = tarfile.open(name=path)
            


    def arg_parser():
        parser = argparse.ArgumentParser(description='Automatic Rice Installer')
        parser.add_argument('-i','--install', help='unpackages and install a rice given the rice tarball, or if already installed, the name.', required=False)
        parser.add_argument('-r','--remove', help='uninstall a rice given the name. NOTE: leaves files in ~/autorice/rices/', required=False)
        parser.add_argument('-u', '--unpackage', help='unpackages a rice tarball into the ~/autorice/rices/ directory.')
        args = vars(parser.parse_args())

        if args['install'] != '':
            self.install(args['install'])

        elif args['remove'] != '':
            self.uninstall(args['uninstall'])
        elif args['unpackage'] != '':
            self.unpackage(args['unpackage'])

    


#represents a section header in autorice.conf
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
        elif section == 'Dep':
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



def main():








if __name__ == '__main__':
    main()

