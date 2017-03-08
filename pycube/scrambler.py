__all__ = ['scrambler']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['flat2posit', 'size', 'posit', 'help', 'doslice', 'colorPerm', 'seq', 'colorString', 'scramblestring', 'cubeorient', 'appendmoves', 'imagestring', 'seqlen', 'setForm', 'numcub', 'colorList', 'scramble', 'mult', 'colors'])
@Js
def PyJsHoisted_appendmoves_(sq, axsl, tl, la, this, arguments, var=var):
    var = Scope({'sq':sq, 'axsl':axsl, 'tl':tl, 'la':la, 'this':this, 'arguments':arguments}, var)
    var.registers(['axsl', 'sl', 'tl', 'q', 'sq', 'sa', 'la', 'm'])
    #for JS loop
    var.put('sl', Js(0.0))
    while (var.get('sl')<var.get('tl')):
        try:
            if var.get('axsl').get(var.get('sl')):
                var.put('q', (var.get('axsl').get(var.get('sl'))-Js(1.0)))
                var.put('sa', var.get('la'))
                var.put('m', var.get('sl'))
                if (((var.get('sl')+var.get('sl'))+Js(1.0))>=var.get('tl')):
                    var.put('sa', Js(3.0), '+')
                    var.put('m', ((var.get('tl')-Js(1.0))-var.get('m')))
                    var.put('q', (Js(2.0)-var.get('q')))
                var.get('sq').put(var.get('sq').get('length'), ((((var.get('m')*Js(6.0))+var.get('sa'))*Js(4.0))+var.get('q')))
        finally:
                (var.put('sl',Js(var.get('sl').to_number())+Js(1))-Js(1))
