PyMailer
=======

A classic email sending library for Python.


## Description
PyMailer is a framework for seding email. This project is designed to be simple to code.


## Usage
### Simple Example
```python
from pymailar import PyMailer

# Set Gmail Account with address・password
mailer = PyMailer('your gmail address', 'your gmail application password')
# Set Gmail Account with Yaml
mailer = PyMailer(yaml_file='yaml file path')

# Send Email
mailer.send('to address', 'subject', 'body')
```

### Yaml Example
```yaml
address: your gmail address
pymailar: your gmail application password
```


## Installation
```sh
$ git clone https://github.com/AjxLab/PyMailer
$ cd PyMailer
```
