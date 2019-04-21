#!/bin/bash
# Usage Note: you need to bump the version, then commit before running the
#  script

# See https://github.com/pandas-dev/pandas/issues/18985
# TODO: automate the bumping of MAJOR/MINOR/BUGFIX?
MAJOR="0"
MINOR="3"
BUGFIX="1"

git commit --allow-empty -m 'RLS: v '$MAJOR.$MINOR.$BUGFIX
git tag -a v$MAJOR.$MINOR.$BUGFIX -m "Version "$MAJOR.$MINOR.$BUGFIX

rm -rf dist
python2 setup.py sdist
python3 setup.py sdist bdist_wheel

# Assumes pypi account is already set up with appropriate permissions/config
twine upload dist/*

# Assumes `git remote upstream` is already set up
git push
