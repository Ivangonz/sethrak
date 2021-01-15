from invoke import Collection

from tasks import build

ns = Collection(build=build,)
