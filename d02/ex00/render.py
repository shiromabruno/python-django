import os
import sys
import re
import settings

# myCV.template
def main(template_file):    

    f = open(template_file, "r")

    # "".join(input_file.readlines()) reads all the lines from the file.
    template = "".join(f.readlines())

    # f.readlines() fica []
    # template2 = f.readlines()
    f.close()

    #txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
    #txt2 = "My name is {0}, I'm {1}".format("John",36)
    #txt3 = "My name is {}, I'm {}".format("John",36) 
    file = template.format(name=settings.name, surname=settings.surname, title=settings.title,
        age=settings.age, profession=settings.profession)
    

    #We can combine a regular expression pattern into pattern objects, which can be used for pattern matching.
    #Example:
    #pattern=re.compile('TP')
    #result=pattern.findall('TP Tutorialspoint TP')
    #print result #  ----> ['TP', 'TP']
    #result2=pattern.findall('TP is most popular tutorials site of India')
    #print result2 #  ----> ['TP']
    regex = re.compile("(\.template)")


    template_file = "".join([template_file[0:regex.search(template_file).start()], ".html"]) # criou como myCV.html
    #template_file = "".join([template_file.split('.')[0], ".html"]) # criou como myCV.html
    #template_file = "".join([template_file[0], ".html"]) # criou como m.html

    f = open(template_file, "w")
    f.write(file)
    f.close()

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Necessario 2 argumentos apenas")
        sys.exit(1)

    template_file = sys.argv[1]

    if not template_file.endswith('.template'):
        print("Arquivo nao termina com .template")
        sys.exit(1)

    if not os.path.isfile(template_file):
        print("Arquivo com extensao template nao existe")
        sys.exit(1)
    
    try:
        main(template_file)
    except Exception as ex:
        print (ex)