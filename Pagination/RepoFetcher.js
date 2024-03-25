class RepoFetcher {
    constructor(url){
        this.url = url;
    }

    async fetchRepo(url) {
        try {
            const response = await fetch(url);
            const listOfRepos = await response.json();
            const cursorNext = this.parseLinkNext(response.headers);
            if (response.ok) {
                return [listOfRepos, cursorNext];
            }

            return [{}, ""];
        } catch (error) {
            console.log(error);
            return [{}, ""];
        }
    }

    parseLinkNext(headers) {
        const links = headers.get("link").split(",");
        for (const link of links) {
            const result = link.split(";");
            if (result.length == 2 && result[1].includes("next")) {
                return result[0].trim().slice(1,-1);
            }
        }

        return "";
    }

    async getAllRepos() {
        const repos = [];
        let hasNext = this.url;

        while (hasNext.length > 0) {
            const [listOfRepos, cursorNext] = await this.fetchRepo(hasNext);

            for (const repo of listOfRepos) {
                const repo_item = {
                    "name": repo["name"],
                    "pushed_at": repo["pushed_at"]
                };
                repos.push(repo_item);
            }

            hasNext = cursorNext;
        }

        return repos;
    }

    async getRepoSortedByName() {
        const repos = await this.getAllRepos();
        return repos.sort((a,b) => a.name.localeCompare(b.name)) // descending order
    }

    async getRepoSortedByDate() {
        const repos = await this.getAllRepos();
        return repos.sort((a,b) => b.pushed_at.localeCompare(a.pushed_at)) // descending order
    }
}

async function main() {
    const GITHUB_URL = "https://api.github.com/orgs/agoda-com/repos"
    const repoFetcher = new RepoFetcher(GITHUB_URL);
    const repos = await repoFetcher.getRepoSortedByDate();
    console.log(repos);

/**
[
  { name: 'AgodaAnalyzers', pushed_at: '2023-10-08T07:14:10Z' },
  { name: 'autorest.csharp', pushed_at: '2023-07-21T07:30:11Z' },
  { name: 'mention-bot', pushed_at: '2023-03-03T00:50:55Z' },
  { name: 'swagger-codegen', pushed_at: '2023-03-03T00:44:39Z' },
  { name: 'Todo-app-sample', pushed_at: '2023-03-03T00:40:25Z' },
   ...
  { name: 'kafka-jdbc-connector', pushed_at: '2017-10-01T06:23:46Z' },
  { name: 'consul-mirror', pushed_at: '2017-09-05T11:21:57Z' },
  { name: 'Hangfire', pushed_at: '2017-07-10T14:12:27Z' },
  { name: 'Hangfire-Documentation', pushed_at: '2017-06-22T17:42:30Z' },
  { name: 'Swashbuckle', pushed_at: '2017-03-14T08:51:12Z' },
  { name: 'swagger-akka-http', pushed_at: '2017-01-25T01:23:42Z' },
  { name: 'nunit', pushed_at: '2017-01-04T03:48:12Z' },
  { name: 'octokit.net', pushed_at: '2016-10-30T05:29:56Z' },
  { name: 'pullmasi.github.io', pushed_at: '2016-08-02T02:09:33Z' }
*/
}

main();