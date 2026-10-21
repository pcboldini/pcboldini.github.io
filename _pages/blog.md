---
layout: page
title: posts
permalink: /blog/
description: All posts, newest first.
nav: false
---

<div class="news">
{% assign posts_by_year = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
{% for year in posts_by_year %}
  <h3>{{ year.name }}</h3>
  <table class="table table-sm table-borderless">
    {% for item in year.items %}
      <tr>
        <th scope="row" style="width: 20%">{{ item.date | date: '%b %d, %Y' }}</th>
        <td><a class="news-title" href="{{ item.url | relative_url }}">{{ item.title }}</a></td>
      </tr>
    {% endfor %}
  </table>
{% endfor %}
</div>
