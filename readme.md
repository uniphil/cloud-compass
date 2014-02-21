
dependencies suck. compile sass in cloud.

for heroku the buildpack must be set to

```bash
heroku config:set BUILDPACK_URL=https://github.com/uniphil/heroku-buildpack-pythonsass.git
```

to get sass in on this
