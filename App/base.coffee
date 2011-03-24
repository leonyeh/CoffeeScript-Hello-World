class BaseWindow
	constructor: (winID) ->

		@win = new Window({id: 'Window'+winID})
		
		label = new Label({id: 'Label'+winID, className: 'big_text red_text' })
		@win.add(label)

mobiten.BaseWindow = BaseWindow
