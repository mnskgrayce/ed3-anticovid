# Engineering Design 3

## Project Structure
The project has three branches (not including master), each corresponding to a folder of the same name:
- **user-interface** (Trang, Han)
- **hardware-sensor** (Duc, Uyen)
- **vision** (Thien)

## Get Started
Clone this repository onto your local machine then perform the following steps:
1. Checkout the branch corresponding to your subteam
2. Create a folder with the same name as the branch to contain your subteam's code
3. Push and update within your branch

## Git Workflow
- Update remote changes to entire project with `git fetch origin`
- View the code at the remote branch with `git checkout origin/branch_name`
- Check the code to see if it's safe to merge with your local branch
- Return to your local branch with `git checkout your_branch`
- Merge changes from a remote branch to your current branch with `git merge origin/branch_name`
- Modify your code, then use `git add .` and `git commit -m "commit_message"` to make local commits
- Push changes from your current branch to the remote branch with `git push origin branch_name`

## Notes
- Add the files and folders you don't want to share with the team (node_modules, configurations etc.) to the `.gitignore` file
- When you push your code to the team repository, the ignored files will not appear
