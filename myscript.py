import os

def git_bisect(bad_hash, good_hash, test_command):
    os.system(f"git bisect start {bad_hash} {good_hash}")
    os.system(f"git bisect run {test_command}")

if __name__ == "__main__":
    bad_hash = "6bc0c0aa3f78ccad3230f451b51c70c03569f848"
    good_hash = "a9f20e8a511665d81967342e7829e737395944d3"

    test_command = "python manage.py test"

    git_bisect(bad_hash, good_hash, test_command)
