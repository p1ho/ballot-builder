# Ballot Builder

This is the group repository for SI-699 team project.
Scraping stuff [https://onyourballot.vote411.org/index.do]

# Synchronizing workflow

I played around with it a little bit, basically a flask app has a lot of dependencies that Pycharm will prepare for us, but those files should not be uploaded to Github because they could be machine dependent.

In other words, the only files on Github are files that all of us must have the same version of (like app.py), everything else should not be uploaded.
Pycharm doesn't seem to create a .gitignore for us, but it looks smart enough to know what files should be uploaded.

Because it is possible to check out from a repo directly at Pycharm's bootup screen, I think there are ways to include meta information about what kind of project this is on Github so Pycharm knows to immediately set up a Flask environment, but I'm not sure how at the moment.

The following is what has worked for me.

## steps to setting up the first time

1. open Pycharm, create a new flask project

1. once it sets up everything
    * go to VCS / Enable VCS Control Integration
    * Select Git
    * OK
    * (This is equivalent to "git init")
  
1. after successful initialization:
    * go to VCS / Git / Remotes
    * Fill in URL w/ this repo's URL
    * OK
    * (This is equivalent to "git add origin url-for-this-repo")
  
1. after adding remote:
    * remove app.py

1. after removing app.py (source of conflict):
    * go to VCS / Git / Pull
    * click refresh button next to Remote
    * Select origin/master in Branches to merge
    * (This is equivalent to "git pull")

1. Right now you should be synced with the GitHub Repo, I would suggest we create different branches for our work, otherwise if everyone's pushing to the master branch we would have to do a git pull (or git rebase) every time someone pushes new change to the branch. TBH I haven't done it before either, but I think doing things in branches then a single session merging conflicts is probably more efficient.