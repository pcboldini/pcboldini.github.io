---
permalink: /assets/js/search-data.js
---
// search index for the ninja-keys command palette (cmd/ctrl + k)
const ninja = document.querySelector("ninja-keys");
ninja.data = [
  {
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => { window.location.href = "{{ '/' | relative_url }}"; },
  },
  {%- assign nav_pages = site.pages | where: "nav", true | sort: "nav_order" -%}
  {%- for p in nav_pages %}
  {
    id: "nav-{{ p.title | slugify }}",
    title: {{ p.title | jsonify }},
    description: {{ p.description | strip_html | jsonify }},
    section: "Navigation",
    handler: () => { window.location.href = "{% if p.permalink contains '://' %}{{ p.permalink }}{% else %}{{ p.permalink | relative_url }}{% endif %}"; },
  },
  {%- endfor %}
  {
    id: "nav-posts",
    title: "posts",
    section: "Navigation",
    handler: () => { window.location.href = "{{ '/blog/' | relative_url }}"; },
  },
  {%- for post in site.posts %}
  {
    id: "post-{{ post.url | slugify }}",
    title: {{ post.title | strip_html | jsonify }},
    description: {{ post.date | date: '%b %d, %Y' | jsonify }},
    section: "Posts",
    handler: () => { window.location.href = "{{ post.url | relative_url }}"; },
  },
  {%- endfor %}
  {
    id: "social-email",
    title: "email",
    section: "Socials",
    handler: () => { window.open("mailto:{{ site.data.socials.email }}", "_blank"); },
  },
  {
    id: "social-scholar",
    title: "Google Scholar",
    section: "Socials",
    handler: () => { window.open("https://scholar.google.com/citations?user=EFjb36EAAAAJ", "_blank"); },
  },
  {
    id: "social-github",
    title: "GitHub",
    section: "Socials",
    handler: () => { window.open("https://github.com/{{ site.data.socials.github_username }}", "_blank"); },
  },
  {
    id: "social-orcid",
    title: "ORCID",
    section: "Socials",
    handler: () => { window.open("https://orcid.org/{{ site.data.socials.orcid_id }}", "_blank"); },
  },
  {
    id: "social-researchgate",
    title: "ResearchGate",
    section: "Socials",
    handler: () => { window.open("https://www.researchgate.net/profile/{{ site.data.socials.research_gate_profile }}", "_blank"); },
  },
  {
    id: "light-theme",
    title: "Change theme to light",
    section: "Theme",
    handler: () => { setThemeSetting("light"); },
  },
  {
    id: "dark-theme",
    title: "Change theme to dark",
    section: "Theme",
    handler: () => { setThemeSetting("dark"); },
  },
  {
    id: "system-theme",
    title: "Use system default theme",
    section: "Theme",
    handler: () => { setThemeSetting("system"); },
  },
];
