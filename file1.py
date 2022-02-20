

#git commands
git init
git clone
git fetch
git pull --rebase
git pull --merge
git push
git branch <branch-name>
git branch --delete <branch-name>
git branch -u origin/main ; to track the current branch to origin main branch
git switch <branch-name>
git switch -
git reset --HARD origin/master
git log
git tag v1.0
git tag -a v1.1 -m 'tag message, -a is verbose'
git tag -a v1.2 15027957951b64cf874c3557a0f3547bd83b3ff6
git reflog
git checkout sha1 <detached head> ;# used to go back to a commit and experiment and commit code and a branch created out of it and then that can be merged
git rebase -i HEAD~3 <pick sha1 squash sha1 squash sha1>
git cat-file d3e92575b7dd42c143e7c56aa71f968e6efbf3e0 -t
git cat-file d3e92575b7dd42c143e7c56aa71f968e6efbf3e0 -p

git checkout <file> ; will discard all the changes in the working area
git checkout . ; discards all the changes in all the files in working area
git reset --soft HEAD~1/sha1 <uncommit and changes in staging area and working tree>
git reset --mixed HEAD~1/sha1 <uncommit and changes only in working tree>
git reset --hard HEAD~1/sha1 <uncommit and changes cleaned up>
git revert HEAD~1/sha1 -m 'revert command' ; need to be followed by git push
# reset is always HEAD minus something.. we can not reset a particular commit
# revert can be any commit, since revert is a new commit added to the tree with sha1 commit changes removed


git work flow:
    git clone
    create a feature branch from the main branch
    start commits into the feature branch
    once feature completed, squash ur feature branch commits if needed 
    rebase ur main branch against origin/master
    rebase ur feature branch against ur main branch
    either push from the feature branch or 
    merge feature branch into main branch and push to origin/master
    
     
