#autorice

autorice creates a way for unix theme configurations or "rices" to be shared between people and easily installed with minimal setup.


##Rices
The basic setup for a rice is a tar archive containing a config file called autorice.conf which tells the program what to do with each of the files in the rice, and subdirectories each of which correspond to a different [Section] in the autorice.conf

##autorice.conf
autorice.conf is a configuration file written in the INI standard which contains all the mappings for the rice files as well as some info about the rice.  If a rice archive does not contain an autorice.conf on the highest level, autorice will not be able to do anything with it and will throw an error.

The headers (excluding [Rice] and [Dep]) correspond to subdirectories within the rice and each parameter under the section headers corresponds to a file in that subdirectory.  The value of each key indicates where the file should be symlinked to on the user's system.  If any subdirectories do not have section headers in autorice.conf, they will be ignored and if any files inside a subdirectory do not have keys under that section header, they will also be ignored.

A small example of an autorice.conf is below, for more detailed info see the autorice.conf.example file.

```
;both the [Rice] and [Dep] headers are required.
[Rice]
author: alec-chan
name: example-rice
version: 1.0.0

;the keys under the [Dep] header can be arbitrarily named, only the values have any importance.  
;Here I used 0-n as the keys but it really does not matter what they are.
;Currently the dependency checker only checks if the binary specified in the value is installed on the system 
;using the which command.  This means that the values have to match the names of the dependencies exactly.
;If any dependencies are not installed, the program will simply throw an error telling the user which dependencies
;need to be installed.
[Dep]
0: conky
1: i3wm

;maps to the directory /example-rice/Conky/
;can be arbitrarily named as long as it contains the name of an existing directory (case sensitive)
;In these user defined sections, the key should match up to a file within the directory that the section maps to.
;The value defines where the symlink will point to.
[Conky]
conky.conf: ~/.config/conky/conky.conf

;maps to /example-rice/i3/
[i3]
i3.conf: ~/.config/i3/i3.conf
```


