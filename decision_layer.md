# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T22:57:29.225891+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 8.761 | entrée 7.650 | trend 8.700 | rang 8.131
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AERO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.789 | entrée 6.750 | trend 8.450 | rang 7.602
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CELO-EUR | action LATENT_ACCELERATOR | opportunité 7.505 | entrée 5.700 | trend 8.700 | rang 7.465
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.502 | entrée 6.450 | trend 9.200 | rang 8.188
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.188
2. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.131
3. SUPER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.094

## Accélération indépendante

- NEAR-EUR — BUILDING_ACCELERATION — score 6.437/10 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — BUILDING_ACCELERATION — score 5.044/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHIP-EUR — BUILDING_ACCELERATION — score 4.965/10 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — BUILDING_ACCELERATION — score 4.951/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 9.738/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.767/10 — sources ACCELERATION — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.732/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY
- SFP-EUR — MEMORY_24H — score mémoire 8.323/10 — sources ACCELERATION — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.188/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.131/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 8.094/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.005/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +89.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +75.29% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AIOZ-EUR +53.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZETA-EUR +52.44% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- FORM-EUR +41.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +36.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +35.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SWELL-EUR +33.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +22.69% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- GRASS-EUR +22.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
