test:
	py.test --cov app --cov-config .coveragerc --cov-report term-missing app