PyJsHoisted_appendmoves_.func_name = 'appendmoves'
var.put('appendmoves', PyJsHoisted_appendmoves_)
@Js
def PyJsHoisted_scramble_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'axam', 'ax', 'sl', 'q', 'tl', 'axsl', 'la', 'moved'])
    var.put('tl', var.get('size'))
    if (var.get('mult') or ((var.get('size')&Js(1.0))!=Js(0.0))):
        (var.put('tl',Js(var.get('tl').to_number())-Js(1))+Js(1))
    var.put('axsl', var.get('Array').create(var.get('tl')))
    var.put('axam', var.get('Array').create(Js(0.0), Js(0.0), Js(0.0)))
    pass
    #for JS loop
    var.put('n', Js(0.0))
    while (var.get('n')<var.get('numcub')):
        try:
            var.put('la', (-Js(1.0)))
            var.get('seq').put(var.get('n'), var.get('Array').create())
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('tl')):
                try:
                    var.get('axsl').put(var.get('i'), Js(0.0))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.get('axam').put('0', var.get('axam').put('1', var.get('axam').put('2', Js(0.0))))
            var.put('moved', Js(0.0))
            while ((var.get('seq').get(var.get('n')).get('length')+var.get('moved'))<var.get('seqlen')):
                pass
                while 1:
                    while 1:
                        var.put('ax', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0))))
                        var.put('sl', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tl'))))
                        var.put('q', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0))))
                        if not ((var.get('ax')==var.get('la')) and (var.get('axsl').get(var.get('sl'))!=Js(0.0))):
                            break
                    def PyJs_LONG_0_(var=var):
                        return ((((var.get('ax')==var.get('la')) and var.get('mult').neg()) and (var.get('tl')==var.get('size'))) and (((((Js(2.0)*var.get('axam').get('0'))==var.get('tl')) or ((Js(2.0)*var.get('axam').get('1'))==var.get('tl'))) or ((Js(2.0)*var.get('axam').get('2'))==var.get('tl'))) or (((Js(2.0)*(var.get('axam').get(var.get('q'))+Js(1.0)))==var.get('tl')) and ((((var.get('axam').get('0')+var.get('axam').get('1'))+var.get('axam').get('2'))-var.get('axam').get(var.get('q')))>Js(0.0)))))
                    if not PyJs_LONG_0_():
                        break
                if (var.get('ax')!=var.get('la')):
                    var.get('appendmoves')(var.get('seq').get(var.get('n')), var.get('axsl'), var.get('tl'), var.get('la'))
                    #for JS loop
                    var.put('i', Js(0.0))
                    while (var.get('i')<var.get('tl')):
                        try:
                            var.get('axsl').put(var.get('i'), Js(0.0))
                        finally:
                                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                    var.get('axam').put('0', var.get('axam').put('1', var.get('axam').put('2', Js(0.0))))
                    var.put('moved', Js(0.0))
                    var.put('la', var.get('ax'))
                (var.get('axam').put(var.get('q'),Js(var.get('axam').get(var.get('q')).to_number())+Js(1))-Js(1))
                (var.put('moved',Js(var.get('moved').to_number())+Js(1))-Js(1))
                var.get('axsl').put(var.get('sl'), (var.get('q')+Js(1.0)))
            var.get('appendmoves')(var.get('seq').get(var.get('n')), var.get('axsl'), var.get('tl'), var.get('la'))
            var.get('seq').get(var.get('n')).put(var.get('seq').get(var.get('n')).get('length'), (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(24.0))) if var.get('cubeorient') else Js(0.0)))
        finally:
                (var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1))
    var.put('flat2posit', var.get('Array').create(((Js(12.0)*var.get('size'))*var.get('size'))))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('flat2posit').get('length')):
        try:
            var.get('flat2posit').put(var.get('i'), (-Js(1.0)))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('size')):
        try:
            #for JS loop
            var.put('j', Js(0.0))
            while (var.get('j')<var.get('size')):
                try:
                    var.get('flat2posit').put(((((Js(4.0)*var.get('size'))*(((Js(3.0)*var.get('size'))-var.get('i'))-Js(1.0)))+var.get('size'))+var.get('j')), ((var.get('i')*var.get('size'))+var.get('j')))
                    var.get('flat2posit').put((((((Js(4.0)*var.get('size'))*(var.get('size')+var.get('i')))+var.get('size'))-var.get('j'))-Js(1.0)), (((var.get('size')+var.get('i'))*var.get('size'))+var.get('j')))
                    var.get('flat2posit').put((((((Js(4.0)*var.get('size'))*(var.get('size')+var.get('i')))+(Js(4.0)*var.get('size')))-var.get('j'))-Js(1.0)), ((((Js(2.0)*var.get('size'))+var.get('i'))*var.get('size'))+var.get('j')))
                    var.get('flat2posit').put(((((Js(4.0)*var.get('size'))*var.get('i'))+var.get('size'))+var.get('j')), ((((Js(3.0)*var.get('size'))+var.get('i'))*var.get('size'))+var.get('j')))
                    var.get('flat2posit').put(((((Js(4.0)*var.get('size'))*(var.get('size')+var.get('i')))+(Js(2.0)*var.get('size')))+var.get('j')), ((((Js(4.0)*var.get('size'))+var.get('i'))*var.get('size'))+var.get('j')))
                    var.get('flat2posit').put(((((Js(4.0)*var.get('size'))*(var.get('size')+var.get('i')))+var.get('size'))+var.get('j')), ((((Js(5.0)*var.get('size'))+var.get('i'))*var.get('size'))+var.get('j')))
                finally:
                        (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
PyJsHoisted_scramble_.func_name = 'scramble'
var.put('scramble', PyJsHoisted_scramble_)
@Js
def PyJsHoisted_scramblestring_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['s', 'j', 'ori', 'n', 'i', 'k'])
    var.put('s', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('seq').get(var.get('n')).get('length')-Js(1.0))):
        try:
            if (var.get('i')!=Js(0.0)):
                var.put('s', Js(' '), '+')
            var.put('k', (var.get('seq').get(var.get('n')).get(var.get('i'))>>Js(2.0)))
            var.put('j', (var.get('k')%Js(6.0)))
            var.put('k', ((var.get('k')-var.get('j'))/Js(6.0)))
            if ((var.get('k') and (var.get('size')<=Js(5.0))) and var.get('mult').neg()):
                var.put('s', Js('dlburf').callprop('charAt', var.get('j')), '+')
            else:
                if ((var.get('size')<=Js(5.0)) and var.get('mult')):
                    var.put('s', Js('DLBURF').callprop('charAt', var.get('j')), '+')
                    if var.get('k'):
                        var.put('s', Js('w'), '+')
                else:
                    if var.get('k'):
                        var.put('s', (var.get('k')+Js(1.0)), '+')
                    var.put('s', Js('DLBURF').callprop('charAt', var.get('j')), '+')
            var.put('j', (var.get('seq').get(var.get('n')).get(var.get('i'))&Js(3.0)))
            if (var.get('j')!=Js(0.0)):
                var.put('s', Js(" 2'").callprop('charAt', var.get('j')), '+')
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    if var.get('cubeorient'):
        var.put('ori', var.get('seq').get(var.get('n')).get((var.get('seq').get(var.get('n')).get('length')-Js(1.0))))
        var.put('s', (((((Js('Top:')+var.get('colorList').get((Js(2.0)+var.get('colors').get(var.get('colorPerm').get(var.get('ori')).get('3')))))+Js('&nbsp;&nbsp;&nbsp;Front:'))+var.get('colorList').get((Js(2.0)+var.get('colors').get(var.get('colorPerm').get(var.get('ori')).get('5')))))+Js('<br>'))+var.get('s')))
    return var.get('s')
