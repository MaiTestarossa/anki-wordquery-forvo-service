# anki-wordquery-forvo-service

1. Make sure your have installed anki plugin WordQuery https://ankiweb.net/shared/info/775418273
2. Get your api key form https://api.forvo.com/
3. download and open forvo.py with an editor(like Notepad)
4. Paste your api key in forvo.py line22
```python
	# add your forvo api here,more visit https://api.forvo.com/
	self.API = 'Paste API Here'
```
5. choose pronunciation's language,default is japanese(ja),all codes you can visit https://forvo.com/languages-codes/
```python
	# custuom language
	self.language = 'ja'
```
6. Copy forvo.py to Anki2\addons\wquery\service
7. Open Anki->Tools->WordQuery->Options window->choose forvo
