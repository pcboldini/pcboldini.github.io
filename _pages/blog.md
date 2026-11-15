---
layout: page
title: posts
permalink: /blog/
description: All posts, newest first.
nav: false
---

{% assign posts_by_year = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
{% for year in posts_by_year %}
<h3 class="home-h"><span class="hh-icon"><i class="fa-solid fa-calendar"></i></span>{{ year.name }}</h3>
<div class="post-grid">
  {% for item in year.items %}
    {% assign kind = 'News' %}
    {% if item.tags contains 'paper' or item.tags contains 'publication' %}{% assign kind = 'Paper' %}{% endif %}
    {% if item.tags contains 'github' or item.tags contains 'solver' %}{% assign kind = 'Software' %}{% endif %}
    {% if item.tags contains 'talk' or item.tags contains 'seminar' or item.title contains 'talk' or item.title contains 'Talk' or item.title contains 'seminar' %}{% assign kind = 'Talk' %}{% endif %}
    {% assign img = nil %}
    {% if item.content contains '<img' %}{% assign parts = item.content | split: 'src="' %}{% assign img = parts[1] | split: '"' | first %}{% endif %}
    <a class="post-card" href="{{ item.url | relative_url }}">
      {% if img %}<div class="post-thumb"><img src="{{ img }}" alt="" loading="lazy"></div>{% else %}<div class="post-thumb post-thumb-empty"><i class="fa-solid fa-wave-square"></i></div>{% endif %}
      <div class="post-body">
        <div class="post-meta"><span class="post-kind post-kind-{{ kind | downcase }}">{{ kind }}</span><span class="post-date">{{ item.date | date: '%b %d, %Y' }}</span></div>
        <div class="post-title-card">{{ item.title }}</div>
      </div>
    </a>
  {% endfor %}
</div>
{% endfor %}