PyJsHoisted_scramblestring_.func_name = 'scramblestring'
var.put('scramblestring', PyJsHoisted_scramblestring_)
@Js
def PyJsHoisted_imagestring_(nr, this, arguments, var=var):
    var = Scope({'nr':nr, 'this':this, 'arguments':arguments}, var)
    var.registers(['d', 'f', 's', 'nr', 'c', 'stickerheight', 'imageheight', 'ori', 'q', 'i', 'k'])
    #for JS loop
    var.put('k', Js(0.0))
    while (var.get('k')<Js(6.0)):
        try:
            var.get('colors').put(var.get('k'), (var.get('colorList').get('length')-Js(3.0)))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('colorList').get('length')):
                try:
                    if (var.get('colorString').callprop('charAt', var.get('k'))==var.get('colorList').get(var.get('i'))):
                        var.get('colors').put(var.get('k'), var.get('i'))
                        break
                finally:
                        var.put('i', Js(3.0), '+')
        finally:
                (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
    var.put('s', Js(''))
    var.put('d', Js(0.0))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(6.0)):
        try:
            #for JS loop
            var.put('f', Js(0.0))
            while (var.get('f')<(var.get('size')*var.get('size'))):
                try:
                    var.get('posit').put((var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1)), var.get('i'))
                finally:
                        (var.put('f',Js(var.get('f').to_number())+Js(1))-Js(1))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('seq').get(var.get('nr')).get('length')-Js(1.0))):
        try:
            var.put('q', (var.get('seq').get(var.get('nr')).get(var.get('i'))&Js(3.0)))
            var.put('f', (var.get('seq').get(var.get('nr')).get(var.get('i'))>>Js(2.0)))
            var.put('d', Js(0.0))
            while (var.get('f')>Js(5.0)):
                var.put('f', Js(6.0), '-')
                (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
            while 1:
                var.get('doslice')(var.get('f'), var.get('d'), (var.get('q')+Js(1.0)))
                (var.put('d',Js(var.get('d').to_number())-Js(1))+Js(1))
                if not (var.get('mult') and (var.get('d')>=Js(0.0))):
                    break
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('ori', var.get('seq').get(var.get('nr')).get((var.get('seq').get(var.get('nr')).get('length')-Js(1.0))))
    var.put('d', Js(0.0))
    var.put('imageheight', Js(160.0))
    var.put('stickerheight', var.get('Math').callprop('floor', (var.get('imageheight')/(var.get('size')*Js(3.0)))))
    if (var.get('stickerheight')<Js(5.0)):
        var.put('stickerheight', Js(5.0))
    var.put('s', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(Js(3.0)*var.get('size'))):
        try:
            #for JS loop
            var.put('f', Js(0.0))
            while (var.get('f')<(Js(4.0)*var.get('size'))):
                try:
                    if (var.get('flat2posit').get(var.get('d'))<Js(0.0)):
                        var.put('s', Js('empty '), '+')
                    else:
                        var.put('c', var.get('colorPerm').get(var.get('ori')).get(var.get('posit').get(var.get('flat2posit').get(var.get('d')))))
                        var.put('s', (var.get('colorList').get((var.get('colors').get(var.get('c'))+Js(1.0)))+Js(' ')), '+')
                    (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
                finally:
                        (var.put('f',Js(var.get('f').to_number())+Js(1))-Js(1))
            var.put('s', Js('newline '), '+')
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('s')
PyJsHoisted_imagestring_.func_name = 'imagestring'
var.put('imagestring', PyJsHoisted_imagestring_)
@Js
def PyJsHoisted_doslice_(f, d, q, this, arguments, var=var):
    var = Scope({'f':f, 'd':d, 'q':q, 'this':this, 'arguments':arguments}, var)
    var.registers(['s2', 'f3', 'f', 'd', 'f1', 'f4', 'c', 'j', 'f2', 'q', 'i', 'k'])
    pass
    var.put('s2', (var.get('size')*var.get('size')))
    pass
    if (var.get('f')>Js(5.0)):
        var.put('f', Js(6.0), '-')
    #for JS loop
    var.put('k', Js(0.0))
    while (var.get('k')<var.get('q')):
        try:
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('size')):
                try:
                    if (var.get('f')==Js(0.0)):
                        var.put('f1', ((((Js(6.0)*var.get('s2'))-(var.get('size')*var.get('d')))-var.get('size'))+var.get('i')))
                        var.put('f2', ((((Js(2.0)*var.get('s2'))-(var.get('size')*var.get('d')))-Js(1.0))-var.get('i')))
                        var.put('f3', ((((Js(3.0)*var.get('s2'))-(var.get('size')*var.get('d')))-Js(1.0))-var.get('i')))
                        var.put('f4', ((((Js(5.0)*var.get('s2'))-(var.get('size')*var.get('d')))-var.get('size'))+var.get('i')))
                    else:
                        if (var.get('f')==Js(1.0)):
                            var.put('f1', (((Js(3.0)*var.get('s2'))+var.get('d'))+(var.get('size')*var.get('i'))))
                            var.put('f2', (((Js(3.0)*var.get('s2'))+var.get('d'))-(var.get('size')*(var.get('i')+Js(1.0)))))
                            var.put('f3', ((var.get('s2')+var.get('d'))-(var.get('size')*(var.get('i')+Js(1.0)))))
                            var.put('f4', (((Js(5.0)*var.get('s2'))+var.get('d'))+(var.get('size')*var.get('i'))))
                        else:
                            if (var.get('f')==Js(2.0)):
                                var.put('f1', (((Js(3.0)*var.get('s2'))+(var.get('d')*var.get('size')))+var.get('i')))
                                var.put('f2', (((((Js(4.0)*var.get('s2'))+var.get('size'))-Js(1.0))-var.get('d'))+(var.get('size')*var.get('i'))))
                                var.put('f3', ((((var.get('d')*var.get('size'))+var.get('size'))-Js(1.0))-var.get('i')))
                                var.put('f4', ((((Js(2.0)*var.get('s2'))-Js(1.0))-var.get('d'))-(var.get('size')*var.get('i'))))
                            else:
                                if (var.get('f')==Js(3.0)):
                                    var.put('f1', (((((Js(4.0)*var.get('s2'))+(var.get('d')*var.get('size')))+var.get('size'))-Js(1.0))-var.get('i')))
                                    var.put('f2', (((Js(2.0)*var.get('s2'))+(var.get('d')*var.get('size')))+var.get('i')))
                                    var.put('f3', ((var.get('s2')+(var.get('d')*var.get('size')))+var.get('i')))
                                    var.put('f4', (((((Js(5.0)*var.get('s2'))+(var.get('d')*var.get('size')))+var.get('size'))-Js(1.0))-var.get('i')))
                                else:
                                    if (var.get('f')==Js(4.0)):
                                        var.put('f1', ((((Js(6.0)*var.get('s2'))-Js(1.0))-var.get('d'))-(var.get('size')*var.get('i'))))
                                        var.put('f2', (((var.get('size')-Js(1.0))-var.get('d'))+(var.get('size')*var.get('i'))))
                                        var.put('f3', (((((Js(2.0)*var.get('s2'))+var.get('size'))-Js(1.0))-var.get('d'))+(var.get('size')*var.get('i'))))
                                        var.put('f4', ((((Js(4.0)*var.get('s2'))-Js(1.0))-var.get('d'))-(var.get('size')*var.get('i'))))
                                    else:
                                        if (var.get('f')==Js(5.0)):
                                            var.put('f1', ((((Js(4.0)*var.get('s2'))-var.get('size'))-(var.get('d')*var.get('size')))+var.get('i')))
                                            var.put('f2', ((((Js(2.0)*var.get('s2'))-var.get('size'))+var.get('d'))-(var.get('size')*var.get('i'))))
                                            var.put('f3', (((var.get('s2')-Js(1.0))-(var.get('d')*var.get('size')))-var.get('i')))
                                            var.put('f4', (((Js(4.0)*var.get('s2'))+var.get('d'))+(var.get('size')*var.get('i'))))
                    var.put('c', var.get('posit').get(var.get('f1')))
                    var.get('posit').put(var.get('f1'), var.get('posit').get(var.get('f2')))
                    var.get('posit').put(var.get('f2'), var.get('posit').get(var.get('f3')))
                    var.get('posit').put(var.get('f3'), var.get('posit').get(var.get('f4')))
                    var.get('posit').put(var.get('f4'), var.get('c'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            if (var.get('d')==Js(0.0)):
                #for JS loop
                var.put('i', Js(0.0))
                while ((var.get('i')+var.get('i'))<var.get('size')):
                    try:
                        #for JS loop
                        var.put('j', Js(0.0))
                        while ((var.get('j')+var.get('j'))<(var.get('size')-Js(1.0))):
                            try:
                                var.put('f1', (((var.get('f')*var.get('s2'))+var.get('i'))+(var.get('j')*var.get('size'))))
                                var.put('f3', (((var.get('f')*var.get('s2'))+((var.get('size')-Js(1.0))-var.get('i')))+(((var.get('size')-Js(1.0))-var.get('j'))*var.get('size'))))
                                if (var.get('f')<Js(3.0)):
                                    var.put('f2', (((var.get('f')*var.get('s2'))+((var.get('size')-Js(1.0))-var.get('j')))+(var.get('i')*var.get('size'))))
                                    var.put('f4', (((var.get('f')*var.get('s2'))+var.get('j'))+(((var.get('size')-Js(1.0))-var.get('i'))*var.get('size'))))
                                else:
                                    var.put('f4', (((var.get('f')*var.get('s2'))+((var.get('size')-Js(1.0))-var.get('j')))+(var.get('i')*var.get('size'))))
                                    var.put('f2', (((var.get('f')*var.get('s2'))+var.get('j'))+(((var.get('size')-Js(1.0))-var.get('i'))*var.get('size'))))
                                var.put('c', var.get('posit').get(var.get('f1')))
                                var.get('posit').put(var.get('f1'), var.get('posit').get(var.get('f2')))
                                var.get('posit').put(var.get('f2'), var.get('posit').get(var.get('f3')))
                                var.get('posit').put(var.get('f3'), var.get('posit').get(var.get('f4')))
                                var.get('posit').put(var.get('f4'), var.get('c'))
                            finally:
                                    (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        finally:
                (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
PyJsHoisted_doslice_.func_name = 'doslice'
var.put('doslice', PyJsHoisted_doslice_)
@Js
def PyJsHoisted_help_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    def PyJs_LONG_5_(var=var):
        def PyJs_LONG_4_(var=var):
            def PyJs_LONG_3_(var=var):
                def PyJs_LONG_2_(var=var):
                    def PyJs_LONG_1_(var=var):
                        return ((((((Js('Cube Scrambler\n\n')+Js('This cube scrambler can scramble a cube of any size.\n'))+Js('Enter the cube size, the number of scrambles you want,\n'))+Js('and the length of each scramble (in htm). If you then\n'))+Js('press the Scramble button the page will reload and show\n'))+Js('the new scrambles. Every time you then reload the page\n'))+Js('or click the button, a new set of scrambles is generated.\n'))
                    return (((((((PyJs_LONG_1_()+Js('\nFurther options:\n'))+Js('Colours: The colour scheme to use in the previews. It\n'))+Js('consists of 6 letters, the first letter of the colours\n'))+Js('to use on the faces in DLBURF order. Allowed colours are\n'))+Js('yellow, blue, red, white, green, orange, purple.\n'))+Js('Multi-slice: If clear, an inner slice move is just a\n'))+Js('single slice. If checked, an inner slice move means a\n'))
                return (((((((((PyJs_LONG_2_()+Js('turn of the inner slice and all slices lying further\n'))+Js('outwards as a single unit.\n'))+Js('Cube Orient: If chosen, a random cube orientation is\n'))+Js('chosen for each scramble.\n'))+Js('\nScrambles:\n'))+Js('The scrambles will not contain any moves that cancel\n'))+Js('each other, nor moves that simplify to a cube rotation.\n'))+Js('\nNotation:\n'))+Js('Standard FLUBRD notation is used for the 2x2x2 and\n'))
            return (((((((PyJs_LONG_3_()+Js('3x3x3 cubes. With 4x4x4 and 5x5x5 cubes this is extended\n'))+Js('with lower case letters flubrd indicating a turn of an\n'))+Js('inner slice only, or in multi-slice mode the face letter\n'))+Js("is followed by a w to indicate a 'wide' move. For even\n"))+Js('larger cubes, inner slices are denoted by \n'))+Js('notation.\n'))+Js('Tip: On a 2x2x2 cube normally all 6 faces can be turned,\n'))
        return (((((((PyJs_LONG_4_()+Js('but if Multi-Slice is on, only the RFU faces are used.\n'))+Js('\nPrinting:\n'))+Js('The cube layout might not print correctly on a colour\n'))+Js('printer. Make sure that your browser is set up to print\n'))+Js('background colours, which is an Internet Options/Advanced\n'))+Js('setting in Internet Explorer, or a setting in the Print\n'))+Js('dialog in Mozilla Firefox.\n'))
    var.get('alert')((PyJs_LONG_5_()+Js('\nWritten by Jaap Scherphuis, Copyright 2004-2008.')))
PyJsHoisted_help_.func_name = 'help'
var.put('help', PyJsHoisted_help_)
@Js
def PyJsHoisted_setForm_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get('document').get('frm').get('size').put('value', var.get('size'))
    var.get('document').get('frm').get('len').put('value', var.get('seqlen'))
    var.get('document').get('frm').get('num').put('value', var.get('numcub'))
    var.get('document').get('frm').get('multi').put('checked', var.get('mult'))
    var.get('document').get('frm').get('cubori').put('checked', var.get('cubeorient'))
    var.get('document').get('frm').get('col').put('value', var.get('colorString'))
    var.get('document').get('frm').get('subbutton').callprop('focus')
PyJsHoisted_setForm_.func_name = 'setForm'
var.put('setForm', PyJsHoisted_setForm_)
var.put('size', Js(3.0))
var.put('seqlen', Js(30.0))
var.put('numcub', Js(1.0))
var.put('mult', Js(False))
var.put('cubeorient', Js(False))
var.put('colorString', Js('yobwrg'))
var.put('colorList', var.get('Array').create(Js('y'), Js('yellow.jpg'), Js('yellow'), Js('b'), Js('blue.jpg'), Js('blue'), Js('r'), Js('red.jpg'), Js('red'), Js('w'), Js('white.jpg'), Js('white'), Js('g'), Js('green.jpg'), Js('green'), Js('o'), Js('orange.jpg'), Js('orange'), Js('p'), Js('purple.jpg'), Js('purple'), Js('0'), Js('grey.jpg'), Js('grey')))
var.put('colors', var.get('Array').create())
var.put('seq', var.get('Array').create())
var.put('posit', var.get('Array').create())
pass
var.put('colorPerm', var.get('Array').create())
var.get('colorPerm').put('0', var.get('Array').create(Js(0.0), Js(1.0), Js(2.0), Js(3.0), Js(4.0), Js(5.0)))
var.get('colorPerm').put('1', var.get('Array').create(Js(0.0), Js(2.0), Js(4.0), Js(3.0), Js(5.0), Js(1.0)))
var.get('colorPerm').put('2', var.get('Array').create(Js(0.0), Js(4.0), Js(5.0), Js(3.0), Js(1.0), Js(2.0)))
var.get('colorPerm').put('3', var.get('Array').create(Js(0.0), Js(5.0), Js(1.0), Js(3.0), Js(2.0), Js(4.0)))
var.get('colorPerm').put('4', var.get('Array').create(Js(1.0), Js(0.0), Js(5.0), Js(4.0), Js(3.0), Js(2.0)))
var.get('colorPerm').put('5', var.get('Array').create(Js(1.0), Js(2.0), Js(0.0), Js(4.0), Js(5.0), Js(3.0)))
var.get('colorPerm').put('6', var.get('Array').create(Js(1.0), Js(3.0), Js(2.0), Js(4.0), Js(0.0), Js(5.0)))
var.get('colorPerm').put('7', var.get('Array').create(Js(1.0), Js(5.0), Js(3.0), Js(4.0), Js(2.0), Js(0.0)))
var.get('colorPerm').put('8', var.get('Array').create(Js(2.0), Js(0.0), Js(1.0), Js(5.0), Js(3.0), Js(4.0)))
var.get('colorPerm').put('9', var.get('Array').create(Js(2.0), Js(1.0), Js(3.0), Js(5.0), Js(4.0), Js(0.0)))
var.get('colorPerm').put('10', var.get('Array').create(Js(2.0), Js(3.0), Js(4.0), Js(5.0), Js(0.0), Js(1.0)))
var.get('colorPerm').put('11', var.get('Array').create(Js(2.0), Js(4.0), Js(0.0), Js(5.0), Js(1.0), Js(3.0)))
var.get('colorPerm').put('12', var.get('Array').create(Js(3.0), Js(1.0), Js(5.0), Js(0.0), Js(4.0), Js(2.0)))
var.get('colorPerm').put('13', var.get('Array').create(Js(3.0), Js(2.0), Js(1.0), Js(0.0), Js(5.0), Js(4.0)))
var.get('colorPerm').put('14', var.get('Array').create(Js(3.0), Js(4.0), Js(2.0), Js(0.0), Js(1.0), Js(5.0)))
var.get('colorPerm').put('15', var.get('Array').create(Js(3.0), Js(5.0), Js(4.0), Js(0.0), Js(2.0), Js(1.0)))
var.get('colorPerm').put('16', var.get('Array').create(Js(4.0), Js(0.0), Js(2.0), Js(1.0), Js(3.0), Js(5.0)))
var.get('colorPerm').put('17', var.get('Array').create(Js(4.0), Js(2.0), Js(3.0), Js(1.0), Js(5.0), Js(0.0)))
var.get('colorPerm').put('18', var.get('Array').create(Js(4.0), Js(3.0), Js(5.0), Js(1.0), Js(0.0), Js(2.0)))
var.get('colorPerm').put('19', var.get('Array').create(Js(4.0), Js(5.0), Js(0.0), Js(1.0), Js(2.0), Js(3.0)))
var.get('colorPerm').put('20', var.get('Array').create(Js(5.0), Js(0.0), Js(4.0), Js(2.0), Js(3.0), Js(1.0)))
var.get('colorPerm').put('21', var.get('Array').create(Js(5.0), Js(1.0), Js(0.0), Js(2.0), Js(4.0), Js(3.0)))
var.get('colorPerm').put('22', var.get('Array').create(Js(5.0), Js(3.0), Js(1.0), Js(2.0), Js(0.0), Js(4.0)))
var.get('colorPerm').put('23', var.get('Array').create(Js(5.0), Js(4.0), Js(3.0), Js(2.0), Js(1.0), Js(0.0)))
pass
pass
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
scrambler = var.to_python()