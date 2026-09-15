import subprocess


def get_java_major_version(java_version_output):
    # Version parser function, stripping the .stderr (for java specifically) return into only the version int.
    version_line = java_version_output.split("\n")[0]
    version_text = version_line.split('"')[1]
    major_version_text = version_text.split(".")[0]
    major_version = int(major_version_text)

    return major_version


def main():
    try:
        check_java = subprocess.run(
            ["java", "-version"], capture_output=True, text=True
        )
        check_java_output = check_java.stderr

        if check_java.returncode != 0:
            print(
                "ServerDeck found Java but could not read its version. Verify that your Java installation is working, then try again."
            )
            print(check_java.stderr)
            return
    except FileNotFoundError:
        print(
            "Java could not be found. Install Java and make sure it is available from the command line."
        )
        return

    java_version = get_java_major_version(check_java_output)

    print(java_version)


if __name__ == "__main__":
    main()
