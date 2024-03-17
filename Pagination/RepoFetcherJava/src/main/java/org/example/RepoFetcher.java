package org.example;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpHeaders;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpResponse.BodyHandlers;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Date;
import java.util.List;

@JsonIgnoreProperties(ignoreUnknown = true)
record RepoItem(String name, @JsonProperty("pushed_at") Date pushedAt){
  public String getName() {
    return name;
  }

  public Date getDate() {
    return pushedAt;
  }
}
public class RepoFetcher {
  private final String baseUrl;
  private final HttpClient client;
  private final ObjectMapper mapper;

  RepoFetcher(String url) {
    baseUrl = url;
    client = HttpClient.newHttpClient();
    mapper = new ObjectMapper();
  }

  public List<RepoItem> getAllRepos() throws IOException, InterruptedException {
    String hasNext = this.baseUrl;
    List<RepoItem> totalResult = new ArrayList<>();

    while (!hasNext.isEmpty()) {
      HttpRequest request = HttpRequest.newBuilder().uri(URI.create(hasNext)).build();
      HttpResponse response = client.send(request, BodyHandlers.ofString());

      List<RepoItem> repoItems = mapper.readValue(response.body().toString(),
          new TypeReference<>() {
          });

      totalResult.addAll(repoItems);
      hasNext = parserLinkNext(response.headers());
    }

    return totalResult;
  }

  private String parserLinkNext(HttpHeaders headers) {
    final var links = headers.allValues("Link").get(0).split(",");

    for (String link : links) {
      if (link.contains("next")) {
        return link.substring(link.indexOf("<") + 1, link.indexOf(">"));
      }
    }

    return "";
  }

  public List<RepoItem> getSortedReposByName() throws IOException, InterruptedException {
    final var repos = getAllRepos();
    repos.sort(Comparator.comparing(RepoItem::getName));
    return repos;
  }

  public List<RepoItem> getSortedReposByDate() throws IOException, InterruptedException {
    final var repos = getAllRepos();
    repos.sort(Comparator.comparing(RepoItem::getDate).reversed());
    return repos;
  }
}
