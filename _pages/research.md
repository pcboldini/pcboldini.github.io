---
layout: page
permalink: /research/
title: research
description: Instability and transition in compressible and non-ideal fluid flows
nav: true
nav_order: 1
---

I study how laminar flows become turbulent, and how this transition can be predicted and controlled, in flows where compressibility and real-fluid effects change the physics. My work combines stability analysis, high-fidelity simulations and high-performance computing, supported by open-source codes. The full list of papers is on the [publications](/publications/) page, and my PhD work is collected in my [thesis](https://repository.tudelft.nl/record/uuid:f9203cce-d2bd-460f-879d-8dfa4fb1bfa7).

<br>

### Instabilities in non-ideal fluids

Near the Widom line, small temperature changes cause large variations of density, viscosity and heat capacity, which reshape the stability of boundary layers.

- A new unstable mode, linked to a minimum of kinematic viscosity at the Widom line
- Instability in strongly stratified plane Couette flow
- Transient growth in heated and cooled boundary layers
- First-order buoyancy correction of modal instabilities

<div class="publications">
{% bibliography --query @*[key=Boldini4 || key=Bugeat2] --group_by none %}
</div>

**Related:** [Bugeat22](https://www.researchgate.net/publication/368395270_On_the_new_unstable_mode_in_the_boundary_layer_flow_of_supercritical_fluids) · [Boldini24](https://doi.org/10.1103/PhysRevFluids.9.083901)

<br>

### Transition to turbulence at supercritical pressure

Direct numerical simulations follow the full path from small disturbances to turbulence in boundary layers with supercritical fluids.

- K- and H-type transition in flat-plate boundary layers
- Complete transition to turbulence with a fluid at supercritical pressure
- Effect of the Widom line on the transition process

<div class="publications">
{% bibliography --query @*[key=Boldini3 || key=boldini2024directnumericalsimulationsktype || key=Boldini3ETMM] --group_by none %}
</div>

<br>

<div class="row justify-content-sm-center">
    <div class="col-sm-5 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/research/DeHNSSo_logo.svg" class="img-fluid" %}
    </div>
</div>

### Laminar flow control

Within the ERC-funded MetaWing project, I study how to keep boundary layers laminar for longer on wings, reducing skin-friction drag and noise.

- Metamaterial surfaces and wall-based concepts for transition delay
- Harmonic Navier–Stokes methods for stability and receptivity with surface features
- DeHNSSo-v2: curvilinear grids, compressible flows and strongly nonlinear regimes

**Papers:** Boldini26c (submitted to Computer Physics Communications)
<!-- TODO: link Boldini26c to arXiv once available -->

**Code:** [DeHNSSo](https://github.com/pcboldini/DeHNSSo)

<br>

### GPU-accelerated simulation of non-ideal fluids

Open-source, high-order solvers make large simulations of non-ideal fluid flows affordable on modern supercomputers.

- GPU-resident DNS solver, ported with OpenACC to NVIDIA and AMD GPUs
- Cubic equations of state for non-ideal fluids
- Skin-friction and heat-transfer estimates for turbulent non-ideal boundary layers
- Mass-preserving method for low-Mach-number real-gas flows in closed systems

<div class="publications">
{% bibliography --query @*[key=Boldini2 || key=Kotturshettar2026] --group_by none %}
</div>

**Code:** [CUBENS](https://github.com/pcboldini/CUBENS) · [DragHeat-NIF](https://github.com/pcboldini/DragAndHeatTransferEstimation_NonIdealFluids)

<br>

### Earlier work: hypersonic and rarefied flows

Before my PhD, at the University of Stuttgart and Tsinghua University, I worked on high-speed and rarefied flows.

- Thermal non-equilibrium effects on hypersonic boundary-layer transition
- Hypersonic boundary-layer stability with high-temperature effects
- Crossflow transition control in hypersonic boundary layers on cones
- Rarefied-flow intakes for atmosphere-breathing electric propulsion (EU project DISCOVERER)

<div class="publications">
{% bibliography --query @*[key=10.1007/978-981-13-3305-7_41 || key=CitekeyMastersthesis || key=10.1063/1.4967689] --group_by none %}
</div>
