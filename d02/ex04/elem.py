#!/usr/bin/python3

class Text(str):
    def __str__(self):
        return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')


class Elem:

    #teste
    class ValidationError(Exception):
        def __init__(self) -> None:
            super().__init__("Error durante a execucao!")

    def __init__(self, tag: str = 'div', attr: dict = {}, content=None, tag_type: str = 'double'):
        #teste
        self.tag = tag
        self.attr = attr
        self.content = []
        if not (self.check_type(content) or content is None):
            raise self.ValidationError
        if type(content) == list:
            self.content = content
        elif content is not None:
            self.content.append(content)
        if (tag_type != 'double' and tag_type != 'simple'):
            raise self.ValidationError
        self.tag_type = tag_type

    def __str__(self):
        #teste
        attr = self.__make_attr()


        result = "<{tag}{attr}".format(tag=self.tag, attr=attr)
        if self.tag_type == 'double':
            result += ">{content}</{tag}>".format(
                content=self.__make_content(), tag=self.tag)
        elif self.tag_type == 'simple':
            result += " />"
        return result

    def __make_attr(self):
        result = ''

        #  example = {
        #   "href": "https://www.example.com",
        #   "target": "_blank",
        #   "title": "Visit Site" 
        #   }
        # self.attr.items() ---> [('href', 'https://www.example.com'), ('target', '_blank'), ('title', 'Visit Site')]
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result
        # href="https://www.example.com" target="_blank" title="Visit Site"

    def __make_content(self):
        
        # content eh uma lista de ELEM ou lista de TEXT
        if len(self.content) == 0:
            return ""
        result = "\n"
        for elem in self.content:
            #teste
            if (len(str(elem)) != 0):
                # Elem(content=[Text('foo'), Text('bar'), Elem()])
                # vai printar em sequencia:
                # foo
                # foo
                # bar
                # <div></div>
                # OU '<div>\n  foo\n  bar\n \<div></div>\n</div>'
                result += "{elem}\n".format(elem=elem)
        #splitlines(True) txt = "Thank you for the music\nWelcome to the jungle" ----> ['Thank you for the music\n', 'Welcome to the jungle'] 
        result = "  ".join(line for line in result.splitlines(True))
        if len(result.strip()) == 0:
            return ''
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


def test():
    #teste
    html = Elem('html', content=[
                Elem('head', content=
                     Elem('title', content=Text("Hello ground!"))),
                Elem('body', content=
                     [Elem('h1', content=Text("Oh no, not again!")),
                      Elem('img', {'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')])])
    print(html)


if __name__ == '__main__':
    #teste
    test()
