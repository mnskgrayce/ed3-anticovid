# Engineering Design 3

## Project Structure

The project has three branches (not including master), each corresponding to a folder of the same name:

- **user-interface** (Trang, Han)
- **hardware-sensor** (Duc, Uyen)
- **vision** (Thien, Joseph, Che Jui, Duc)

## Get Started

Clone this repository onto your local machine then perform the following steps:

1. Create a local branch that track your team's remote branch with `git checkout --track origin/branch_name`
2. Create a folder with the same name as the branch to contain your subteam's code
3. Put your code inside this folder and push to your subteam's branch

## To run code, please use Windows to run the code 

- Download and install node: https://nodejs.org/en/download/
- Run the command in this link: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
- Install python: https://www.python.org/downloads/
- Install pip : https://www.geeksforgeeks.org/how-to-install-pip-on-windows/#:~:text=Download%20and%20Install%20pip%3A&text=Download%20the%20get%2Dpip.py,where%20the%20above%20file%20exists.&text=and%20wait%20through%20the%20installation,now%20installed%20on%20your%20system. 
- Clone the github

- For running website and camera panel, do the instruction below :
- ** Notes: Use powershell to run the command below 
- Run `pip install -r requirements.txt`
- Run `cd user-interface`
- Run `npm install` to reinstall missing packages, then run `npm run boot` to boot up the web application
- Right click anywhere then choose "Inspect" to open the Developer Tools panel
- You can view the live update logs in the "Console" tab

- For running on raspberry pi. 


## Git Workflow

All commands are run from the Terminal inside the project (subteam's) folder. If your current IDE supports Git, consider using the graphic interface tools for simplicity. If you use VS Code, see the Source Control (left) and branch manager (bottom left) tabs.

Keep an eye on the number of pending commits (both from and to your local machine) and always try to merge the latest updates from remote before you commit local changes.

- Update remote changes to your branch with `git fetch origin branch_name`
- View the code at the remote branch with `git checkout origin/branch_name`
- Check the code to see if it's safe to merge with your local branch
- Return to your local branch with `git checkout branch_name`
- Merge changes from a remote branch to your current branch with `git merge origin/branch_name`
- Modify your code, the run `git add .` to stage all changes **inside your current folder**
- Run `git -m "commit_message"` to make a local commit
- Push changes from your current branch to the remote branch with `git push -u origin branch_name`

**Create a pull request (PR) to merge your branch to the master branch!**

## Handy Commands

- Check which branch are you on: `git status`
- Switch to another branch: `git checkout branch_name`
- View commit history of current branch: `git log` (escape by typing "q")
- Set your current local branch to track a remote branch: `git branch -u origin/branch_name`
- Rename a branch: `git branch -m <oldname> <newname>`

## Tutorials (to be updated)

- Remote branches: https://devconnected.com/how-to-set-upstream-branch-on-git/
- Renaming branches: https://stackoverflow.com/questions/6591213/how-do-i-rename-a-local-git-branch

## Notes

- Add the files and folders you don't want to share with the team (node_modules, configurations etc.) to the `.gitignore` file
- When you push your code to the team repository, the ignored files will not appear
