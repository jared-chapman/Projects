var assert = require('assert');
var tpo = require('/home/jared/wdio/trelloPageObject.js');
describe('The login page of Trello', function() {
	it('Shows an error message if credentials are not correct', function(){
		tpo.login('wrongUsername', 'wrongPassword');
		tpo.waitForError();
		assert.equal(tpo.errorExists(), true);
	});
});

