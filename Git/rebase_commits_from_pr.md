# Rebase Commits from Pull Request

People wouldn't like to see a wrong commit and a revert commit to undo changes of the wrong commit. This pollutes commit history.

Here is a simple way for removing the wrong commit instead of undoing changes with a revert commit:

```bash
$ git checkout my-pull-request-branch

# Rebase the last n commits interactively
# n is the number of commits to be rebased
# For example, if you want to rebase the last 3 commits, n = 3
$ git rebase -i HEAD~n

# The command above will open an editor with a list of commits
# Replace "pick" with "drop" for commits you want to discard.
# Then, save and close the editor.

# use force push with safer mode
$ git push --force-with-lease
```
