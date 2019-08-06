import os
import glob

ROOT_DIR = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__))))


def get_allowed_words_as_tuple():
    with open(os.path.join(ROOT_DIR, "allowed_verbs")) as f:
        retval = []
        verbs = f.readlines()
        for verb in verbs:
            retval.append(verb.strip("\n"))
        return retval


def get_git_dir():
    git_dir_name = ".git"
    working_dir = os.getcwd()
    while working_dir != "/" and git_dir_name not in os.listdir(working_dir):
        working_dir = os.path.abspath(working_dir + "/../")
    os.chdir(f"{working_dir}/.git/")
    return os.path.abspath(os.getcwd())


def main(argv=None):
    retval = 0

    git_dir = get_git_dir()
    git_hooks_dir = os.path.join(git_dir, "hooks")
    git_hooks_file = os.path.join(git_hooks_dir, "commit-msg.sample")

    try:
        with open(os.path.join(ROOT_DIR, "script")) as f:
            script_content = f.readlines()
            allowed_verbs_index = script_content.index("ALLOWED_VERBS = (\"\",)\n")
            script_content[
                allowed_verbs_index] = f'ALLOWED_VERBS = {get_allowed_words_as_tuple()}'

        with open(git_hooks_file, "w") as f:
            f.write("".join(script_content))

        new_file = os.path.join(git_hooks_dir, "commit-msg")
        print(f"Commit-msg hooks successfully installed in directory: {new_file}")
        os.rename(git_hooks_file, new_file)
        os.system(f"chmod +x {new_file}")
    except Exception as e:
        print(e)
        retval = 1

    return retval


if __name__ == '__main__':
    exit(main())
