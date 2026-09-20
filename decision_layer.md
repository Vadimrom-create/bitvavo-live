# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T19:39:08.256048+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : JUP-EUR | action ACHETE_MAINTENANT | opportunité 8.298 | entrée 7.100 | trend 8.450 | rang 7.887
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : W-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.568 | entrée 6.500 | trend 8.100 | rang 7.280
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZIL-EUR | action LATENT_ACCELERATOR | opportunité 7.425 | entrée 4.500 | trend 8.750 | rang 7.346
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RUNE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.885 | entrée 6.100 | trend 8.200 | rang 7.998
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.998
2. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.931
3. JUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.887

## Accélération indépendante

- EDEN-EUR — CONFIRMED_ACCELERATION — score 8.850/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NES-EUR — CONFIRMED_ACCELERATION — score 8.668/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SKL-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- EGLD-EUR — CONFIRMED_ACCELERATION — score 7.205/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 6.349/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XMN-EUR — BUILDING_ACCELERATION — score 6.223/10 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — BUILDING_ACCELERATION — score 5.850/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — BUILDING_ACCELERATION — score 4.857/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAGA-EUR — BUILDING_ACCELERATION — score 4.769/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.613/10 — sources V4 — BUYABLE_NOW
- EDEN-EUR — ACTIVE_NOW — score mémoire 8.850/10 — sources ACCELERATION, V4 — WATCH_ONLY
- NES-EUR — ACTIVE_NOW — score mémoire 8.668/10 — sources ACCELERATION — WATCH_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- C-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SKL-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- RUNE-EUR — ACTIVE_NOW — score mémoire 7.998/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.931/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.887/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.861/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +50.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +26.22% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +25.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +21.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +19.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +16.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +16.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +15.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CELR-EUR +15.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +14.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
