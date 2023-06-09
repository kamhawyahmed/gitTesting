main

#yoyo simulatenous change


# init:
# create repo on github
# connect project by url
# commit master branch and push to hub

# checkout:
# navigate to branch

# branching:
# Theory:
#   New feature new branch / new person new branch

# Application:
# forking(multi-user branch): - use own branch of own fork pls
# forking from github page itself
# own copy of codebase under your name/in your repo stash
# ===> THEN create branch under your fork (copy)
# ====> THEN make changes + commit and push to branch of own fork
# ======> THEN make pull request

# ?When working in fork can have fork as origin and original as upstream by adding git url's in - git - repository - view remotes

# PULL REQUEST: Ask original owner to add commit from branch of forked version to branch of original version (usually master)
# Requester: compare and pull request => create pull request
# Owner: pull requests => review changes => add comments/approve/deny and request changes
# => changes (new commits) added auto to pull request
# ----ensure correct source branch being requested to be pulled into correct target branch
# PR Merging:
# Traditional merge - (off of pull request) - adds 2 commits - PR commit under editor name + merge commit under reviewer name
# Squash and merge: BETTER FOR PRS - removes 2nd commit so reviewing user does not get credit for editor code # will not show branching in intelliJ but thats better that way


# Update Branch:
# add remote changes to local

# STASHING: w the stash oh yeah
# stores uncommitted changes in THE stash (temp holding folder)
# can now checkout other branches and edit freely
# can then return to branch and unstash to return to working with working directory
# BUT gets messy if returned to branch, made MORE changes THEN try to unstash
# ^^^^ DONT DO THAT pls

# DELETING BRANCH:
# make sure not in (checked out in) branch
# make sure working dir changes all accounted for (applied to correct branches / stashed (but idk if can access stash if stash for deleted branch))
# then delete local and remote versions

# CHANGING COMMIT MESSAGE:
# has to be pushed too

#REBASE - keeps feature branches up to date w CLEAN git history:
# okay so had to revert but anyways
# rebase means put changes onto new base (newer version)
# feature 3 rebase commit - can ignore feature 1 and 2 rebase tests (mistakes while rebasing i.e. committing to wrong branch)


# Scenario: made change to feature branch but want to incorporate master changes
# Recognize head (?)
# 1: Merge master changes into feature (can preview before merge)
# 2: Do new commit (for local changes)
# 3: Push local and master commits to remote feature branch
#=> can PR with no conflicts => squash and merge to avoid ownership attribution difficulties

# Scenario: Above not followed/ want to merge feature by overwriting master
# will prompt to:
# manually resolve conflicts to confirm desired changes when PR'ing/merging

# Tags - marks certain node/version of project with certain name i.e. release-v1.0 --> accessible in future
#===> can then create release from tag in github -> makes zip of file structure (project) - saved checkpoint


# colors files: red un-versioned blue uncommitted (for current branch - current location (local/remote))
# colors code lines: blue - edited, green = new
# colors are cool - this is simultaneous change 2 - looks branched bc had to resolve conflicts when merging into master rather than merging master into feature, editing in ide then pushing (lol kinda fuzzy)
# (can assess changes during commit and push by clicking on file changed)
