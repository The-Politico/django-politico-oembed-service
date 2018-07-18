![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# django-politico-oembed-service

### Quickstart

1. Install the app.

  ```
  $ pip install django-politico-oembed-service
  ```

2. Add the app to your Django project and configure settings.

  ```python
  INSTALLED_APPS = [
      # ...
      'rest_framework',
      'oembeder',
  ]

  #########################
  # oembeder settings

  OEMBEDSERVICE_API_AUTHENTICATION_CLASS = ''
  OEMBEDSERVICE_API_PERMISSION_CLASS = ''
  ```


### Using services

##### Twitter

```javascript
fetch('./your/api/endpoint/oembed/twitter', {
  method: 'POST',
  headers: {
    Authorization: `Token ${YOUR_APP_TOKEN_HERE}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    url: 'https://twitter.com/someuser/sometweeturl/'
  })
})
.then(response => response.json())
.then(data => {
  console.log(data);
});
```
