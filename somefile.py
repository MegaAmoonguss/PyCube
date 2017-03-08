__all__ = ['somefile']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['add'])
@Js
def PyJsHoisted_add_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'a'])
    return (var.get('a')+var.get('b'))
PyJsHoisted_add_.func_name = 'add'
var.put('add', PyJsHoisted_add_)
pass
pass


# Add lib to the module scope
somefile = var.to_python()