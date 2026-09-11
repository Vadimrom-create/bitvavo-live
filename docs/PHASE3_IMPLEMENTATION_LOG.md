# Phase 3 — implementation evidence

Starting commit: `6312a153e80e0e4c9b06c5e6672c541149caefbf`.
Architecture: `ASTRA_PHASE3_RECONCILED_PLAN_2026-09-11.md`.
All prospective data starts as TECHNICAL_PILOT, never held-out.

## Lot 1 — References and identities

- Checked remote main, clean isolated checkout, workflows, and four intervening data-only commits. No preceding implementation to reuse.
- Baseline: 61 tests pass. New reference/identity tests fail before implementation, then pass.
- Protected initial market journals, frozen V4 sources and DL-V1 by Git blob hash. Old truncated audit checkout untouched.
- Separated data, decision, execution and evaluation identifiers; no scoring or execution behavior changed.
- Rollback: remove new documentation/identity consumers only; never alter protected history.
- Private validation and deployed legacy daemon: PENDING PRIVATE CONFIGURATION / DEPLOYMENT VERIFICATION.

## Resume checkpoint — 2026-09-11

- Resume SHA `ab475f17ac3a1a95a5b15a41bc1f601f4fad33bf`, branch `codex/astra-phase3-20260911`. Only untracked `tests/test_executor_safety.py`; lot 2 still RED, no production change. Lot 1 is the only completed lot; no phase-3 commit published.
- Remote main `7efa5dc77e818611e839b8d02809aaf63a017359`: 34 additional data-only commits, 17 new market/DL journals; no source/workflow change. Latest eight scheduled runs successful, newest `34596469789`. None validates phase-3 code.
- Re-read complete architectural plan and launch/resume scope. Previous validation: 61 baseline + 2 lot-1 tests; historical V4 raw replay not rerun; DL-V1 audit evidence remains distinct.
- Runtime dependencies did not survive session restart; restored from declared requirements before continuing executor tests. Old audit checkout and all historical artifacts preserved.

## Lot 2 — Legacy executor closed and private

- Reproduced 13 failing assertions in the six previously written safety tests before interruption; implementation now passes all six. Full suite: 69 tests pass.
- Central GET-only transport rejects POST/PUT/PATCH/DELETE before signing or network, including the secondary cancellation route. Environment settings cannot reopen execution; approvals are always rejected.
- Missing/restarted state freezes; malformed state fails explicitly. Public status schema v2 is a strict seven-field whitelist; stdout contains only a generic event code. Private state/events keep diagnostics with mode 0600.
- Sentinel payloads and nested private values tested at caller and publication transport boundaries; zero mutation transport calls. No real account or SMTP access.
- CI installs the existing executor requirements for its new test suite. V4/DL-V1 code and histories unchanged; no market replay needed for this isolated lot.
- Rollback: stop legacy publication/daemon, retain central closure. Exposure ledger remains deferred, not claimed implemented.
- Deployed daemon SHA and prior publicly committed private details cannot be verified/remediated from the repository alone: PENDING PRIVATE CONFIGURATION / DEPLOYMENT VERIFICATION.

## Lot 3 — Independent critical monitoring

- New isolation tests reproduced eager-buy import failure, candle calls preceding justified exits, and absence of a standalone workflow. After changes: 23 monitoring tests and 73 total tests pass; workflow YAML parses.
- Dedicated monitoring workflow has its own timeout/concurrency, no needs dependency, a pinned release SHA and exact cryptography/cffi/pycparser dependencies. Current encrypted state is copied separately from main; only this workflow sends SMTP. CI runs monitoring/data/shadow/executor suites independently.
- Quotes for every holding are assessed first. An exit/partial event prevents candle enrichment and optional buy imports. Fault injection at optional input boundaries covers six named external-failure contexts; no real external outage or email delivery is claimed.
- Publisher commits/rebases only a temporary publication worktree, preserving executing HEAD. Concurrent distinct-file publication succeeds; conflicting same-state publication refuses. Test expectation updated to require the source checkout stay unchanged.
- Private telemetry records successful evaluation intervals and account/book ages; failed/UNCONFIGURED cycles do not become successful monitoring. SMTP accepted followed by state-save failure is explicitly uncertain.
- New buy module retains the original top-one selection until lot 8. Workflow new buys remain disabled until coherent manifests and fallback are validated. No V2 route exists.
- Public live CI no longer commits observations back onto a review branch; validation artifacts remain uploadable. No historical source or journal changed. No V4/DL-V1 replay required for this isolated lot.
- Rollback: pin previous validated monitoring SHA with current encrypted state; never restore a second sender. Real account, SMTP and seven-day cadence: PENDING PRIVATE CONFIGURATION. Release pin is recorded in the immediately following metadata commit after validation.

