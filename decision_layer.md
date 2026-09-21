# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T22:44:38.506281+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 8.397 | entrée 7.150 | trend 8.700 | rang 7.911
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BIGTIME-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.687 | entrée 6.150 | trend 8.450 | rang 7.532
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CELO-EUR | action LATENT_ACCELERATOR | opportunité 7.487 | entrée 5.700 | trend 8.700 | rang 7.455
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COW-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.649 | entrée 6.250 | trend 8.900 | rang 8.115
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.115
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.001
3. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.911

## Accélération indépendante

- XMN-EUR — CONFIRMED_ACCELERATION — score 8.438/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — CONFIRMED_ACCELERATION — score 7.228/10 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — BUILDING_ACCELERATION — score 6.030/10 — DETECTED_BUT_TOO_LATE
- FTT-EUR — BUILDING_ACCELERATION — score 6.011/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWEAT-EUR — BUILDING_ACCELERATION — score 5.970/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 5.515/10 — DETECTED_BUT_TOO_LATE
- GRASS-EUR — BUILDING_ACCELERATION — score 5.475/10 — DETECTED_BUT_TOO_LATE
- CHIP-EUR — BUILDING_ACCELERATION — score 4.762/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 9.738/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.767/10 — sources ACCELERATION — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.732/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XMN-EUR — ACTIVE_NOW — score mémoire 8.438/10 — sources ACCELERATION — WATCH_ONLY
- SFP-EUR — MEMORY_24H — score mémoire 8.323/10 — sources ACCELERATION — MEMORY_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.115/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.001/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.911/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ICX-EUR +92.85% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +89.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +55.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZETA-EUR +51.91% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- FORM-EUR +39.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SWELL-EUR +36.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +34.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +33.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +23.59% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- GRASS-EUR +21.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
