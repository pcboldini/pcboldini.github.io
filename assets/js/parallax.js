// gentle parallax: the background art (body::before / ::after) moves slower than the page;
// on wide screens the side panels pan from top to bottom of the art as the page scrolls
(function () {
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  const root = document.documentElement;
  let ticking = false;
  const update = () => {
    const max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    root.style.setProperty("--scroll", window.scrollY + "px");
    root.style.setProperty("--scrollfrac", Math.min(1, window.scrollY / max).toFixed(4));
    ticking = false;
  };
  window.addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  update();
})();
