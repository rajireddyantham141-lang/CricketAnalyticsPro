const matchesEl = document.getElementById("matches");
const searchEl = document.getElementById("search");
let allMatches = [];

function renderMatches(items) {
  document.getElementById("matchCount").textContent = `${items.length} shown`;
  if (!items.length) {
    matchesEl.innerHTML = '<div class="empty">No matching demo matches. Try another search.</div>';
    return;
  }
  matchesEl.innerHTML = items.map(m => `
    <article class="match-card">
      <div class="card-top"><span>${escapeHtml(m.tournament)} · ${escapeHtml(m.format)}</span><span class="status">${escapeHtml(m.status)}</span></div>
      <div class="teams">
        <div class="team">${escapeHtml(m.team1)}<strong class="score">${escapeHtml(m.score1)}</strong></div>
        <div class="team">${escapeHtml(m.team2)}<strong class="score">${escapeHtml(m.score2)}</strong></div>
      </div>
      <div class="result">${escapeHtml(m.result)}</div>
      <p class="summary">${escapeHtml(m.venue)} · ${escapeHtml(m.summary)}</p>
    </article>`).join("");
}
function escapeHtml(value) {
  return String(value ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
}
async function init() {
  try {
    const response = await fetch("/api/matches");
    if (!response.ok) throw new Error("API unavailable");
    const payload = await response.json();
    allMatches = payload.matches || [];
    renderMatches(allMatches);
    const a = await fetch("/api/analysis");
    const analysis = await a.json();
    document.getElementById("insights").innerHTML = (analysis.insights || []).map(x => `<div class="insight">${escapeHtml(x)}</div>`).join("");
  } catch (error) {
    matchesEl.innerHTML = '<div class="empty">Could not load match data. Please refresh the page.</div>';
    document.getElementById("matchCount").textContent = "Unavailable";
    document.getElementById("insights").textContent = "Analytics service is unavailable.";
  }
}
searchEl.addEventListener("input", () => {
  const q = searchEl.value.trim().toLowerCase();
  renderMatches(allMatches.filter(m => [m.team1,m.team2,m.tournament,m.venue,m.format].join(" ").toLowerCase().includes(q)));
});
document.getElementById("clearSearch").addEventListener("click", () => { searchEl.value = ""; renderMatches(allMatches); });
init();
