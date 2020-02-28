# FastDash

> There are countless ways to do one thing, I just choose the one that works for myself.

_**Note: Just a demo, no production, no guarantee.**_

`FastDash` is just `FastAPI` and `DashBoard`.
Obviously another host health dashboard, working with FastAPI.

## TODO

- [ ] API
  - [ ] More and more-fine-grained API.
  - [ ] Smaller and reasonable root API.
- [ ] UI
  - [ ] Basic display.
  - [ ] Beautiful charts.
- [ ] Others
  - [ ] Reasonable data storage.
  - [ ] Simple performance / availability analysis.

## Usage

You need to have Python & Pipenv.

```shell
git clone git@github.com:psiace/fastdash.git
pipenv install
# for developer, run `pipenv install --dev`
pipenv shell
uvicorn fastdash.main:app --reload
# or `pipenv run uvicorn fastdash.main:app --reload`
```

Now, you can see all infomation at `http://127.0.0.1:8000/api/fastdash`.

All routes are available on `/docs` or `/redoc` paths with Swagger or ReDoc.

## Contact

Chojan Shang - [@PsiACE](https://github.com/psiace) - <psiace@outlook.com>

Project Link: [https://github.com/psiace/fastdash](https://github.com/psiace/fastdash)

## License

This project is licensed under the terms of the [MIT license](./LICENSE).

## Credits

- [pyDash](https://gitlab.com/k3oni/pydash): A small web-based monitoring dashboard for your linux pc/server writen in Python and Django + Chart.js.
- [FastAPI](https://github.com/tiangolo/fastapi): A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- [FastAPI RealWorld](https://github.com/nsidnev/fastapi-realworld-example-app): Backend logic implementation for [RealWorld](https://github.com/gothinkster/realworld) with awesome FastAPI. I learned a lot, including the code.
