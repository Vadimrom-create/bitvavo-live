# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T18:22:06.634635+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 8.289 | entrée 6.950 | trend 8.400 | rang 7.883
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : WAL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.239 | entrée 5.850 | trend 9.200 | rang 7.997
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : JUP-EUR | action LATENT_ACCELERATOR | opportunité 7.820 | entrée 5.750 | trend 8.600 | rang 7.585
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.264 | entrée 5.700 | trend 8.950 | rang 7.947
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.997
2. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.947
3. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.883

## Accélération indépendante

- PTB-EUR — CONFIRMED_ACCELERATION — score 8.142/10 — DETECTED_BUT_TOO_LATE
- CROSS-EUR — CONFIRMED_ACCELERATION — score 7.467/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYN-EUR — CONFIRMED_ACCELERATION — score 7.416/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 6.818/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MEGA-EUR — CONFIRMED_ACCELERATION — score 6.573/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AIOZ-EUR — CONFIRMED_ACCELERATION — score 6.542/10 — DETECTED_BUT_TOO_LATE
- NPC-EUR — BUILDING_ACCELERATION — score 6.461/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ATH-EUR — BUILDING_ACCELERATION — score 6.343/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CPOOL-EUR — BUILDING_ACCELERATION — score 6.230/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — BUILDING_ACCELERATION — score 6.033/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- RON-EUR — MEMORY_24H — score mémoire 9.938/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- THQ-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 8.588/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FARTCOIN-EUR — MEMORY_24H — score mémoire 8.408/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SFP-EUR — MEMORY_24H — score mémoire 8.323/10 — sources ACCELERATION — MEMORY_ONLY
- ZKJ-EUR — MEMORY_24H — score mémoire 8.224/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +171.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +101.66% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZETA-EUR +56.63% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- FORM-EUR +41.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +36.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AIOZ-EUR +25.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SWELL-EUR +25.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEPE-EUR +24.76% — DETECTED_EARLY — couche NONE — action NONE
- PTB-EUR +23.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +22.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
