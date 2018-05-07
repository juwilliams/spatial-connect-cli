import datetime

def replaceTokens(rawSource):
	# replace date tokens
	rawSource = replaceDateTokens(rawSource)

	return rawSource

def replaceDateTokens(rawSource):
	now = datetime.datetime.now()

	rawSource = rawSource.replace("[[YEAR]]", str(now.year)).replace("[[MONTH]]", str(now.month)).replace("[[DAY]]", str(now.day))

	return rawSource
