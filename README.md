# Tears 😭

Tears is a wrapper around git that reverts your changes when you didn't do what you said you would.

# Setup

Add `tears` to your `PATH`.

# Usage

```shell
# initialize a git repository
git init
# add the tears config to the git project
tears init
# tell tears what you are going to commit next
tears goal
# same as 'git status' with some extra tears info
tears status
# try to commit your code (maybe it will fail, and disappear like tears in rain)
git commit
```
