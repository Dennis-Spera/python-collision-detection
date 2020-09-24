#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

'''

import traceback, re
import pprint, sqlite3
import display, setup, menu, dialogs, metrics, database, treeMethods, methods, error
import wx, printer

#=======================================================================================================================
classes = [setup.SetupEnvironment, display.Initialize, menu.MenuActions, metrics.metricDetails,  database.queryDatabase, \
           database.createObjects, treeMethods.treeOP, methods.treeMethods, display.iconMethods, error.errorClass ]

ora = None

class BaseClass(*classes):
    def __init__(self):
        self.instance = {}
        self.iTree = {}
        for className in classes:
            className.__init__(self)


    def _add(self, **kwargs):
        if kwargs['_name']  in self.iTree:
            print('attempt to add an existing instance variable : ' + _name)
            exit(1)
        else:
            try:
                if  kwargs['_type']:
                    pass
            except:
                kwargs['_type'] = None

            try:
                if kwargs['_readonly']:
                    pass
            except:
                kwargs['_readonly'] = None

            try:
                if kwargs['_default']:
                    pass
            except:
                kwargs['_default'] = None

            try:
                if  kwargs['_file_name']:
                    pass
            except:
                kwargs['_file_name'] = None

            try:
                if kwargs['_current_line_number']:
                    pass
            except:
                kwargs['_current_line_number'] = None

            try:
                if kwargs['_current_function_name']:
                    pass
            except:
                kwargs['_current_function_name'] = None

            self.instance = {'name':kwargs['_name'], 'type':kwargs['_type'], 'readonly':kwargs['_readonly'], 'default':kwargs['_default'],
                             'file_name':kwargs['_file_name'],'current_line_number':kwargs['_current_line_number'], 'current_function_name':kwargs['_current_function_name']}

            self.iTree[ kwargs['_name'] ] = self.instance

    def _set(self, _name, value):
        if _name in self.iTree:
            self.iTree[_name][_name] = value
        else:
            print('instance variable ' + _name + ' does not exist')
            self._exit()

    def _get(self, _name):
        if _name in self.iTree[_name]:
           return self.iTree[_name][_name]
        else:
           print('instance variable ' + _name + ' does not exist')
           self._exit()

    def _destroy(self, _name):
        if _name in self.iTree:
           del self.iTree[_name][_name]
        else:
           print('instance variable ' + _name + ' does not exist')
           self._exit()

    def _undef(self, _name):
        if _name in self.iTree:
           del self.iTree[_name][_name]
        else:
           print('instance variable ' + _name + ' does not exist')
           self._exit()

    def _dump (self):
        print("\n",'Dump of object')
        print('===============================================================')
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.iTree)
        print('===============================================================')

    def _exit(self):
        traceback.print_stack()
        print(repr(traceback.extract_stack()))
        print(repr(traceback.format_stack()))
        exit(1)

def new():
        d = {}
        for class_name in classes:
            list = dir(class_name)
            for method in list:
                regex = r"(^__(.*)__$)"
                if not re.search(regex, method):
                    if method not in d:
                        d[method] = None
                    else:
                        print('method collision ' + method + ' is defined')
                        exit(1)

        return BaseClass()
#=======================================================================================================================

class MainWindow(wx.Frame):
    def __init__(gui, *args, **kwds):
        wx.Frame.__init__(gui, *args, **kwds)

        obj = new()

        obj.defineConstants()
        obj.createSqliteObjects()
        logger = obj._get('logger')
        logger.info('success: createSqliteObjects()')

        obj.setupTerminal(gui)
        logger = obj._get('logger')
        logger.info('success: setupTerminal(gui)')

        obj._dump()

#-------------
#   M A I N
#-------------

class MyApp(wx.App):

    def OnInit(new):

        wx.InitAllImageHandlers()
        mw = MainWindow(None, -1, "main.py - proto+")
        new.SetTopWindow(mw)
        mw.Show()
        return 1

if __name__ == "__main__":

    app = MyApp(0)
    app.MainLoop()
