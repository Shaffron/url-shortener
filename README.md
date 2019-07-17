# compressor

Shorten URL Service

# Environments
## Python
3.7 +

## Redis
5.0.0 +

## Docker
```bash
# Docker Client
Client: Docker Engine - Community
 Version:           18.09.2
 API version:       1.39
 Go version:        go1.10.8
 Git commit:        6247962
 Built:             Sun Feb 10 04:12:31 2019
 OS/Arch:           windows/amd64
 Experimental:      false

# Docker Server
Server: Docker Engine - Community
 Engine:
  Version:          18.09.2
  API version:      1.39 (minimum version 1.12)
  Go version:       go1.10.6
  Git commit:       6247962
  Built:            Sun Feb 10 04:13:06 2019
  OS/Arch:          linux/amd64
  Experimental:     false

# Docker Compose
docker-compose version 1.23.2, build 1110ad01
```

## Browser
All of ES6+ (Javascript)  support browser


# Virtualenv
> Before you run application or test  
activate virtualenv first

```bash
python -m venv virtualenv

# Linux
source virtualenv/bin/activate
# Windows
source virtualenv/Scripts/activate

pip install -r requirements.txt
```

# Run
## Development Server
<code>docker & docker-compose required</code>
```bash
docker-compose up
```
After development server is up  
now we can explore shorten url service at <a href='http://localhost:5000'>http://localhost:5000</a>


## Test
One time test with code coverage
```bash
pytest --cov --cov-config .coveragerc
```

If you want test continuously, run below command
```bash
ptw
```


# License
MIT

Copyright (c) 2019-present, YoungJin Kim