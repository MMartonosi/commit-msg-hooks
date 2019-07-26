import os


def main(argv=None):
    retval = 0
    git_hooks_file = os.path.join(os.getcwd(), ".git", "hooks", "commit-msg.example")
    with open(git_hooks_file) as f:
        f.write("#!/usr/bin/python")
        # user_data = data.split("[user]")[1]
        # user_email = user_data.split("email = ")[1]
        # if not "@mediamonks.com" in user_email:
        #     print("Email address used in this git repo doesn't "
        #           "seem to have mediamonks domain")
        #     retval = 1

    return retval


if __name__ == '__main__':
    exit(main())