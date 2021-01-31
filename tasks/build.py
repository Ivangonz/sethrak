

from invoke import task


@task
def run(c):
    c.run('python -m sethrak')


@task
def test(c):
    c.run('py.test -s --cov-report term-missing --cov-config tests/.coveragerc --cov sethrak tests/')


@task
def tox(c):
    c.run('tox')


@task
def lock_proj(c):
    c.run('poetry lock -n')


@task
def lint(c):
    """Sorts, cleans, and formats current code."""
    commands = [
        (
            'Sort imports',
            'isort -j2 .',
        ),
        (
            'Remove unused',
            'autoflake -r --remove-all-unused-imports  --ignore-init-module-imports --remove-unused-variables --exclude scratch.py -i sethrak tasks tests',
        ), (
            'Fix python format',
            'yapf -r -i -p sethrak tests',
        ), (
            'Analyze runtime errors',
            'pyflakes sethrak/',
        ),
        (
            'Check for misspellings',
            'codespell -q3 --skip=".git,.idea,*.pyc,*.pyo,.mypy*,poetry.lock,build,dist" -I .dictionary sethrak',
        )
    ]

    for name, cmd in commands:
        print(' -- ', name)
        c.run(cmd)


@task
def req(c):
    c.run('poetry export -f requirements.txt --without-hashes > requirements.txt')


@task(post=(req,))
def clean(c):
    folders = [
        '.pytest_cache',
        '.tox',
        'build',
        'dist',
        'sethrak.egg-info',
    ]

    files = [
        'requirements.txt',
        '.coverage',
    ]

    for file in files + folders:
        c.run(f'rm -rf {file}')

