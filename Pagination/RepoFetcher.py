# api.github.io ratelimit 60 per day
# pip3 install requests

import requests

class RepoFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_paginated_repo(self, current_page):
        try:
            response = requests.get(current_page)
            response.raise_for_status()
            cursor_next = self.parse_link_next(response.headers)
            return response.json(), cursor_next
        except requests.exceptions.HTTPError as _:
            error_message = response.json().get("message")
            print(f"error message: {error_message}") # error message:  API rate limit exceeded for x.x.x.x.
            return None, None
        except Exception as error:
            print(f"uncaught error: {error}")
            return None, None

    def parse_link_next(self, headers):
        links = headers['Link'].split(",")
        for link in links:
            result = link.split(";")
            if len(result) == 2:
                if "next" in result[1]:
                       return result[0].strip().strip("<>")
        return None

    def get_all_repos(self):
        has_next = self.url
        repos = []

        while has_next and len(has_next) > 0:
            response, cursor_next = self.fetch_paginated_repo(has_next)
            if response is not None:
                for repo in response:
                    repo_info = {
                        "name": repo["name"],
                        "pushed_at": repo["pushed_at"]
                    }
                    repos.append(repo_info)
            has_next = cursor_next
        return repos

    def get_sorted_repos_by_name(self):
        repos = self.get_all_repos()
        return sorted(repos, key=lambda x:x["name"])

    def get_sorted_repos_by_date(self):
        repos = self.get_all_repos()
        return sorted(repos, key=lambda x:x["pushed_at"], reverse=True)

GITHUB_URL = "https://api.github.com/orgs/agoda-com/repos"
repo_fetcher = RepoFetcher(GITHUB_URL)
repos = repo_fetcher.get_all_repos()
print(repos)

