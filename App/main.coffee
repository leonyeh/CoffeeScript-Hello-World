Titanium.UI.setBackgroundColor('#000')

# windows
root.win1 = new mobiten.BaseWindow('1')
root.win2 = new mobiten.BaseWindow('2')


tabGroup = new TabGroup();

root.tab1 = new Tab( {id: 'Tab1', window: root.win1.win})
tabGroup.addTab(root.tab1);

root.tab2 = new Tab( {id: 'Tab2', window: root.win2.win})
tabGroup.addTab(root.tab2);



tabGroup.open({transition:Titanium.UI.iPhone.AnimationStyle.FLIP_FROM_LEFT})
tabGroup.setActiveTab(1)
