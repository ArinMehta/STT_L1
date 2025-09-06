from pydriller import Repository
import csv

repo_url = 'https://github.com/pythonprofilers/memory_profiler.git'

repo = Repository(repo_url)

keywords = ['fix', 'fixes', 'fixed', 'bug', 'bugfix', 'defect', 'defects',
            'error', 'issue', 'patch', 'repair', 'fault', 'resolved', 'resolve']

def is_a_bug_fixing_commit(msg):
    if msg is None or msg == "":
        return False
    msg = msg.lower()
    for keyword in keywords:
        if keyword in msg:
            return True
    return False

with open("bug_fixing_commits.csv", mode='w', newline='', encoding='utf-8') as file:
    write = csv.writer(file)
    write.writerow(["Hash", "Message", "Hashes of Parents",
                    "Is a merge commit", "List of modified files"])
    
    for commit in repo.traverse_commits():
        msg = commit.msg.lower()
        if is_a_bug_fixing_commit(msg) == True:

            parents = commit.parents

            if len(commit.parents) > 1:
                is_merge = "Yes"
            else:
                is_merge = "No"

            modif_file = []
            for mod in commit.modifications:
                if mod.new_path:
                    modif_file.append(mod.new_path)

            write.writerow([commit.hash, commit.msg.strip().replace("\n"," "),
                           parents, is_merge, modif_file])