## Lot 4 — Minimum temporal contract

- Four new temporal tests failed before implementation; five targeted tests now pass, full suite 78 tests pass.
- PublicClient.capture binds copied content and metadata, request/response identity, per-consumer/key sequence and availability cutoff. Refreshed same-URL responses coexist. ReplayClient replays consumer-bound responses with no network fallback; old journals retain their legacy reader.
- Source-close bound uses request start plus measured server offset minus clock uncertainty; HTTP Date is retained separately and is not a market-content timestamp. Actual cache closure correction follows in lot 5.
- Pipeline records four policy identities, input snapshot/cutoff and separate baseline/diagnostic readiness. This lot still labels legacy inputs LEGACY_OBSERVED_V1; later diagnostics do not become earlier V4 inputs.
- Downloaded actual CI raw snapshot from run 34596469789, artifact 10261523827. Local replay of 20260911T115709Z-f616cf19: frozen reference = instrumented = recorded live, 50 watch rows. All 113 DL-V1 journals present in the starting checkout replay exactly on every field returned by decide.
- Source/historical blob protections pass. No historical journal or baseline source changed. Rollback: legacy replay reader remains; reject ambiguous inputs rather than replacing an earlier response.

## Lot 5 — Per-profile cache and source-closed inputs

- Four cache/closure tests failed before implementation. Targeted tests cover AAA + insufficient NEW, restart, failure without clock renewal, three-hour expiry, BTC/ETH dependency freshness, crossing request/close boundaries and unchanged daily-profile formula.
- New TrendCache keeps each market's attempt/acquisition/source independently; TTL remains 90 minutes and maximum age three hours. Expired references cannot silently confer fresh relative strength. Original v4_common.py is untouched.
- Versioned V4 adapter filters candles according to request-start clock bound and supplies corrected profiles without editing the frozen formulas. Corrected rolling states and journals use separate namespaces; no synthetic freshness migration from legacy cache. --data-policy CORRECTED_INPUTS_V1 selects this path.
- Legacy V4 plus repaired diagnostic data is explicitly LEGACY_V4_CORRECTED_DIAGNOSTICS_V1, with separate journals; it is not relabeled as original historical input policy. The default CLI retains this reference path until prospective orchestration is installed.
- Diagnostics and monitoring bind candle content/metadata. A cache captured before closure cannot acquire that closure on later read; insufficient latest closure remains unavailable. Post-baseline diagnostic reception has its own cutoff, not an earlier V4 timestamp.
- Full pipeline fixture exercises legacy and corrected paths in isolated subprocesses and exact consumer-aware replay against both frozen and instrumented engines. A cold-cache {} replay initialization discrepancy was found and fixed. These fabricated fixture observations are not saved into repository journals.
- 83 tests pass. Actual CI raw legacy replay 20260911T115709Z-f616cf19 remains exact (50 watch rows). V4/DL-V1 source and historical hash invariants pass; prior 113 DL-V1 replays remain valid.
- Rollback: suspend corrected consumer / reject ambiguous closure; retain its logs and original replay mode. Live corrected acquisition still needs a prospective run; private monitoring remains PENDING PRIVATE CONFIGURATION. Monitoring release pin will advance after all critical-path changes are validated.

## Lot 6 — Historical continuity and explicit output scopes

