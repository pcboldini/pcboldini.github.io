---
layout: about
title: about
permalink: /
subtitle: Aerodynamics Group, Faculty of Aerospace Engineering, Delft University of Technology

profile:
  align: right
  image: prof_pic_square.jpg
  image_circular: true # crops the image to make it circular
  more_info: >
    <p>Building 45 (LSL), 00-040</p>
    <p>Leeghwaterstraat 45</p>
    <p>2628 CA Delft, The Netherlands</p>

news: false # includes a list of news items
selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page
latest_posts_in_content: true # latest posts rendered below the introduction
---

<style>
  .work-fig .card-img-top, .work-fig img { width: 100%; max-height: 260px; object-fit: contain; background: #fff; border-radius: 6px; }
  .work-cap { font-size: 0.9rem; margin-top: 0.5rem; }
  .sw-box { border-left: 4px solid var(--global-theme-color); padding: 0.8rem 1.1rem; margin: 0.8rem 0; background: var(--global-code-bg-color); border-radius: 4px; }
  .sw-box img.badge-img { height: 20px; margin-right: 4px; }
  .sw-box .btn { font-size: 0.8rem; padding: 0.15rem 0.6rem; margin: 0.15rem 0.25rem 0.15rem 0; }
  .sw-row { display: flex; align-items: center; gap: 1rem; margin-bottom: 0.8rem; }
  .sw-row:last-child { margin-bottom: 0; }
  .sw-row .sw-logo { width: 88px; flex-shrink: 0; background: #fff; border-radius: 6px; padding: 4px; }
  .hl-box { display: flow-root; border: 1px solid var(--global-theme-color); border-radius: 6px; padding: 0.6rem 1rem; margin: 0 0 1.2rem 0; font-size: 0.95rem; }
  .hl-box .hl-tag { background: var(--global-theme-color); color: #fff; border-radius: 4px; padding: 0.05rem 0.45rem; font-size: 0.8rem; margin-right: 0.4rem; }
  .sw-box details { display: inline-block; }
  .sw-box details summary { display: inline-block; cursor: pointer; font-size: 0.8rem; padding: 0.15rem 0.6rem; border: 1px solid var(--global-divider-color); border-radius: 4px; list-style: none; }
  .sw-box details pre { font-size: 0.72rem; white-space: pre-wrap; margin-top: 0.4rem; }
  .stud-box { border-left: 4px solid var(--global-theme-color); padding: 0.6rem 1rem; margin: 1.2rem 0 0.5rem 0; background: var(--global-code-bg-color); border-radius: 4px; font-size: 0.95rem; }
  .hero-vid { clear: both; margin: 1rem 0 0.2rem 0; }
  .hero-vid video, .work-fig video { width: 100%; border-radius: 6px; display: block; background: #fff; }
  .vid-cap { font-size: 0.85rem; color: var(--global-text-color-light); margin-top: 0.35rem; }
  .tl { position: relative; margin: 0.8rem 0 0.5rem 0; padding-left: 1.4rem; border-left: 2px solid var(--global-theme-color); }
  .tl-item { position: relative; margin-bottom: 0.8rem; font-size: 0.92rem; display: flex; align-items: center; gap: 0.7rem; }
  .tl-logo { width: 74px; height: 38px; object-fit: contain; background: #fff; border-radius: 6px; padding: 3px 5px; flex-shrink: 0; }
  .tl-item::before { content: ''; position: absolute; left: -1.82rem; top: calc(50% - 0.35rem); width: 0.7rem; height: 0.7rem; border-radius: 50%; background: var(--global-theme-color); }
  .tl-item .tl-date { font-weight: 600; color: var(--global-theme-color); margin-right: 0.4rem; }
  .profile .more-info, .profile .more-info p { font-family: inherit !important; font-size: 0.8rem; line-height: 1.35; display: block; margin: 0; }
</style>

<div class="hl-box"><span class="hl-tag">New</span><b>DeHNSSo-v2</b>, a compressible, curvilinear, and efficient harmonic Navier&ndash;Stokes solver for boundary-layer stability, is now on arXiv. <a href="https://doi.org/10.48550/arXiv.2610.27906">Read the preprint</a></div>

I'm a postdoctoral researcher at the Delft University of Technology with particular interest in **flow instabilities**, **laminar-to-turbulent transition**, and **flow control**. My major focus lies on **highly compressible and non-ideal fluid flows**, in which unconventional high-temperature and gas dynamic effects are extremely relevant. My work combines **high-fidelity simulations**, **high-performance computing**, and **stability-analysis tools**.

My PhD research in the group of [Rene Pecnik](https://dutw1479.wbmt.tudelft.nl/~renep/) focused on the stability and transition to turbulence of **fluids at supercritical pressure**, which feature strong variations of properties (viscosity, density, etc.).

My postdoctoral research in the group of [Marios Kotsonis](https://www.tudelft.nl/staff/m.kotsonis/) focuses on **flow control through metamaterials**, with the aim of postponing transition, thereby reducing turbulence and mitigating its impact on aerodynamic drag and noise.

<h2 class="home-h" style="clear: both;"><span class="hh-icon"><i class="fa-solid fa-bullhorn"></i></span><a href="/blog/" style="color: inherit">News</a></h2>
{% include latest_posts_cards.liquid limit=3 %}

<h2 class="home-h"><span class="hh-icon"><i class="fa-solid fa-wind"></i></span>Research highlight</h2>

<div class="row mt-2">
<div class="col-md-12 mb-2 work-fig" markdown="0">
  <video autoplay loop muted playsinline preload="auto" poster="/assets/video/breakdown_poster.jpg">
    <source src="/assets/video/breakdown.mp4" type="video/mp4">
  </video>
  <p class="work-cap"><b>Breakdown to turbulence at supercritical pressure.</b> Direct numerical simulation of a heated boundary layer crossing the Widom line: vortical structures (Q-criterion, coloured by streamwise velocity) and regions of flow reversal (cyan) over one forcing period. <a href="https://doi.org/10.1017/jfm.2025.10993">J. Fluid Mech. 2025</a> &middot; <a href="https://github.com/pcboldini/DNSvisualisation">all movies</a></p>
</div>
</div>

<div class="row mt-0">
<div class="col-md-6" markdown="0">
<h2 class="home-h"><span class="hh-icon"><i class="fa-solid fa-route"></i></span>Career</h2>

<div class="tl">
  <div class="tl-item"><img class="tl-logo" src="/assets/img/logos/tudelft.png" alt="TU Delft"><div><span class="tl-date">2025&ndash;now</span>Postdoctoral researcher, Aerodynamics Group, TU Delft (ERC MetaWing)</div></div>
  <div class="tl-item"><img class="tl-logo" src="/assets/img/logos/tudelft.png" alt="TU Delft"><div><span class="tl-date">2020&ndash;2025</span>PhD, Process &amp; Energy Department, TU Delft (ERC Critical)</div></div>
  <div class="tl-item"><img class="tl-logo" src="/assets/img/logos/stuttgart.png" alt="University of Stuttgart"><div><span class="tl-date">2019&ndash;2020</span>Research associate, Institute of Aerodynamics and Gas Dynamics, University of Stuttgart</div></div>
  <div class="tl-item"><img class="tl-logo" src="/assets/img/logos/tsinghua.png" alt="Tsinghua University"><div><span class="tl-date">2018</span>MSc thesis, Laboratory for Advanced Simulation of Turbulence, Tsinghua University, Beijing</div></div>
  <div class="tl-item"><img class="tl-logo" src="/assets/img/logos/stuttgart.png" alt="University of Stuttgart"><div><span class="tl-date">2012&ndash;2018</span>BSc and MSc in Aerospace Engineering, University of Stuttgart</div></div>
</div>
</div>
<div class="col-md-6" markdown="0">
<h2 class="home-h"><span class="hh-icon"><i class="fa-solid fa-code"></i></span>Open-source software</h2>

<div class="sw-box">
  <div class="sw-row">
    <img class="sw-logo" src="/assets/img/publication_preview/CUBENS_logo.png" alt="CUBENS">
    <div>
      <b>CUBENS</b>: GPU-accelerated, high-order DNS solver for wall-bounded flows with non-ideal fluids.<br>
      <img class="badge-img" src="https://img.shields.io/github/stars/pcboldini/CUBENS?style=flat" alt="stars">
      <img class="badge-img" src="https://img.shields.io/github/license/pcboldini/CUBENS" alt="license"><br>
      <a class="btn btn-sm z-depth-0" role="button" href="https://github.com/pcboldini/CUBENS">GitHub</a>
      <a class="btn btn-sm z-depth-0" role="button" href="https://doi.org/10.1016/j.cpc.2025.109507">Paper</a>
      <details><summary>Cite</summary><pre>@article{Boldini2025CUBENS,
  title   = {CUBENS: A GPU-accelerated high-order solver for wall-bounded flows with non-ideal fluids},
  author  = {Boldini, P. C. and Hirai, R. and Costa, P. and Peeters, J. W. R. and Pecnik, R.},
  journal = {Computer Physics Communications},
  volume  = {309},
  pages   = {109507},
  year    = {2025},
  doi     = {10.1016/j.cpc.2025.109507}
}</pre></details>
    </div>
  </div>
  <div class="sw-row">
    <img class="sw-logo" src="/assets/img/research/DeHNSSo_logo.svg" alt="DeHNSSo-v2">
    <div>
      <b>DeHNSSo-v2</b>: harmonic Navier–Stokes solver for the linear and nonlinear stability of compressible boundary layers.<br>
      <img class="badge-img" src="https://img.shields.io/github/stars/pcboldini/DeHNSSo?style=flat" alt="stars">
      <img class="badge-img" src="https://img.shields.io/github/license/pcboldini/DeHNSSo" alt="license"><br>
      <a class="btn btn-sm z-depth-0" role="button" href="https://github.com/pcboldini/DeHNSSo">GitHub</a>
      <a class="btn btn-sm z-depth-0" role="button" href="https://doi.org/10.48550/arXiv.2610.27906">Preprint</a>
      <details><summary>Cite</summary><pre>@misc{Boldini2026DeHNSSo,
  title         = {DeHNSSo-v2: A compressible, curvilinear, and efficient extension of the Delft Harmonic Navier--Stokes Solver},
  author        = {Boldini, P. C. and Chen, Y. and Kotsonis, M.},
  year          = {2026},
  eprint        = {2610.27906},
  archivePrefix = {arXiv}
}</pre></details>
    </div>
  </div>
</div>
</div>
</div>

<div class="hl-box" style="margin-top: 1.4rem;"><span class="hl-tag">Contact</span>Interested in an MSc thesis or PhD project on laminar-to-turbulent transition, flow control, or GPU-accelerated simulation? Feel free to <a href="mailto:pietro.c.boldini@gmail.com">reach out</a>, also for collaborations.</div>
