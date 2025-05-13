import subprocess
import yaml
import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python add_users.py <path_to_yaml_file>")
        sys.exit(1)

    yaml_file = sys.argv[1]
    
    if not os.path.exists(yaml_file):
        print(f"File not found: {yaml_file}")
        sys.exit(1)

    contest_id = "3"
    cms_command = "./cms/cms-venv/bin/cmsAddParticipation"

    # Load YAML data
    with open(yaml_file, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    # Iterate over users
    for user in data.get("users", []):
        username = user["username"]
        print(f"Adding user: {username} to contest {contest_id}")
        subprocess.run([cms_command, username, "-c", contest_id])

if __name__ == "__main__":
    main()
