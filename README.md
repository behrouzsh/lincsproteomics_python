# lincsproteomics_python 
This repo is for python APIs used in lincsproteomics.org


### To run:


```
	$ virtualenv venv
	$ . venv/bin/activate
	$ pip install -r requirements.txt
	$ python app.py
```

### To run the docker:


```
	$ docker build -t lincsproteomics:1.0 .
	$ docker images
	$ docker run <imade_id>
	$ python app.py
```