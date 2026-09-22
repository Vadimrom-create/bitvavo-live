# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T00:49:54.813739+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WAL-EUR | action ACHETE_MAINTENANT | opportunité 8.699 | entrée 7.100 | trend 9.200 | rang 8.222
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CELO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.203 | entrée 5.800 | trend 8.750 | rang 7.689
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 8.149 | entrée 5.200 | trend 8.400 | rang 7.530
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GRT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.117 | entrée 6.900 | trend 8.300 | rang 8.135
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.222
2. GRT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.135
3. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.076

## Accélération indépendante

- OSMO-EUR — CONFIRMED_ACCELERATION — score 7.728/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRUMP-EUR — CONFIRMED_ACCELERATION — score 6.648/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEAR-EUR — CONFIRMED_ACCELERATION — score 6.603/10 — DETECTED_BUT_TOO_LATE
- ENA-EUR — BUILDING_ACCELERATION — score 6.478/10 — DETECTED_BUT_TOO_LATE
- MEW-EUR — BUILDING_ACCELERATION — score 6.178/10 — DETECTED_BUT_TOO_LATE
- GMT-EUR — BUILDING_ACCELERATION — score 5.897/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HAEDAL-EUR — BUILDING_ACCELERATION — score 5.716/10 — DETECTED_BUT_TOO_LATE
- RUNE-EUR — BUILDING_ACCELERATION — score 5.689/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RAY-EUR — BUILDING_ACCELERATION — score 5.670/10 — DETECTED_BUT_TOO_LATE
- C98-EUR — BUILDING_ACCELERATION — score 5.621/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WLD-EUR — ACTIVE_NOW — score mémoire 7.255/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DATAIP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.738/10 — sources ACCELERATION — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.204/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.732/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY
- SFP-EUR — MEMORY_24H — score mémoire 8.323/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ICX-EUR +109.84% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +83.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +49.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZETA-EUR +46.43% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +35.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +34.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +33.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SWELL-EUR +31.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEPE-EUR +24.02% — DETECTED_EARLY — couche NONE — action NONE
- WIF-EUR +22.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
