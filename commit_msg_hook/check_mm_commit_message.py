import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__))))


def get_allowed_words_as_tuple():
    with open(os.path.join(ROOT_DIR, "allowed_verbs")) as f:
        retval = []
        verbs = f.readlines()
        for verb in verbs:
            retval.append(verb.strip("\n"))

        return retval


def main(argv=None):
    retval = 0
    git_hooks_dir = os.path.join(os.getcwd(), ".git", "hooks")
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
        os.rename(git_hooks_file, new_file)
        os.system(f"chmod +x {new_file}")
    except Exception as e:
        print(e)
        retval = 1

    return retval


if __name__ == '__main__':
    exit(main())
