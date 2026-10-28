# hello-bohdana

A Python learning package for hands-on work with DevOps: the `hello_bohdana` module contains the `hello()` function, which returns a greeting string.
The package is built using the command `python -m build`, and you can install it from the local devpi repository as follows:

```bash
pip install -i http://localhost:3141/bohdana/dev/+simple/ hello-bohdana
```

The `linux/` folder contains the systemd unit `mytest.service`, and the `loadtest/` folder contains a test server and the molotov load test.