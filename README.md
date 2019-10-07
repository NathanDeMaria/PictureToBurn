<img src="https://upload.wikimedia.org/wikipedia/en/thumb/e/e5/Taylor_Swift_-_Picture_to_Burn.png/220px-Taylor_Swift_-_Picture_to_Burn.png" align=right width=30%></img>
# PictureToBurn

A python package for gif-making.

## Setup and Installation
### Set up Twitter creds
* Generate access token. Full instructions at https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens
* Copy `twitter_creds.dist.json` to `twitter_creds.json`
* Add token details to `twitter_creds.json`

### Install
```
python setup.py install
```

## Running
```
create_gif [local_file | twitter_url]
```