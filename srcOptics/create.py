# Helpers for creating and adding models to the db
#
# Austin Shafer

from srcOptics.models import *

class Creator:
    # ------------------------------------------------------------------
    # DB helper functions
    #
    # Wrappers for adding objects to the database to keep that functionality
    # out of the clone/scanning functions above.

    # ------------------------------------------------------------------
    def create_repo(org_name, repo_url, repo_name, cred):
        org_parent = Organization.objects.get(name=org_name)
        try:
            repo_instance = Repository.objects.get(name=repo_name)
        except:
            repo_instance = Repository.objects.create(cred=cred, url=repo_url, name=repo_name)
        return repo_instance

    # ------------------------------------------------------------------
    def create_author(email):
        try:
            author_instance = Author.objects.get(email=email)
        except:
            author_instance = Author.objects.create(email=email)
        return author_instance

    # ------------------------------------------------------------------
    def create_commit(repo_instance, subject, author_instance, sha_, author_date_, commit_date_, added, removed):
        try:
            commit_instance = Commit.objects.get(sha=sha_)
        except:
            commit_instance = Commit.objects.create(repo=repo_instance, author=author_instance, sha=sha_, commit_date=commit_date_, author_date=author_date_, lines_added=added, lines_removed=removed, subject=subject)
        return commit_instance

    # ------------------------------------------------------------------
    def create_filechange(path, commit, la, lr, binary):
        # find the extension
        split = path.rsplit('.', 1)
        ext = ""
        if len(split) > 1:
            ext = split[1]
                
        #get the file name
        fArray = path.rsplit('/', 1)
        
        fName = ""
        if len(fArray) > 1:
            fName = fArray[1]
        else:
            fName = fArray[0]
            
        filechange_instance = FileChange.objects.create(name=fName, path=path, ext=ext, commit=commit, repo=commit.repo, lines_added=la, lines_removed=lr, binary=binary)
            
        return filechange_instance

    # ------------------------------------------------------------------
    def create_file(path, commit, la, lr, binary):
        #get the file name
        fArray = path.rsplit('/', 1)
        
        fName = ""
        if len(fArray) > 1:
            fName = fArray[1]
        else:
            fName = fArray[0]

        try:
            file_instance = File.objects.get(name=fName, path=path)

            # update the lines added/removed
            file_instance.lines_added += la
            file_instance.lines_removed += lr

            file_instance.save()
            return file_instance
            
        except:
            # find the extension
            split = path.rsplit('.', 1)
            ext = ""
            if len(split) > 1:
                ext = split[1]
            
            file_instance = File.objects.create(name=fName, path=path, ext=ext, commit=commit, repo=commit.repo, lines_added=la, lines_removed=lr, binary=binary)
            
            return file_instance