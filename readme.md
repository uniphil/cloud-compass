
dependencies suck. compile sass in cloud.

for heroku the buildpack must be set to

```bash
heroku config:set BUILDPACK_URL=git@github.com:ddollar/heroku-buildpack-multi.git
```
