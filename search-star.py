import requests

# Thresholds
min_stars = 2000
min_forks = 200
min_issues = 10
min_contributors = 1

# Personal Access Token for Authentication
access_token = open("../github-personal-access-token.txt", 'r').read()

# Gets all repos under a certain programming language
def get_repos(language):
    response = requests.get("https://api.github.com/legacy/repos/search/{}?language={}".format(language, language))
    data = response.json()
    return data

# Retrieving all relevant information from a repo's JSON
def get_info(repo):
    name = repo["name"]
    creator = repo["owner"]
    description = repo["description"]
    forks = repo["forks"]
    stars = repo["followers"]
    issues = repo["open_issues"]
    created_date = repo["created"].split("T")[0]
    last_pushed_date = repo["pushed"].split("T")[0]
    link = repo["url"]
    return (name, creator, description, forks, stars, issues, created_date, last_pushed_date, link)

# Does nothing for now
def extend(repo):
    response = requests.get(repo.url)
    return response

# Main function
if __name__ == "__main__":
    language = "Python"
    repos = get_repos(language)

    # Looping through all repos
    for repo in repos["repositories"]:
        valid = True

        # Getting info on repo
        name, creator, description, forks, stars, issues, created_date, last_pushed_date, link = get_info(repo)

        # Checking repo against thresholds
        if stars < min_stars:
            valid = False
        elif forks < min_forks:
            valid = False
        elif issues < min_issues:
            valid = False

        if valid:
            info_string = f"""
            Name: {name}
            Creator: {creator}
            Description: {description}
            Forks: {forks}
            Stars: {stars}
            Issues: {issues}
            Created: {created_date}
            Last Updated: {last_pushed_date}
            Link: {link}
            """
            result = input(info_string + "Do you want to star this repository? Yes(y) or No(n)? ")
            if result.lower() == "y":
                subprocess.run(f"curl -X PUT -u calixo888:{access_token} https://api.github.com/user/starred/{creator}/{name}".split())
            elif result.lower() == "n":
                pass
            elif result.lower() == "q":
                print("[+] Shutting down...")
                break
