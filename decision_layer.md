# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T09:09:57.777641+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SHIB-EUR | action ACHETE_MAINTENANT | opportunité 9.019 | entrée 7.250 | trend 7.050 | rang 7.596
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CRO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.964 | entrée 6.650 | trend 7.300 | rang 7.683
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RED-EUR | action LATENT_ACCELERATOR | opportunité 7.753 | entrée 4.500 | trend 8.650 | rang 7.330
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HBAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.203 | entrée 8.000 | trend 7.850 | rang 7.966
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HBAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.966
2. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.834
3. TAIKO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.805

## Accélération indépendante

- GIGA-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — CONFIRMED_ACCELERATION — score 8.130/10 — DETECTED_BUT_TOO_LATE
- BOB-EUR — CONFIRMED_ACCELERATION — score 7.480/10 — DETECTED_BUT_TOO_LATE
- CHILLGUY-EUR — CONFIRMED_ACCELERATION — score 6.876/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- THQ-EUR — CONFIRMED_ACCELERATION — score 6.744/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — DETECTED_BUT_TOO_LATE
- HNT-EUR — BUILDING_ACCELERATION — score 5.723/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEAQ-EUR — BUILDING_ACCELERATION — score 5.460/10 — DETECTED_BUT_TOO_LATE
- LMWR-EUR — BUILDING_ACCELERATION — score 5.290/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DYDX-EUR — BUILDING_ACCELERATION — score 5.205/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 9.015/10 — sources ACCELERATION — MEMORY_ONLY
- GIGA-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- PONKE-EUR — ACTIVE_NOW — score mémoire 8.130/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- HBAR-EUR — ACTIVE_NOW — score mémoire 7.966/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — MEMORY_24H — score mémoire 7.941/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 7.834/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TAIKO-EUR — ACTIVE_NOW — score mémoire 7.805/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 7.768/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BAT-EUR — ACTIVE_NOW — score mémoire 7.754/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ICX-EUR +125.67% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +89.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +45.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +36.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +24.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WIF-EUR +23.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +20.92% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +19.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- THQ-EUR +17.39% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CARV-EUR +17.34% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
