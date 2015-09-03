# Zimuzu

[![Latest Version][1]][2]

A command line tool for doing the signing work for zimuzu(<http://www.zimuzu.tv/>).

## Install

    $ (sudo) pip install -U zimuzu

## Usage

Touch a new configuration json file named `zimuzu_config.json` under
`/usr/local/bin`:

    {
        "account": "Your username",
        "password": "Your password"
    }

do the sign:

    $ zimuzu sign

## Contribute

Contributions are always welcome! :sparkles:  :cake: :sparkles: Please file an
issue with detailed information if you run into problems. Feel free to send me
a pull request, I'll be happy to review and merge it!

## Details

### Login:

* url:  http://www.zimuzu.tv/User/Login/ajaxLogin
* method:  post
* post data:
    - account
    - password
    - remember: 0 no; 1 yes
    - url_back: http://www.zimuzu.tv/user/sign

* response(json):

        {
             "status":1,    # 1 means ok.
             "info":"\u767b\u5f55\u6210\u529f\uff01",
             "data":{"url_back":"http:\/\/www.zimuzu.tv\/user\/sign"}
        }


### Visit sign page

* url: http://www.zimuzu.tv/user/sign
* method: get

This step is essential, or you'll get 4002 status when you do the sign next.

### Do sign:

* url: http://www.zimuzu.tv/user/sign/dosign
* method: get
* response(json):

        {
             "status":1,    # 1 means ok.
             "info":"",
             "data":1    # 1 means you keep signing for 1 days.
        }

## License

MIT.


[1]: http://img.shields.io/pypi/v/zimuzu.svg
[2]: https://pypi.python.org/pypi/zimuzu