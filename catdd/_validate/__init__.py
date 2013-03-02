import inspect
from pprint import pprint


class ValidateBase(object):
    __PARAMETER_VALIDATION__ = True

    def __init__(self, value, template=None):
        self.template = None
        frame_current = inspect.currentframe()
        frames_outer = inspect.getouterframes(frame_current)
        outer = frames_outer[1]
        source = outer[4][outer[5]]
        label = source.split('(', 1)[1]
        label = label.rsplit(')',  1)[0]
        self.label_argument = label
        self.validate(value)
        
    def validate(self, value):
        pass
    
    def is_of_instance(self, instance, types, named):
        text = ("Content '%s' by argument label '%s'"
                " of type '%s' exceeds restriction '%s'.")
        if not isinstance(instance, types):
            text = text % (instance, self.label_argument, 
                           type(instance).__name__, 
                           named)
            raise(ValueError(text))

class String(ValidateBase):
    def validate(self, value):
        self.is_of_instance(value, str, 'string')        
        
class Number(ValidateBase):
    def validate(self, value):
        self.is_of_instance(value, (int, float), 'number')
        
class Boolean(ValidateBase):
    def validate(self, value):
        self.is_of_instance(value, bool, 'boolean')
        
class Dictionary(ValidateBase):
    def validate(self, value):
        self.is_of_instance(value, dict, 'dictionary')
        
class Array(ValidateBase):
    def validate(self, value):
        self.is_of_instance(value, (list, tuple, set), 'array')


class Structure(ValidateBase):
    def validate(self, value):
        pass
    
if __name__ == '__main__':
    given = [1,2,3,4]
    template = {} 
    Structure(given, template)
        