repo_sorted_by_name = repo_fetcher.get_sorted_repos_by_name()
print(repo_sorted_by_name)
"""
[{'name': '.github', 'pushed_at': '2023-12-20T04:23:46Z'}, {'name': 'Agoda.IoC', 'pushed_at': '2023-08-23T10:39:29Z'}, {'name': 'AgodaAnalyzers', 'pushed_at': '2023-10-08T07:14:10Z'}, {'name': 'GraphQlGenSharp', 'pushed_at': '2018-07-16T04:08:33Z'}, {'name': 'Hangfire', 'pushed_at': '2017-07-10T14:12:27Z'}, {'name': 'Hangfire-Documentation', 'pushed_at': '2017-06-22T17:42:30Z'}, {'name': 'JsonCSharpClassGenerator', 'pushed_at': '2021-07-25T08:08:17Z'}, {'name': 'KafkaFlow.ApplicationInsights', 'pushed_at': '2023-12-22T07:37:18Z'}, {'name': 'Kakao', 'pushed_at': '2021-05-26T07:38:45Z'}, {'name': 'NJsonSchema.CodeGeneration.CLI', 'pushed_at': '2021-07-18T06:40:38Z'}, {'name': 'OSX-KVM', 'pushed_at': '2024-01-02T05:10:03Z'}, {'name': 'Rebus.Kafka', 'pushed_at': '2018-11-04T07:01:30Z'}, {'name': 'Shouldly.FromAssert', 'pushed_at': '2024-03-13T02:10:18Z'}, {'name': 'SlackAPI', 'pushed_at': '2019-05-03T04:34:27Z'}, {'name': 'StructuredMapper', 'pushed_at': '2018-11-22T09:22:37Z'}, {'name': 'Swashbuckle', 'pushed_at': '2017-03-14T08:51:12Z'}, {'name': 'SwiftLint', 'pushed_at': '2023-05-09T09:39:58Z'}, {'name': 'SwiftLint-Bazel', 'pushed_at': '2023-06-15T15:44:16Z'}, {'name': 'Todo-app-sample', 'pushed_at': '2023-03-03T00:40:25Z'}, {'name': 'VideoCompress', 'pushed_at': '2022-09-01T13:35:56Z'}, {'name': 'adb-butler', 'pushed_at': '2022-02-07T05:21:05Z'}, {'name': 'agoda-design-toolkit', 'pushed_at': '2023-03-02T23:29:29Z'}, {'name': 'android-ci', 'pushed_at': '2023-06-19T04:43:26Z'}, {'name': 'android-farm', 'pushed_at': '2020-05-03T11:21:50Z'}, {'name': 'archaius-consul', 'pushed_at': '2023-03-03T00:34:01Z'}, {'name': 'arm64-to-sim', 'pushed_at': '2021-06-03T07:04:01Z'}, {'name': 'autorest', 'pushed_at': '2023-03-02T23:44:00Z'}, {'name': 'autorest.csharp', 'pushed_at': '2023-07-21T07:30:11Z'}, {'name': 'boots', 'pushed_at': '2019-10-10T09:45:41Z'}, {'name': 'capacitor', 'pushed_at': '2023-11-07T10:35:56Z'}, {'name': 'charts', 'pushed_at': '2018-07-09T11:18:55Z'}, {'name': 'cicd', 'pushed_at': '2023-03-02T22:23:25Z'}, {'name': 'cluster-api-provider-gcp', 'pushed_at': '2020-07-20T06:08:52Z'}, {'name': 'consul', 'pushed_at': '2017-10-31T14:58:30Z'}, {'name': 'consul-mirror', 'pushed_at': '2017-09-05T11:21:57Z'}, {'name': 'consuldotnet', 'pushed_at': '2018-05-16T19:08:48Z'}, {'name': 'couchbase-net-client', 'pushed_at': '2018-02-06T17:43:04Z'}, {'name': 'dependabot-script', 'pushed_at': '2023-03-07T21:59:58Z'}, {'name': 'devfeedback-js', 'pushed_at': '2024-02-19T10:25:04Z'}, {'name': 'docker-emulator-android', 'pushed_at': '2022-04-05T11:59:18Z'}, {'name': 'docker-smbupload', 'pushed_at': '2022-01-17T09:44:18Z'}, {'name': 'dotnet-build-metrics', 'pushed_at': '2023-11-03T05:44:33Z'}, {'name': 'eslint-config-agoda', 'pushed_at': '2023-11-21T22:44:05Z'}, {'name': 'example-scala', 'pushed_at': '2020-01-13T06:43:29Z'}, {'name': 'feast', 'pushed_at': '2023-03-02T23:00:40Z'}, {'name': 'feathr', 'pushed_at': '2023-03-02T22:44:07Z'}, {'name': 'fission', 'pushed_at': '2023-03-02T23:56:27Z'}, {'name': 'fork', 'pushed_at': '2023-03-03T00:17:27Z'}, {'name': 'ga-big-branch-warning', 'pushed_at': '2021-01-20T01:08:59Z'}, {'name': 'ga-npm-wildcard-check', 'pushed_at': '2021-01-20T00:34:37Z'}, {'name': 'ga-nuget-alpha-detection', 'pushed_at': '2021-01-20T15:13:37Z'}, {'name': 'ga-samples', 'pushed_at': '2021-01-19T01:32:58Z'}, {'name': 'gitlab-client', 'pushed_at': '2024-02-11T10:30:37Z'}, {'name': 'gradle-play-publisher', 'pushed_at': '2019-12-12T08:16:49Z'}, {'name': 'graphql-code-generator', 'pushed_at': '2023-03-03T00:00:42Z'}, {'name': 'graphql-codegen-csharp', 'pushed_at': '2023-03-02T23:02:45Z'}, {'name': 'helm', 'pushed_at': '2018-07-08T15:44:29Z'}, {'name': 'icolormg', 'pushed_at': '2019-10-28T11:34:57Z'}, {'name': 'ignore-styled-components-theme', 'pushed_at': '2023-03-02T22:27:33Z'}, {'name': 'junit4', 'pushed_at': '2023-03-02T23:58:36Z'}, {'name': 'kafka-jdbc-connector', 'pushed_at': '2017-10-01T06:23:46Z'}, {'name': 'kafka-jdbc-connector-samples', 'pushed_at': '2017-10-01T07:25:44Z'}, {'name': 'keychain-cleaner', 'pushed_at': '2018-04-12T10:55:38Z'}, {'name': 'marathon', 'pushed_at': '2024-01-22T08:53:02Z'}, {'name': 'mention-bot', 'pushed_at': '2023-03-03T00:50:55Z'}, {'name': 'muter', 'pushed_at': '2022-09-16T07:20:50Z'}, {'name': 'nerv', 'pushed_at': '2023-03-02T23:25:20Z'}, {'name': 'net-loadbalancing', 'pushed_at': '2024-03-05T02:48:36Z'}, {'name': 'nexus-public', 'pushed_at': '2023-03-03T00:13:17Z'}, {'name': 'ninjato', 'pushed_at': '2021-06-14T11:45:41Z'}, {'name': 'nunit', 'pushed_at': '2017-01-04T03:48:12Z'}, {'name': 'octokit.net', 'pushed_at': '2016-10-30T05:29:56Z'}, {'name': 'opentelemetry-go', 'pushed_at': '2024-02-13T07:05:07Z'}, {'name': 'opentelemetry-logs-go', 'pushed_at': '2024-02-27T14:54:11Z'}, {'name': 'otelzap', 'pushed_at': '2023-09-29T03:51:25Z'}, {'name': 'playground', 'pushed_at': '2021-08-18T08:36:02Z'}, {'name': 'pullmasi.github.io', 'pushed_at': '2016-08-02T02:09:33Z'}, {'name': 'react-handyman', 'pushed_at': '2023-03-02T22:29:39Z'}, {'name': 'samsahai', 'pushed_at': '2024-01-05T09:14:17Z'}, {'name': 'samsahai-example', 'pushed_at': '2023-03-02T11:38:42Z'}, {'name': 'scoold', 'pushed_at': '2023-03-03T00:09:00Z'}, {'name': 'screenshot-tests-for-android', 'pushed_at': '2022-05-27T07:11:45Z'}, {'name': 'sonar-csharp', 'pushed_at': '2023-03-03T00:11:09Z'}, {'name': 'sonarqube-roslyn-sdk', 'pushed_at': '2018-06-19T09:33:28Z'}, {'name': 'spark-cassandra-connector', 'pushed_at': '2022-03-01T04:19:02Z'}, {'name': 'spark-hpopt', 'pushed_at': '2021-02-10T08:48:44Z'}, {'name': 'standards-c-sharp', 'pushed_at': '2019-02-10T13:54:57Z'}, {'name': 'swagger-akka-http', 'pushed_at': '2017-01-25T01:23:42Z'}, {'name': 'swagger-codegen', 'pushed_at': '2023-03-03T00:44:39Z'}, {'name': 'teldrassil', 'pushed_at': '2023-01-13T10:52:15Z'}, {'name': 'testresults-collector', 'pushed_at': '2024-02-19T09:20:08Z'}, {'name': 'tslint-rules', 'pushed_at': '2023-03-02T23:48:09Z'}, {'name': 'ycs5-pricing-api-spec', 'pushed_at': '2022-10-08T13:56:02Z'}]
"""

