var assert = require('assert');
var tpo = require('/home/jared/wdio/trelloPageObject.js');
describe('The login page of Trello', function() {
	it('Logs in if credentials are correct', function(){
		tpo.login('jared.chapman.0613@gmail.com', 'amidoingthisright?');
		tpo.waitForInitials();
		assert.equal(tpo.initialsExist(), true);
	});
});

