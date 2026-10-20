---
layout: page
permalink: /research/
title: research
description: Instability and transition in compressible and non-ideal fluid flows
nav: true
nav_order: 1
---

<style>
  .res-card figure { margin: 0; }
  .res-card .card-img-top { height: 170px; object-fit: contain; background: #fff; padding: 6px; }
  .res-card .card-title { font-size: 1rem; margin-bottom: 0.4rem; }
  .res-card .card-text { font-size: 0.85rem; }
  .res-card .card-link { font-size: 0.85rem; }
</style>

I study how laminar flows become turbulent, and how this transition can be predicted and controlled, in flows where compressibility and non-ideal effects change the physics. My work combines stability analysis, high-fidelity simulations and high-performance computing, supported by open-source codes. The full list of papers is on the [publications](/publications/) page, and my PhD work is collected in my [thesis](https://repository.tudelft.nl/record/uuid:f9203cce-d2bd-460f-879d-8dfa4fb1bfa7).

### Instabilities in non-ideal fluids

Fluids at supercritical pressure are used in power cycles, rocket-engine cooling and heat pumps. Near the Widom line, small temperature changes cause large variations of density, viscosity and heat capacity, which reshape the stability of boundary layers.

<div class="row">
  <div class="col-md-6 mb-4">
    <div class="card h-100 res-card">
      {% include figure.liquid loading="lazy" path="assets/img/publication_preview/TSFP_inviscid.jpg" class="card-img-top" alt="A new unstable mode" %}
      <div class="card-body">
        <h5 class="card-title">A new unstable mode</h5>
        <p class="card-text">A minimum of kinematic viscosity at the Widom line creates a generalised inflection point, which explains the additional unstable mode of supercritical fluids.</p>
        <a href="https://www.researchgate.net/publication/368395270_On_the_new_unstable_mode_in_the_boundary_layer_flow_of_supercritical_fluids" class="card-link">TSFP-12, 2022</a>
      </div>
    </div>
  </div>
  <div class="col-md-6 mb-4">
    <div class="card h-100 res-card">
      {% include figure.liquid loading="lazy" path="assets/img/publication_preview/JFM_Mechanism.jpg" class="card-img-top" alt="Stratified Couette flow" %}
      <div class="card-body">
        <h5 class="card-title">Stratified Couette flow</h5>
        <p class="card-text">A minimum of kinematic viscosity also destabilises plane Couette flow, through two interacting vorticity waves driven by shear and baroclinic effects.</p>
        <a href="https://doi.org/10.1017/jfm.2024.193" class="card-link">Journal of Fluid Mechanics, 2024</a>
      </div>
    </div>
  </div>
  <div class="col-md-6 mb-4">
    <div class="card h-100 res-card">
      {% include figure.liquid loading="lazy" path="assets/img/publication_preview/PRF_streaks.jpg" class="card-img-top" alt="Non-modal growth" %}
      <div class="card-body">
        <h5 class="card-title">Non-modal growth</h5>
        <p class="card-text">Across the Widom line, the Orr mechanism joins lift-up, and optimal disturbances become streamwise-modulated streaks with strong thermal components.</p>
        <a href="https://doi.org/10.1103/PhysRevFluids.9.083901" class="card-link">Physical Review Fluids, 2024</a>
      </div>
    </div>
  </div>
  <div class="col-md-6 mb-4">
    <div class="card h-100 res-card">
      {% include figure.liquid loading="lazy" path="assets/img/publication_preview/JFM2_foc.jpg" class="card-img-top" alt="Buoyancy at first order" %}
      <div class="card-body">
        <h5 class="card-title">Buoyancy at first order</h5>
        <p class="card-text">A first-order correction predicts how stratification changes instabilities without re-solving the eigenvalue problem; under pseudo-boiling, buoyancy significantly affects transition.</p>
        <a href="https://doi.org/10.1017/jfm.2026.11653" class="card-link">Journal of Fluid Mechanics, 2026</a>
      </div>
    </div>
  </div>
</div>

### Transition to turbulence at supercritical pressure

Direct numerical simulations with CUBENS follow the full path from small disturbances to turbulence in boundary layers with supercritical fluids.

<div class="row">
  <div class="col-md-4 mb-4">
    <div class="card h-100 res-card">
      {% include figure.liquid loading="lazy" path="assets/img/publication_preview/JFM_billows.jpg" class="card-img-top" alt="Billows at the Widom line" %}
      <div class="card-body">
        <h5 class="card-title">Billows at the Widom line</h5>
        <p class="card-text">A single two-dimensional wave creates Kelvin–Helmholtz-like billows and near-wall flow reversal around the Widom line, triggering transition early.</p>
        <a href="https://doi.org/10.1017/jfm.2025.10993" class="card-link">Journal of Fluid Mechanics, 2025</a>
      </div>
    </div>
  </div>
  <div class="col-md-4 mb-4">
    <div class="card h-100 res-card">
      {% include figure.liquid loading="lazy" path="assets/img/publication_preview/ETMM_qvort.jpg" class="card-img-top" alt="H-type breakdown" %}
      <div class="card-body">
        <h5 class="card-title">H-type breakdown</h5>
        <p class="card-text">With the wall above the pseudo-boiling temperature, Λ-vortices alternate with velocity and density streaks before hairpin vortices form.</p>
        <a href="https://www.researchgate.net/publication/373683624_Direct_numerical_simulation_of_H-type_transition_in_a_flat-plate_boundary_layer_with_supercritical_fluids" class="card-link">ETMM14, 2023</a>
      </div>
    </div>
  </div>
  <div class="col-md-4 mb-4">
    <div class="card h-100 res-card">
      {% include figure.liquid loading="lazy" path="assets/img/publication_preview/IUTAM_qvort.jpg" class="card-img-top" alt="K-type breakdown" %}
      <div class="card-body">
        <h5 class="card-title">K-type breakdown</h5>
        <p class="card-text">Beyond pseudo-boiling, streak secondary instabilities add hairpin vortices, yet transition is significantly delayed compared with the liquid-like case.</p>
        <a href="https://doi.org/10.1007/978-981-96-9829-5_33" class="card-link">IUTAM Transition, 2026</a>
      </div>
    </div>
  </div>
</div>

### Numerical simulation of non-ideal fluid flows

Open-source, high-order solvers make large simulations of non-ideal fluid flows affordable on modern supercomputers.

<div class="row">
  <div class="col-md-6 mb-4">
    <div class="card h-100 res-card">
      {% include figure.liquid loading="lazy" path="assets/img/publication_preview/CUBENS_logo.png" class="card-img-top" alt="CUBENS" %}
      <div class="card-body">
        <h5 class="card-title">CUBENS</h5>
        <p class="card-text">An open-source, GPU-accelerated DNS solver for non-ideal fluids, running on NVIDIA and AMD GPUs and scaling up to 512 GPUs.</p>
        <a href="https://doi.org/10.1016/j.cpc.2025.109507" class="card-link">Computer Physics Communications, 2025</a>
      </div>
    </div>
  </div>
  <div class="col-md-6 mb-4">
    <div class="card h-100 res-card">
      {% include figure.liquid loading="lazy" path="assets/img/publication_preview/JCP_Sanath.png" class="card-img-top" alt="Non-ideal fluid flows in closed systems" %}
      <div class="card-body">
        <h5 class="card-title">Non-ideal fluid flows in closed systems</h5>
        <p class="card-text">A low-Mach-number method for non-ideal fluids in closed systems that keeps the thermodynamic pressure, the equation of state and global mass consistent.</p>
        <a href="https://arxiv.org/abs/2607.29224" class="card-link">arXiv, 2026</a>
      </div>
    </div>
  </div>
</div>

**Code:** [CUBENS](https://github.com/pcboldini/CUBENS) · [DragHeat-NIF](https://github.com/pcboldini/DragAndHeatTransferEstimation_NonIdealFluids)

### Laminar flow control

Within the ERC-funded MetaWing project, I study how metamaterial surfaces and wall-based concepts can keep boundary layers laminar for longer on wings, reducing skin-friction drag and noise. Harmonic Navier–Stokes methods predict how surface features and flow-control devices change the growth of instabilities.

<div class="row justify-content-center">
  <div class="col-md-6 mb-4">
    <div class="card h-100 res-card">
      {% include figure.liquid loading="lazy" path="assets/img/research/DeHNSSo_logo.svg" class="card-img-top" alt="DeHNSSo-v2" %}
      <div class="card-body">
        <h5 class="card-title">DeHNSSo-v2</h5>
        <p class="card-text">Extends the Delft Harmonic Navier–Stokes Solver to compressible flows over curved geometries, with automatic grids and about ten times faster nonlinear runs.</p>
        <a href="https://github.com/pcboldini/DeHNSSo" class="card-link">Code on GitHub (paper submitted to CPC)</a>
      </div>
    </div>
  </div>
</div>

### Earlier work: hypersonic and rarefied flows

Before my PhD, at the University of Stuttgart and Tsinghua University, I studied thermal non-equilibrium effects on hypersonic transition, crossflow transition control on cones, and rarefied-flow intakes for atmosphere-breathing electric propulsion (EU project DISCOVERER).

<div class="publications">
{% bibliography --query @*[key=10.1007/978-981-13-3305-7_41 || key=CitekeyMastersthesis || key=10.1063/1.4967689] --group_by none %}
</div>
