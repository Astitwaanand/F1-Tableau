(() => {
  const viz = document.querySelector("#race-viz");
  const pointButtons = [...document.querySelectorAll("[data-story-index]")];
  const progress = document.querySelector("#story-progress");
  if (!viz || pointButtons.length === 0) return;

  let story = null;
  const setActive = (index, caption = "") => {
    pointButtons.forEach((button) => {
      const active = Number(button.dataset.storyIndex) === index;
      button.classList.toggle("is-current", active);
      button.setAttribute("aria-pressed", String(active));
    });
    if (progress) {
      const title = caption || pointButtons[index]?.querySelector("strong")?.textContent || "Story point";
      progress.textContent = `${String(index + 1).padStart(2, "0")} / ${String(pointButtons.length).padStart(2, "0")} · ${title}`;
    }
  };

  viz.addEventListener("firstinteractive", () => {
    const activeSheet = viz.workbook?.activeSheet;
    if (Array.isArray(activeSheet?.storyPointsInfo)) {
      story = activeSheet;
      const activePoint = activeSheet.activeStoryPoint;
      if (activePoint) setActive(activePoint.index, activePoint.caption);
    }
  });

  viz.addEventListener("storypointswitched", (event) => {
    const point = event.detail?.newStoryPoint;
    if (point) setActive(point.index, point.caption);
  });

  pointButtons.forEach((button) => {
    button.addEventListener("click", async () => {
      const index = Number(button.dataset.storyIndex);
      try {
        story ||= viz.workbook?.activeSheet;
        if (typeof story?.activateStoryPointAsync !== "function") throw new Error("The published view is not a Tableau Story.");
        await story.activateStoryPointAsync(index);
        setActive(index);
        document.querySelector(".viz-panel")?.scrollIntoView({ behavior: "smooth", block: "start" });
      } catch (error) {
        if (progress) progress.textContent = error.message || "Story point could not be opened.";
      }
    });
  });
})();
