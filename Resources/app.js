var root = {};
var mobiten = {};

Ti.include('library/redux.js');
includeRJSSGlobal('rjss/common.rjss');
includeRJSSGlobal('rjss/localize.rjss');

// Tell the compiler which modules we are going to use; note there are no () on these!
var used = [Ti.UI.createTabGroup, Ti.UI.createWindow, Ti.UI.createTab, Ti.UI.createLabel, Ti.Platform.locale];


Ti.include('js/base.js');
Ti.include('js/main.js');