- Reproduced false onset across a 3h50 gap. Three new tests cover the gap, continuous sequence, reverse input order, duplicate/conflicting bars, partial crossing bar and a previously detected market outside a 70-market current top.
- HISTORY_CONTINUITY_V2 checks the entire 13-bar link and rejects unclosed/invalid/contradictory inputs. Insufficient observability does not assign detection lead or FN.
- Current published-list presence and complete-journal diagnostics are separate outputs; historical rows have no 50/40/20 cap. Legacy aliases carry explicit current-only scope. Pages and documentation link both.
- Actual latest starting-checkout scan 20260911T065702Z-cc6756ed inspected after index reconstruction: 428 markets, 12 observable short-event diagnostics, 407 insufficient-continuity, 9 no-event. This is a development diagnostic, not performance validation.
- 86 tests pass, including both complete pipeline/replay fixtures. V4/DL-V1 algorithms unchanged; historical source/hash protections pass. No old report or journal rewritten.
- Rollback: suspend the new diagnostic report; retain versioned raw journals and explicit alias scope.

## Lot 7 — Data capabilities and real producer contracts

- Five new tests initially failed; 91 tests now pass, including historical IOST observation and complete frozen/corrected replay fixtures.
- CAPABILITIES_V1 separately records structure, measured entry, immediate execution, inactive passive planning, retrace observation and outcome-reference availability with reasons and source IDs. Coverage is exposed globally and by category. Missing future labels remain unknown.
- Structural proof requires source-closed 15m data and fresh local/BTC/ETH profiles at consumption; missing secondary 5m data can leave structure usable while entry is unavailable. A 4.5 entry default with NOT_ENTRY_ENRICHED remains untouched in the baseline and becomes UNKNOWN/null only in the new view.
- Actual historical IOST stays UNVERIFIABLE with unknown entry; the complete synthetic case has distinct evidence. No outcome or historical winner influenced thresholds.
- Spread severity includes WIDE_SPREAD_RISK and WIDE_SPREAD with monotone constraints. All five real wick statuses are decoded; execution-only reasons are separated from price-confirmation reasons. No is_wick_setup dependency, numeric wick penalty or global prefix veto is introduced.
- Raw data_quality, exclusions and V1 payloads are retained. The new interpretation is for the forthcoming versioned consumer; its inactive planning capability does not authorize a trade.
- Rollback: disable the new consumer/view, preserve raw histories and block any new activation whose execution proof is unavailable.

## Second resume checkpoint — 2026-09-11

- Resume SHA `4223ab99848362ed4310dbe5b59f6e856fdd20bf`; clean branch `codex/astra-phase3-20260911`. Lots 1–7 have eight local commits (lot 3 has a separate validated-release pin). No phase-3 branch/commit has been published. Lot 8 had not yet been modified.
- Remote main now `d5a450a728c2493ed2b525526941cffd7339d26a`, 70 data-only commits after phase start, no source/workflow diff. Last five scheduled runs successful, latest 34627687210. These remain pre-phase-3 workflows.
- Rechecked immutable architectural document SHA256 `2583ebb02e91ee0dd4b7db94dd6b2a9b0108503423be787b30b20da6e27fe9c8`, remaining sections and launch/resume scope. No methodology/order change.
- Previously validated: 91 tests; actual frozen V4 replay exact; 113 DL-V1 exact replays; both full pipeline fixture paths exact. Private/deployed validations remain pending. Restored executor dependencies lost in the resumed runtime; no code change needed for that environment issue.

## Lot 8 — One eligible buy after local fallback

- Reproduced top-AA rejection losing valid BB, stale-account traversal and multiple BUY actions at the final boundary. Five targeted tests pass, including real runner + simulated SMTP failure/retry and private encrypted delivery state. Full suite: 96 tests pass; independent critical suite: 23 pass.
- ranked_eligible_events returns the full V4 ranking with unchanged cooldown/episode rules; select_events keeps the historical one-result interface. Global account/budget failures stop before candidate reads. Local held/correlation/drift/read failures permit the next candidate.
- A bounded optional acquisition loop returns only the first valid candidate and checks the canonical current spread. Final action selection rejects all buys when management is pending and caps BUY at one. Freshness is rechecked immediately before simulated notification by the existing critical runner.
- Pipeline publishes all qualified V4 alternatives for private fallback, without prematurely consuming hypothetical portfolio budget; its separate theoretical proposal output is capped at one. Actual private risk/portfolio checks remain in the final selector.
- Only BB receives delivery markers after SMTP acknowledgement; failed delivery creates none. V2/non-V4 policy identities are refused. Optional-buy tests are kept outside the critical monitoring gate so a broken buy import cannot block exits.
- Both pipeline/replay fixtures pass; no V4/DL-V1 source/history mutation. Rollback: disable optional new buys, retain position monitoring and current encrypted delivery state. Coherent buy manifests are added in lot 11 before workflow buy enablement is considered.