repo_sorted_by_date = repo_fetcher.get_sorted_repos_by_date()
print(repo_sorted_by_date)
"""
[{'name': 'Shouldly.FromAssert', 'pushed_at': '2024-03-13T02:10:18Z'}, {'name': 'net-loadbalancing', 'pushed_at': '2024-03-05T02:48:36Z'}, {'name': 'opentelemetry-logs-go', 'pushed_at': '2024-02-27T14:54:11Z'}, {'name': 'devfeedback-js', 'pushed_at': '2024-02-19T10:25:04Z'}, {'name': 'testresults-collector', 'pushed_at': '2024-02-19T09:20:08Z'}, {'name': 'opentelemetry-go', 'pushed_at': '2024-02-13T07:05:07Z'}, {'name': 'gitlab-client', 'pushed_at': '2024-02-11T10:30:37Z'}, {'name': 'marathon', 'pushed_at': '2024-01-22T08:53:02Z'}, {'name': 'samsahai', 'pushed_at': '2024-01-05T09:14:17Z'}, {'name': 'OSX-KVM', 'pushed_at': '2024-01-02T05:10:03Z'}, {'name': 'KafkaFlow.ApplicationInsights', 'pushed_at': '2023-12-22T07:37:18Z'}, {'name': '.github', 'pushed_at': '2023-12-20T04:23:46Z'}, {'name': 'eslint-config-agoda', 'pushed_at': '2023-11-21T22:44:05Z'}, {'name': 'capacitor', 'pushed_at': '2023-11-07T10:35:56Z'}, {'name': 'dotnet-build-metrics', 'pushed_at': '2023-11-03T05:44:33Z'}, {'name': 'AgodaAnalyzers', 'pushed_at': '2023-10-08T07:14:10Z'}, {'name': 'otelzap', 'pushed_at': '2023-09-29T03:51:25Z'}, {'name': 'Agoda.IoC', 'pushed_at': '2023-08-23T10:39:29Z'}, {'name': 'autorest.csharp', 'pushed_at': '2023-07-21T07:30:11Z'}, {'name': 'android-ci', 'pushed_at': '2023-06-19T04:43:26Z'}, {'name': 'SwiftLint-Bazel', 'pushed_at': '2023-06-15T15:44:16Z'}, {'name': 'SwiftLint', 'pushed_at': '2023-05-09T09:39:58Z'}, {'name': 'dependabot-script', 'pushed_at': '2023-03-07T21:59:58Z'}, {'name': 'mention-bot', 'pushed_at': '2023-03-03T00:50:55Z'}, {'name': 'swagger-codegen', 'pushed_at': '2023-03-03T00:44:39Z'}, {'name': 'Todo-app-sample', 'pushed_at': '2023-03-03T00:40:25Z'}, {'name': 'archaius-consul', 'pushed_at': '2023-03-03T00:34:01Z'}, {'name': 'fork', 'pushed_at': '2023-03-03T00:17:27Z'}, {'name': 'nexus-public', 'pushed_at': '2023-03-03T00:13:17Z'}, {'name': 'sonar-csharp', 'pushed_at': '2023-03-03T00:11:09Z'}, {'name': 'scoold', 'pushed_at': '2023-03-03T00:09:00Z'}, {'name': 'graphql-code-generator', 'pushed_at': '2023-03-03T00:00:42Z'}, {'name': 'junit4', 'pushed_at': '2023-03-02T23:58:36Z'}, {'name': 'fission', 'pushed_at': '2023-03-02T23:56:27Z'}, {'name': 'tslint-rules', 'pushed_at': '2023-03-02T23:48:09Z'}, {'name': 'autorest', 'pushed_at': '2023-03-02T23:44:00Z'}, {'name': 'agoda-design-toolkit', 'pushed_at': '2023-03-02T23:29:29Z'}, {'name': 'nerv', 'pushed_at': '2023-03-02T23:25:20Z'}, {'name': 'graphql-codegen-csharp', 'pushed_at': '2023-03-02T23:02:45Z'}, {'name': 'feast', 'pushed_at': '2023-03-02T23:00:40Z'}, {'name': 'feathr', 'pushed_at': '2023-03-02T22:44:07Z'}, {'name': 'react-handyman', 'pushed_at': '2023-03-02T22:29:39Z'}, {'name': 'ignore-styled-components-theme', 'pushed_at': '2023-03-02T22:27:33Z'}, {'name': 'cicd', 'pushed_at': '2023-03-02T22:23:25Z'}, {'name': 'samsahai-example', 'pushed_at': '2023-03-02T11:38:42Z'}, {'name': 'teldrassil', 'pushed_at': '2023-01-13T10:52:15Z'}, {'name': 'ycs5-pricing-api-spec', 'pushed_at': '2022-10-08T13:56:02Z'}, {'name': 'muter', 'pushed_at': '2022-09-16T07:20:50Z'}, {'name': 'VideoCompress', 'pushed_at': '2022-09-01T13:35:56Z'}, {'name': 'screenshot-tests-for-android', 'pushed_at': '2022-05-27T07:11:45Z'}, {'name': 'docker-emulator-android', 'pushed_at': '2022-04-05T11:59:18Z'}, {'name': 'spark-cassandra-connector', 'pushed_at': '2022-03-01T04:19:02Z'}, {'name': 'adb-butler', 'pushed_at': '2022-02-07T05:21:05Z'}, {'name': 'docker-smbupload', 'pushed_at': '2022-01-17T09:44:18Z'}, {'name': 'playground', 'pushed_at': '2021-08-18T08:36:02Z'}, {'name': 'JsonCSharpClassGenerator', 'pushed_at': '2021-07-25T08:08:17Z'}, {'name': 'NJsonSchema.CodeGeneration.CLI', 'pushed_at': '2021-07-18T06:40:38Z'}, {'name': 'ninjato', 'pushed_at': '2021-06-14T11:45:41Z'}, {'name': 'arm64-to-sim', 'pushed_at': '2021-06-03T07:04:01Z'}, {'name': 'Kakao', 'pushed_at': '2021-05-26T07:38:45Z'}, {'name': 'spark-hpopt', 'pushed_at': '2021-02-10T08:48:44Z'}, {'name': 'ga-nuget-alpha-detection', 'pushed_at': '2021-01-20T15:13:37Z'}, {'name': 'ga-big-branch-warning', 'pushed_at': '2021-01-20T01:08:59Z'}, {'name': 'ga-npm-wildcard-check', 'pushed_at': '2021-01-20T00:34:37Z'}, {'name': 'ga-samples', 'pushed_at': '2021-01-19T01:32:58Z'}, {'name': 'cluster-api-provider-gcp', 'pushed_at': '2020-07-20T06:08:52Z'}, {'name': 'android-farm', 'pushed_at': '2020-05-03T11:21:50Z'}, {'name': 'example-scala', 'pushed_at': '2020-01-13T06:43:29Z'}, {'name': 'gradle-play-publisher', 'pushed_at': '2019-12-12T08:16:49Z'}, {'name': 'icolormg', 'pushed_at': '2019-10-28T11:34:57Z'}, {'name': 'boots', 'pushed_at': '2019-10-10T09:45:41Z'}, {'name': 'SlackAPI', 'pushed_at': '2019-05-03T04:34:27Z'}, {'name': 'standards-c-sharp', 'pushed_at': '2019-02-10T13:54:57Z'}, {'name': 'StructuredMapper', 'pushed_at': '2018-11-22T09:22:37Z'}, {'name': 'Rebus.Kafka', 'pushed_at': '2018-11-04T07:01:30Z'}, {'name': 'GraphQlGenSharp', 'pushed_at': '2018-07-16T04:08:33Z'}, {'name': 'charts', 'pushed_at': '2018-07-09T11:18:55Z'}, {'name': 'helm', 'pushed_at': '2018-07-08T15:44:29Z'}, {'name': 'sonarqube-roslyn-sdk', 'pushed_at': '2018-06-19T09:33:28Z'}, {'name': 'consuldotnet', 'pushed_at': '2018-05-16T19:08:48Z'}, {'name': 'keychain-cleaner', 'pushed_at': '2018-04-12T10:55:38Z'}, {'name': 'couchbase-net-client', 'pushed_at': '2018-02-06T17:43:04Z'}, {'name': 'consul', 'pushed_at': '2017-10-31T14:58:30Z'}, {'name': 'kafka-jdbc-connector-samples', 'pushed_at': '2017-10-01T07:25:44Z'}, {'name': 'kafka-jdbc-connector', 'pushed_at': '2017-10-01T06:23:46Z'}, {'name': 'consul-mirror', 'pushed_at': '2017-09-05T11:21:57Z'}, {'name': 'Hangfire', 'pushed_at': '2017-07-10T14:12:27Z'}, {'name': 'Hangfire-Documentation', 'pushed_at': '2017-06-22T17:42:30Z'}, {'name': 'Swashbuckle', 'pushed_at': '2017-03-14T08:51:12Z'}, {'name': 'swagger-akka-http', 'pushed_at': '2017-01-25T01:23:42Z'}, {'name': 'nunit', 'pushed_at': '2017-01-04T03:48:12Z'}, {'name': 'octokit.net', 'pushed_at': '2016-10-30T05:29:56Z'}, {'name': 'pullmasi.github.io', 'pushed_at': '2016-08-02T02:09:33Z'}]
"""
