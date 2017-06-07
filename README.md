# Wavefront API Client

The Wavefront API allows you to perform various operations in Wavefront. The API can be used to automate commonly executed operations such as tagging sources automatically, sending events, and more.

This Python package is automatically generated by the Swagger Codegen project.

- Wavefront API version: 2

If you're looking for the V1 API, the API client can be found in the api-v1 branch of this repository.

## Requirements

- Python 2.7 and higher
- OpenSSL 1.0 and higher

**Note**: As of April 2017 Macs ship with OpenSSL version 0.9.8. You may need to upgrade to 1.0 if you have not already. To upgrade using Homebrew, run:

```
brew upgrade openssl
```

## Setuptools
You can install the bindings via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install
```

Or you can install from Github via pip:

```sh
pip install git+https://github.com/wavefronthq/python-client.git
```

Or you can install from PyPi via pip:

```sh
pip install wavefront_client
```


To use the bindings, import the package:

```python
import wavefront_api_client
```

## Manual Installation
If you do not want to use Setuptools, you can download the latest release.
Then, to use the bindings, import the package:

```python
import path.to.wavefront_api_client
```

## Getting Started

All API endpoints are documented at https://YOUR_INSTANCE.wavefront.com/api-docs/ui/. Below is a simple example demonstrating how to use the library to call the Source API. You can use this example as a starting point.

```python
import wavefront_api_client as wave_api

base_url = 'https://YOUR_INSTANCE.wavefront.com'
api_key = 'YOUR_API_TOKEN'

client = wave_api.ApiClient(host=base_url, header_name='Authorization', header_value='Bearer ' + api_key)

# instantiate source API
source_api = wave_api.SourceApi(client)
sources = source_api.get_all_source()
print sources
```

## Troubleshooting

If you encounter a bug or need help, feel free to leave an [issue](https://github.com/wavefrontHQ/python-client/issues) on this GitHub repository, or contact us at [support@wavefront.com](support@wavefront.com).