## Lot 9 — Opportunity baseline V2, shadow only

- Six initial V2 tests failed; eight targeted tests now pass, full suite 104 tests pass. Additional checks cover explicit scan mismatch, unchanged active-output sentinel and byte-stable original shadow readiness on replay.
- DL_V2_OPPORTUNITY_BASELINE_SHADOW ranks verified candidates by Opportunity descending, market ascending for ties. Trend/Entry determine eligibility/readiness; no recurrence/chase/wick additive score, no calibrated probabilities or optimality claim. Five experimental threshold values are unchanged.
- Unknown entry with verified structure can be latent; unverified structure remains awaiting revalidation. Entry crossing 5.80/6.80 does not erase surveillance. Negative 24h change is not a pullback. Existing PULLBACK mode plus closed declining candles records descriptive reference/invalidation, without a new resumption trigger.
- Passive bucket describes an inactive candidate; trade_plan remains null. Support-price and resumption hypotheses are explicitly DEFERRED_OPTIONAL_SHADOW_EXPERIMENT, disabled independently. No invented ask, fill or active proposal.
- New run_shadow.py requires journal + scan_id + version, hashes its source snapshot, writes separate policy/data journals and preserves initial readiness on replay. It runs V1 without modifying decide or old journals. Workflow passes runtime/current_scan.json explicitly; shadow failures are isolated from valid V4 publication.
- Source stage distinguishes TECHNICAL_PILOT, SIMULATED_FIXTURE and old-data DEVELOPMENT_REPLAY; a historical replay is not relabeled prospective. Current code revision is recorded from Git rather than assuming an environment SHA matches checkout.
- Real starting-checkout latest scan inspected with V2: 430 observations awaiting revalidation because old source proofs are unavailable; no forced IOST rescue. All 113 original V1 journals still replay exactly. Both full V4 pipeline/replay fixtures pass; histories/source blob protections pass.
- Rollback: disable the V2 runner and retain its journals. Core privacy, temporal and monitoring fixes remain. Actual prospective V2 collection and comparison wiring follow in lots 10–12.

## Lot 10 — comparateur technique (repris après le lot 9)

- Reproduction : huit tests initialement en erreur (comparateur absent). Treize tests ciblés passent après implémentation : identité des politiques, déduplication/réordre, latence, publication perdue/inconnue, G indépendant du veto, censure, futur au-delà du cutoff, fenêtres absentes, données non reconstructibles, budget séparé et OHLC ambigu/gap/coûts.
- Ajouts : `research/comparison.py`, `scripts/run_comparison.py`, `tests/test_comparison.py`. Le scan contient la sortie V4 réellement produite, la métadonnée de marché et l'heure de disponibilité après stabilisation (le timestamp du callback avant stabilisation n'était pas cette disponibilité).
- Les plans théoriques sont construits ex ante par les mêmes règles ; aucune activation DL-V2. Journaux/cycles séparés et immuables. Publication native inconnue jusqu'au reçu prévu au lot 11 ; elle n'est pas simulée comme réussie.
- Non-régression : **117 tests passent**, dont les deux pipelines complets avec replay exact de leurs consommations V4. Les sources frozen V4/V1 et leurs journaux de départ conservent leurs empreintes.
- Convention documentée : disponibilité commune cutoff + 120 s pour le pilote, à inclure dans le gel ; pas de modification des seuils de trading. La séparation 4h ne prouve pas l'indépendance des épisodes. Les contrastes de données absents restent indisponibles.
- Limites explicites : aucune donnée prospective mature ni rendement validé ; le stade natif mesuré est la publication, les étapes privées de consommation/notification restent à configurer. Aucune causalité « avant le mouvement » déduite du seul délai jusqu'à cible.
- Rollback : désactiver le rapport comparatif sans retirer ses sources ; achats V2 et expériences toujours désactivés. Le code critique de monitoring n'importe pas le comparateur.
- Point suivant : lot 11, index reconstructible, séparation des sorties/workflows et reçus de publication cohérents.
